const perUserByDay = new Map();
const globalByDay = new Map();

function _key(dayKey, username) {
  return dayKey + "|" + username.toLowerCase();
}

function _bump(map, key) {
  const n = (map.get(key) || 0) + 1;
  map.set(key, n);
  return n;
}

function _read(map, key) {
  return map.get(key) || 0;
}

function checkAndConsume({ dayKey, username, maxUserStartsPerDay, maxGlobalStartsPerDay }) {
  const userKey = _key(dayKey, username);
  const gKey = dayKey;

  const userCount = _read(perUserByDay, userKey);
  if (userCount >= maxUserStartsPerDay) {
    return {
      ok: false,
      status: 429,
      message: "daily per-user export limit reached",
      userCount,
    };
  }

  const globalCount = _read(globalByDay, gKey);
  if (globalCount >= maxGlobalStartsPerDay) {
    return {
      ok: false,
      status: 429,
      message: "daily service cap reached",
      globalCount,
    };
  }

  _bump(perUserByDay, userKey);
  _bump(globalByDay, gKey);
  return { ok: true };
}

module.exports = {
  checkAndConsume,
};
