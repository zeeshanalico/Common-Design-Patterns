namespace Custom { 
  class Request{
    isAuthenticated: boolean;
    isAuthorized: boolean;
  }


interface Handler {
  setNext(handler: Handler): Handler;
  handle(request: Request): void;
}

class LoggingHandler implements Handler {
  private nextHandler: Handler;

  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler;
  }

  handle(request: Request): void {
    console.log("Logging request...");
    if (this.nextHandler) this.nextHandler.handle(request);
  }
}

class AuthenticationHandler implements Handler {
  private nextHandler: Handler;

  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler;
  }

  handle(request: Request): void {
    if (!request.isAuthenticated) {
      console.log("Authentication failed. Stopping chain.");
      return; // Stop the chain here if authentication fails
    }
    console.log("User authenticated.");
    if (this.nextHandler) this.nextHandler.handle(request);
  }
}

class AuthorizationHandler implements Handler {
  private nextHandler: Handler;

  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler;
  }

  handle(request: Request): void {
    if (!request.isAuthorized) {
      console.log("Authorization failed. Stopping chain.");
      return;
    }
    console.log("User authorized.");
    if (this.nextHandler) this.nextHandler.handle(request);
  }
}

// Usage
const request = { isAuthenticated: false, isAuthorized: true };

const logger = new LoggingHandler();
const authenticator = new AuthenticationHandler();
const authorizer = new AuthorizationHandler();

logger.setNext(authenticator).setNext(authorizer);

logger.handle(request);
}