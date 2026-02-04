const { generateRequestId, logInfo, logError } = require("./utils/logger");

const requestId = generateRequestId();

logInfo("Demo request started", { requestId });

try {
  throw new Error("Something went wrong");
} catch (err) {
  logError(err.message, { requestId });
}
