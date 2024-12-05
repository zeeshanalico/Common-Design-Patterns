import { BasicNotification ,Notification} from "./BasicNotification";
import { EmailNotificationDecorator } from "./EmailNotification";
import { SMSNotificationDecorator } from "./SMSNotifcationDecorator";

let notification: Notification = new BasicNotification();
// notification = new EmailNotificationDecorator(notification);  
// notification = new SMSNotificationDecorator(notification);    

notification= new SMSNotificationDecorator(new EmailNotificationDecorator(notification));

notification.send("You've got a new message!");