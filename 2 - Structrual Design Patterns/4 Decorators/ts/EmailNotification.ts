import NotificationDecorator from "./NotificationDecorator";
export class EmailNotificationDecorator extends NotificationDecorator {
    send(message: string): void {
        super.send(message);
        this.sendEmail(message);  // Additional behavior
    }

    private sendEmail(message: string): void {
        console.log(`Sending email notification: ${message}`);
    }
}