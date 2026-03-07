(function () {
  const form = document.getElementById("export-form");
  const statusEl = document.getElementById("status");
  const downloadEl = document.getElementById("download");

  const setStatus = (obj) => {
    statusEl.textContent =
      typeof obj === "string" ? obj : JSON.stringify(obj, null, 2);
  };

  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    downloadEl.textContent = "";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;
    setStatus("Export in progress. This can take a while...");

    try {
      const res = await fetch("/.netlify/functions/diigo-export-download", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ username, password }),
      });
      if (!res.ok) {
        const body = await res.json();
        setStatus(body);
        return;
      }
      const ndjson = await res.text();
      const blob = new Blob([ndjson], { type: "application/x-ndjson" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "diigo-bookmarks.ndjson";
      a.textContent = "Download diigo-bookmarks.ndjson";
      downloadEl.textContent = "";
      downloadEl.appendChild(a);
      a.click();
      setStatus("Export complete.");
    } catch (err) {
      setStatus({ error: String(err) });
    }
  });
})();
