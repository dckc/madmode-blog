const https = require("https");
const { URLSearchParams } = require("url");

const API_HOST = "secure.diigo.com";
const API_BASE = "https://secure.diigo.com/api/v2";

function authHeader(username, password) {
  const token = Buffer.from(username + ":" + password, "utf8").toString("base64");
  return "Basic " + token;
}

async function requestPrimary(path, headers) {
  const res = await fetch(API_BASE + path, { method: "GET", headers });
  const text = await res.text();
  return {
    status: res.status,
    body: text,
  };
}

function requestKnownIp(path, headers, knownIp) {
  return new Promise((resolve, reject) => {
    const req = https.request(
      {
        host: knownIp,
        port: 443,
        method: "GET",
        path: "/api/v2" + path,
        servername: API_HOST,
        headers: Object.assign({}, headers, { Host: API_HOST }),
      },
      (res) => {
        let data = "";
        res.setEncoding("utf8");
        res.on("data", (chunk) => {
          data += chunk;
        });
        res.on("end", () => {
          resolve({ status: res.statusCode || 0, body: data });
        });
      },
    );
    req.on("error", reject);
    req.end();
  });
}

function parseArray(body) {
  const parsed = JSON.parse(body);
  if (!Array.isArray(parsed)) {
    throw new Error("unexpected Diigo response shape");
  }
  return parsed;
}

async function requestPage({
  username,
  password,
  apiKey,
  start,
  count,
  knownIp,
}) {
  const params = new URLSearchParams({
    user: username,
    sort: "2",
    filter: "all",
    start: String(start),
    count: String(count),
    key: apiKey,
  });
  const path = "/bookmarks?" + params.toString();
  const headers = {
    Authorization: authHeader(username, password),
    Accept: "application/json",
  };

  try {
    const primary = await requestPrimary(path, headers);
    if (primary.status === 200) {
      return parseArray(primary.body);
    }
    if (primary.status === 401) {
      throw new Error("authentication failed");
    }
  } catch (err) {
    // Fall through to known-ip strategy.
    if (!knownIp) {
      throw err;
    }
  }

  if (!knownIp) {
    throw new Error("Diigo API unavailable");
  }
  const fallback = await requestKnownIp(path, headers, knownIp);
  if (fallback.status === 200) {
    return parseArray(fallback.body);
  }
  if (fallback.status === 401) {
    throw new Error("authentication failed");
  }
  throw new Error("Diigo API unavailable: HTTP " + String(fallback.status));
}

async function* fetchAllBookmarks({
  username,
  password,
  apiKey,
  knownIp,
  pageSize = 100,
}) {
  let start = 0;
  for (;;) {
    const page = await requestPage({
      username,
      password,
      apiKey,
      start,
      count: pageSize,
      knownIp,
    });
    if (page.length === 0) {
      return;
    }
    yield page;
    start += pageSize;
  }
}

module.exports = {
  fetchAllBookmarks,
};
