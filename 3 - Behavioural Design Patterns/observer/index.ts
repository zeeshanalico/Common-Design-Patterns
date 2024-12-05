namespace Custom{
  interface Observer {
    update(message: string): void;
  }

  class EmailMsgListener implements Observer {
    private email: string;

    constructor(email: string) {
      this.email = email;
    }

    update(message: string): void {
      console.log(`Email to ${this.email}: ${message}`);
    }
  }

  // Notification Class (Holds a list of EmailMsgListeners)
  class Notification {
    private emailListeners: EmailMsgListener[] = [];

    // Add a new EmailMsgListener to the notification
    addEmailListener(listener: EmailMsgListener): void {
      this.emailListeners.push(listener);
    }

    // Remove an EmailMsgListener from the notification
    removeEmailListener(listener: EmailMsgListener): void {
      const index = this.emailListeners.indexOf(listener);
      if (index !== -1) {
        this.emailListeners.splice(index, 1);
      }
    }

    // Notify all email listeners (customers) with a message
    sendNotification(message: string): void {
      for (const listener of this.emailListeners) {
        listener.update(message);
      }
    }
  }

  // Store Class (Subject)
  class Store {
    private notification: Notification;

    constructor() {
      this.notification = new Notification();
    }

    // Add an observer (Email listener)
    addObserver(listener: EmailMsgListener): void {
      this.notification.addEmailListener(listener);
    }

    // Remove an observer (Email listener)
    removeObserver(listener: EmailMsgListener): void {
      this.notification.removeEmailListener(listener);
    }

    // Create a notification and notify all customers
    createNotification(message: string): void {
      this.notification.sendNotification(message);
    }
  }

  // Example usage
  const store = new Store();

  // Create customers (observers)
  const customer1 = new EmailMsgListener('customer1@example.com');
  const customer2 = new EmailMsgListener('customer2@example.com');

  // Add customers to the store's list of email listeners
  store.addObserver(customer1);
  store.addObserver(customer2);

  // Create a new notification
  store.createNotification('New sale on your favorite items! 20% off now!');

  // Remove customer2 and send another notification
  store.removeObserver(customer2);
  store.createNotification('Special offer for members only!');
}