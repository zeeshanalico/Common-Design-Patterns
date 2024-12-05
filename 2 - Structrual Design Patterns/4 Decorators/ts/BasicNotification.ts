interface Notification {
    send(message: string): void;
}

class BasicNotification implements Notification {
    send(message: string): void {
        console.log(`Sending basic notification: ${message}`);
    }
}
export  { BasicNotification, Notification };