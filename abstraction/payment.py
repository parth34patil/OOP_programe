# Example of abstraction using abstract base classes for payment gateways

from abc import ABC, abstractmethod

# Abstract base class for payment gateways
class Paymentgetway(ABC):
    # Abstract method to be implemented by subclasses
    @abstractmethod
    def payment_process(self, amount):
        pass

    # Concrete method to show payment status
    def payment_status(self):
        print("payment status is success")

# Subclass representing Phonepe payment gateway
class Phonepe(Paymentgetway):
    # Implementation of abstract method for Phonepe
    def payment_process(self, amount):
        print(f"Payment of  ${amount} processed through Phonepe")

# Subclass representing Google Pay payment gateway
class googlepay(Paymentgetway):
    # Implementation of abstract method for Google Pay
    def payment_process(self, amount):
        print(f"Payment of {amount} processed through Google Pay")

# Creating instances and processing payments
p1 = Phonepe()
g1 = googlepay()

p1.payment_process(1000)
p1.payment_status()

g1.payment_process(2000)
g1.payment_status()