# Example of abstraction using abstract base classes for notifications

from abc import ABC, abstractmethod  # Import ABC and abstractmethod

# Abstract base class for notification servers
class Notifiactionserver(ABC):

    # Abstract method to be implemented by subclasses
    @abstractmethod
    def senf_notification(Self, message):
        pass

# Subclass representing an email notification server
class EmailNotificationServer(Notifiactionserver):

    # Implementation of abstract method for email notifications
    def senf_notification(Self, message):
        print(f"notification from Email:{message}")

# Subclass representing an SMS notification server
class smsnotification(Notifiactionserver):

    # Implementation of abstract method for SMS notifications
    def senf_notification(Self, message):
        print(f"notification from SMS:{message}")

# Creating instances and sending notifications
e1 = EmailNotificationServer()
e1.senf_notification("Hello, this is a test email notification.")

s1 = smsnotification()
s1.senf_notification("Hello, this is a test SMS notification.")