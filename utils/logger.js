/**
 * Centralized Logger Utility
 * Can be reused across backend or frontend projects
 */

function generateRequestId() {
  return `req-${Date.now()}-${Math.floor(Math.random() * 1000)}`;
}

function logInfo(message, meta = {}) {
  console.log(
    JSON.stringify({
      level: "INFO",
      timestamp: new Date().toISOString(),
      message,
      ...meta,
    })
  );
}

function logError(message, meta = {}) {
  console.error(
    JSON.stringify({
      level: "ERROR",
      timestamp: new Date().toISOString(),
      message,
      ...meta,
    })
  );
}

module.exports = {
  generateRequestId,
  logInfo,
  logError,
};
