exports.handler = async () => {
  return {
    statusCode: 501,
    headers: { "content-type": "application/json; charset=utf-8" },
    body: JSON.stringify({
      error: "not implemented",
      note: "Current build runs export work directly from export-start.",
    }),
  };
};
