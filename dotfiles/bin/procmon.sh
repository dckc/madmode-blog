#!/bin/bash
#
# Process census snapshot.
#
# Context: `pstree -s -p $$` showed PIDs in the millions after only a few
# days of uptime (e.g. bash(2252311), script(3282662)). We're collecting
# these aggregate stats to determine whether that is normal PID allocation
# on this machine or whether some process is burning through the PID space
# abnormally fast.
#

proc_comm() {
    local pid=$1
    local file="/proc/${pid}/comm"
    if [[ -r "$file" ]]; then
        tr -d '\n' < "$file" 2>/dev/null || echo '?'
    else
        echo '?'
    fi
}

proc_ppid() {
    local pid=$1
    local file="/proc/${pid}/status"
    if [[ -r "$file" ]]; then
        awk '/^PPid:/{print $2; exit}' "$file" 2>/dev/null || echo 0
    else
        echo 0
    fi
}

mapfile -t pids < <(ls /proc | grep -E '^[0-9]+$' | sort -n)
count=${#pids[@]}

if [[ $count -eq 0 ]]; then
  max=0
  min=0
  median=0
else
  max=${pids[-1]}
  min=${pids[0]}
  if (( count % 2 == 1 )); then
    median=${pids[$((count / 2))]}
  else
    a=${pids[$((count / 2 - 1))]}
    b=${pids[$((count / 2))]}
    median=$(( (a + b) / 2 ))
  fi
fi

fields=(
  'MESSAGE=process census snapshot'
  'SYSLOG_IDENTIFIER=procmon'
  "PROC_COUNT=${count}"
  "PROC_MIN_PID=${min}"
  "PROC_MAX_PID=${max}"
  "PROC_MEDIAN_PID=${median}"
)

# Top 3 newest (highest-numbered) processes, with their parent.
for i in 1 2 3; do
    idx=$(( count - i ))
    if (( idx < 0 )); then
        break
    fi
    pid=${pids[$idx]}
    comm=$(proc_comm "$pid")
    ppid=$(proc_ppid "$pid")
    pcomm=$(proc_comm "$ppid")
    fields+=(
        "PROC_TOP${i}_PID=${pid}"
        "PROC_TOP${i}_COMM=${comm}"
        "PROC_TOP${i}_PPID=${ppid}"
        "PROC_TOP${i}_PCOMM=${pcomm}"
    )
done

printf '%s\n' "${fields[@]}" | logger --journald
