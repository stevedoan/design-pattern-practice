from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def notify(self, message):
        pass


class LoggingObserver(Observer):
    def notify(self, message: str):
        print("Logging {message}")


class UserObserver(Observer):
    def notify(self, message: str):
        print("Notify all related users: {message}")


class BroadcastMessage:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)

    def broadcast(self, message):
        for observer in self.observers:
            observer.notify(message)
