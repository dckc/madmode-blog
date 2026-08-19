function parseTs(name) {
  const raw = process.env[name];
  if (!raw) {
    return null;
  }
  const ms = Date.parse(raw);
  if (Number.isNaN(ms)) {
    return null;
  }
  return ms;
}

function utcDay(ms) {
  return new Date(ms).toISOString().slice(0, 10);
}

function getConfig(now = Date.now()) {
  return {
    enabled: process.env.RESCUE_ENABLED !== "false",
    startAt: parseTs("RESCUE_START_AT"),
    sunsetAt: parseTs("RESCUE_SUNSET_AT"),
    diigoApiKey: process.env.DIIGO_API_KEY || "",
    knownIp: process.env.DIIGO_KNOWN_IP || "54.148.192.94",
    maxActiveJobs: Number(process.env.MAX_ACTIVE_JOBS || "3"),
    maxGlobalStartsPerDay: Number(process.env.MAX_GLOBAL_STARTS_PER_DAY || "50"),
    maxUserStartsPerDay: Number(process.env.MAX_USER_STARTS_PER_DAY || "5"),
    maxDownloadAgeMs: Number(
      process.env.MAX_DOWNLOAD_AGE_MS || String(60 * 60 * 1000),
    ),
    now,
    dayKey: utcDay(now),
  };
}

function checkWindow(cfg) {
  if (!cfg.enabled) {
    return { ok: false, status: 503, message: "service disabled" };
  }
  if (!cfg.diigoApiKey) {
    return { ok: false, status: 503, message: "server is not configured" };
  }
  if (cfg.startAt === null || cfg.sunsetAt === null) {
    return {
      ok: false,
      status: 503,
      message: "start/sunset timestamps are not configured",
    };
  }
  if (cfg.sunsetAt - cfg.startAt > 72 * 60 * 60 * 1000) {
    return {
      ok: false,
      status: 503,
      message: "invalid window: must be 72h or less",
    };
  }
  if (cfg.now < cfg.startAt) {
    return { ok: false, status: 403, message: "service not open yet" };
  }
  if (cfg.now >= cfg.sunsetAt) {
    return { ok: false, status: 410, message: "service window has ended" };
  }
  return { ok: true };
}

module.exports = {
  getConfig,
  checkWindow,
};
