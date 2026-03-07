const { getConfig } = require("./_config");
const { getJob, purgeOldJobs } = require("./_jobs");

exports.handler = async (event) => {
  const cfg = getConfig();
  purgeOldJobs(cfg.maxDownloadAgeMs);

  const id = event.queryStringParameters && event.queryStringParameters.id;
  if (!id) {
    return {
      statusCode: 400,
      body: "missing id",
    };
  }

  const job = getJob(id);
  if (!job) {
    return {
      statusCode: 404,
      body: "job not found or expired",
    };
  }
  if (job.state !== "done") {
    return {
      statusCode: 409,
      body: "job not complete",
    };
  }

  return {
    statusCode: 200,
    headers: {
      "content-type": "application/x-ndjson; charset=utf-8",
      "content-disposition": 'attachment; filename="diigo-bookmarks.ndjson"',
      "cache-control": "no-store",
    },
    body: job.ndjson,
  };
};
