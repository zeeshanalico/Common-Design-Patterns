import NotificationDecorator from "./NotificationDecorator";
export class SMSNotificationDecorator extends NotificationDecorator {
    send(message: string): void {
        super.send(message);
        this.sendSMS(message);  // Additional behavior
    }

    private sendSMS(message: string): void {
        console.log(`Sending SMS notification: ${message}`);
    }
}