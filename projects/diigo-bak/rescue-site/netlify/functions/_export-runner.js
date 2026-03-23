const { fetchAllBookmarks } = require("./_diigo-client");
const { updateJob } = require("./_jobs");

async function runExportJob({ jobId, username, password, apiKey, knownIp }) {
  updateJob(jobId, { state: "running", error: null });
  const lines = [];
  let fetched = 0;
  try {
    for await (const page of fetchAllBookmarks({
      username,
      password,
      apiKey,
      knownIp,
    })) {
      for (const item of page) {
        lines.push(JSON.stringify(item));
      }
      fetched += page.length;
      updateJob(jobId, { fetched });
    }
    updateJob(jobId, {
      state: "done",
      fetched,
      ndjson: lines.join("\n") + (lines.length ? "\n" : ""),
    });
  } catch (err) {
    updateJob(jobId, {
      state: "error",
      error: String(err && err.message ? err.message : err),
    });
  } finally {
    // Scrub local references.
    username = "";
    password = "";
  }
}

module.exports = {
  runExportJob,
};
