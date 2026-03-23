const crypto = require("crypto");

const jobs = new Map();

function makeJobId() {
  return "j_" + crypto.randomBytes(16).toString("hex");
}

function usernameHash(username) {
  return crypto.createHash("sha256").update(username).digest("hex").slice(0, 16);
}

function createJob({ usernameHashValue, now }) {
  const id = makeJobId();
  const job = {
    id,
    state: "queued",
    fetched: 0,
    createdAt: now,
    updatedAt: now,
    usernameHash: usernameHashValue,
    ndjson: "",
    error: null,
  };
  jobs.set(id, job);
  return job;
}

function getJob(id) {
  return jobs.get(id) || null;
}

function updateJob(id, patch) {
  const job = jobs.get(id);
  if (!job) {
    return null;
  }
  Object.assign(job, patch, { updatedAt: Date.now() });
  jobs.set(id, job);
  return job;
}

function countActiveJobs() {
  let n = 0;
  for (const job of jobs.values()) {
    if (job.state === "queued" || job.state === "running") {
      n += 1;
    }
  }
  return n;
}

function purgeOldJobs(maxAgeMs, now = Date.now()) {
  for (const [id, job] of jobs.entries()) {
    if (now - job.createdAt > maxAgeMs) {
      jobs.delete(id);
    }
  }
}

module.exports = {
  usernameHash,
  createJob,
  getJob,
  updateJob,
  countActiveJobs,
  purgeOldJobs,
};
