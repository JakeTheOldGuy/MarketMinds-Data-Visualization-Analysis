class Publisher:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify(self, data):
        for subscriber in self.subscribers:
            subscriber.update(data)


class Subscriber:
    def update(self, data):
        raise NotImplementedError("Subscribers must implement the update method.")
