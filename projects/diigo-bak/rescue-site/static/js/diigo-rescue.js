(function () {
  const form = document.getElementById("export-form");
  const statusEl = document.getElementById("status");
  const outputEl = document.getElementById("output");

  const setStatus = (obj) => {
    statusEl.textContent =
      typeof obj === "string" ? obj : JSON.stringify(obj, null, 2);
  };

  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    outputEl.value = "";

    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;
    const count = 100;
    let start = 0;
    let pageNo = 0;
    let total = 0;
    setStatus("Starting export...");

    try {
      for (;;) {
        pageNo += 1;
        setStatus(
          "Fetching page " + pageNo + " starting from record " + (start + 1),
        );
        const res = await fetch("/.netlify/functions/diigo-export-page", {
          method: "POST",
          headers: { "content-type": "application/json" },
          body: JSON.stringify({ username, password, start, count }),
        });
        const body = await res.json();
        if (!res.ok) {
          setStatus(body);
          return;
        }
        if (body.ndjson) {
          outputEl.value += body.ndjson;
        }
        total += body.fetched || 0;
        if (body.done) {
          setStatus("Export complete. Total records: " + total);
          return;
        }
        start = body.nextStart;
      }
    } catch (err) {
      setStatus({ error: String(err) });
    }
  });
})();
