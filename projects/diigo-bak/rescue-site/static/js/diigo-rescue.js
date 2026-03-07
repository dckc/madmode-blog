(function () {
  const form = document.getElementById("export-form");
  const statusEl = document.getElementById("status");
  const downloadEl = document.getElementById("download");

  let pollTimer = null;

  const setStatus = (obj) => {
    statusEl.textContent =
      typeof obj === "string" ? obj : JSON.stringify(obj, null, 2);
  };

  const stopPolling = () => {
    if (pollTimer) {
      clearTimeout(pollTimer);
      pollTimer = null;
    }
  };

  const pollStatus = async (jobId) => {
    try {
      const res = await fetch(
        "/.netlify/functions/diigo-export-status?id=" +
          encodeURIComponent(jobId),
      );
      const body = await res.json();
      setStatus(body);
      if (!res.ok || body.state === "error" || body.state === "expired") {
        stopPolling();
        return;
      }
      if (body.state === "done") {
        stopPolling();
        const url =
          "/.netlify/functions/diigo-export-download?id=" +
          encodeURIComponent(jobId);
        downloadEl.innerHTML =
          '<a href="' + url + '">Download diigo-bookmarks.ndjson</a>';
        return;
      }
      pollTimer = setTimeout(() => pollStatus(jobId), 2000);
    } catch (err) {
      setStatus({ error: String(err) });
      stopPolling();
    }
  };

  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    stopPolling();
    downloadEl.textContent = "";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;
    setStatus("Starting export...");

    try {
      const res = await fetch("/.netlify/functions/diigo-export-start", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      const body = await res.json();
      setStatus(body);
      if (!res.ok) {
        return;
      }
      pollStatus(body.jobId);
    } catch (err) {
      setStatus({ error: String(err) });
    }
  });
})();
