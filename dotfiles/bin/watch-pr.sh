#!/bin/bash
# Watch a GitHub PR and notify when it merges or CI fails
# Usage: watch-pr.sh <PR_NUMBER> [REPO]

PR=${1:?Usage: watch-pr.sh <PR_NUMBER> [REPO]}
REPO=${2:-Agoric/agoric-sdk}

echo "Watching PR #$PR in $REPO..."

while true; do
  state=$(gh pr view $PR -R $REPO --json state -q '.state')

  if [[ "$state" == "MERGED" ]]; then
    notify-send "PR #$PR Merged" "$REPO PR merged successfully"
    exit 0
  fi

  # Check for required CI failure only
  if gh pr checks $PR -R $REPO --required 2>/dev/null | grep -q "fail"; then
    notify-send -u critical "PR #$PR CI Failed" "Check GitHub for details"
    exit 1
  fi

  if [[ "$state" == "CLOSED" ]]; then
    notify-send "PR #$PR Closed" "PR was closed without merging"
    exit 1
  fi

  sleep 60
done
