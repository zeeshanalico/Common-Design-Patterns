from abc import ABC, abstractmethod

#in py we can create interface like functionality using Abstract Base class with @abstractmethod and without its implemetation using 'pass'
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

class BasicNotification(Notification):
    def send(self, message: str):
        print(f"Sending basic notification: {message}")

class NotificationDecorator(Notification):
    def __init__(self, notification: Notification):
        self._wrapped_notification = notification

    def send(self, message: str):
        # Delegates call to the wrapped notification
        self._wrapped_notification.send(message)

# Email notification decorator
class EmailNotificationDecorator(NotificationDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_email(message)  # Additional behavior

    def send_email(self, message: str):
        print(f"Sending email notification: {message}")

# SMS notification decorator
class SMSNotificationDecorator(NotificationDecorator):
    def send(self, message: str):
        super().send(message)
        self.send_sms(message)  # Additional behavior

    def send_sms(self, message: str):
        print(f"Sending SMS notification: {message}")

# Usage
notification = BasicNotification()
# notification = EmailNotificationDecorator(notification)  # Wrap with email decorator
notification = SMSNotificationDecorator(notification)    # Wrap with SMS decorator

notification.send("You've got a new message!")
