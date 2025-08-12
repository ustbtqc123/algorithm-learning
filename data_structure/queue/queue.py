class QueueEmptyError(Exception):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            raise QueueEmptyError("Queue is empty, cannot dequeue.")

    def size(self):
        return len(self.queue)
