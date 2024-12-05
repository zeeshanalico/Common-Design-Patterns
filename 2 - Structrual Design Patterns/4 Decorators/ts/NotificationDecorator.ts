import { Notification } from "./BasicNotification";
abstract class NotificationDecorator implements Notification {
    protected wrappedNotification: Notification;

    constructor(notification: Notification) {
        this.wrappedNotification = notification;
    }

    send(message: string): void {
        this.wrappedNotification.send(message);  
    }
}
export default NotificationDecorator;



