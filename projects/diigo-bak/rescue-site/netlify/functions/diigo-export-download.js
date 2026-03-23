const { getConfig, checkWindow } = require("./_config");
const { checkAndConsume } = require("./_rate-limit");
const { fetchAllBookmarks } = require("./_diigo-client");

exports.handler = async (event) => {
  const cfg = getConfig();
  if (event.httpMethod !== "POST") {
    return {
      statusCode: 405,
      headers: { "content-type": "application/json; charset=utf-8" },
      body: JSON.stringify({ error: "method not allowed" }),
    };
  }
  const windowCheck = checkWindow(cfg);
  if (!windowCheck.ok) {
    return {
      statusCode: windowCheck.status,
      headers: { "content-type": "application/json; charset=utf-8" },
      body: JSON.stringify({ error: windowCheck.message }),
    };
  }

  let body;
  try {
    body = JSON.parse(event.body || "{}");
  } catch {
    body = {};
  }
  const username = String(body.username || "").trim();
  const password = String(body.password || "");
  if (!username || !password) {
    return {
      statusCode: 400,
      headers: { "content-type": "application/json; charset=utf-8" },
      body: JSON.stringify({ error: "username and password are required" }),
    };
  }

  const limit = checkAndConsume({
    dayKey: cfg.dayKey,
    username,
    maxUserStartsPerDay: cfg.maxUserStartsPerDay,
    maxGlobalStartsPerDay: cfg.maxGlobalStartsPerDay,
  });
  if (!limit.ok) {
    return {
      statusCode: limit.status,
      headers: { "content-type": "application/json; charset=utf-8" },
      body: JSON.stringify({ error: limit.message }),
    };
  }

  const lines = [];
  try {
    for await (const page of fetchAllBookmarks({
      username,
      password,
      apiKey: cfg.diigoApiKey,
      knownIp: cfg.knownIp,
    })) {
      for (const item of page) {
        lines.push(JSON.stringify(item));
      }
    }
  } catch (err) {
    return {
      statusCode: 502,
      headers: { "content-type": "application/json; charset=utf-8" },
      body: JSON.stringify({
        error: String(err && err.message ? err.message : err),
      }),
    };
  }

  return {
    statusCode: 200,
    headers: {
      "content-type": "application/x-ndjson; charset=utf-8",
      "content-disposition": 'attachment; filename="diigo-bookmarks.ndjson"',
      "cache-control": "no-store",
    },
    body: lines.join("\n") + (lines.length ? "\n" : ""),
  };
};
