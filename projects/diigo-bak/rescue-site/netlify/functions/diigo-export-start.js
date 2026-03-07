const { getConfig, checkWindow } = require("./_config");
const {
  createJob,
  countActiveJobs,
  purgeOldJobs,
  usernameHash,
} = require("./_jobs");
const { checkAndConsume } = require("./_rate-limit");
const { runExportJob } = require("./_export-runner");

function json(statusCode, body) {
  return {
    statusCode,
    headers: { "content-type": "application/json; charset=utf-8" },
    body: JSON.stringify(body),
  };
}

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") {
    return json(405, { error: "method not allowed" });
  }
  const cfg = getConfig();
  const windowCheck = checkWindow(cfg);
  if (!windowCheck.ok) {
    return json(windowCheck.status, { error: windowCheck.message });
  }

  purgeOldJobs(cfg.maxDownloadAgeMs);
  if (countActiveJobs() >= cfg.maxActiveJobs) {
    return json(429, { error: "too many active exports; try later" });
  }

  let body;
  try {
    body = JSON.parse(event.body || "{}");
  } catch {
    return json(400, { error: "invalid JSON body" });
  }
  const username = String(body.username || "").trim();
  const password = String(body.password || "");
  if (!username || !password) {
    return json(400, { error: "username and password are required" });
  }

  const limit = checkAndConsume({
    dayKey: cfg.dayKey,
    username,
    maxUserStartsPerDay: cfg.maxUserStartsPerDay,
    maxGlobalStartsPerDay: cfg.maxGlobalStartsPerDay,
  });
  if (!limit.ok) {
    return json(limit.status, { error: limit.message });
  }

  const job = createJob({
    usernameHashValue: usernameHash(username),
    now: cfg.now,
  });

  runExportJob({
    jobId: job.id,
    username,
    password,
    apiKey: cfg.diigoApiKey,
    knownIp: cfg.knownIp,
  });

  return json(202, {
    jobId: job.id,
    state: job.state,
    statusUrl: "/.netlify/functions/diigo-export-status?id=" + job.id,
    downloadUrl: "/.netlify/functions/diigo-export-download?id=" + job.id,
  });
};
