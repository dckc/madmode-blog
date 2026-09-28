const { getConfig, checkWindow } = require("./_config");
const { getJob, purgeOldJobs } = require("./_jobs");

function json(statusCode, body) {
  return {
    statusCode,
    headers: { "content-type": "application/json; charset=utf-8" },
    body: JSON.stringify(body),
  };
}

exports.handler = async (event) => {
  const cfg = getConfig();
  purgeOldJobs(cfg.maxDownloadAgeMs);

  const id = event.queryStringParameters && event.queryStringParameters.id;
  if (!id) {
    return json(400, { error: "missing id" });
  }
  const job = getJob(id);
  if (!job) {
    return json(404, { error: "job not found or expired" });
  }

  const windowCheck = checkWindow(cfg);
  if (!windowCheck.ok && job.state !== "done") {
    return json(windowCheck.status, {
      id: job.id,
      state: "expired",
      fetched: job.fetched,
      error: windowCheck.message,
    });
  }

  return json(200, {
    id: job.id,
    state: job.state,
    fetched: job.fetched,
    error: job.error,
    createdAt: job.createdAt,
    updatedAt: job.updatedAt,
  });
};
