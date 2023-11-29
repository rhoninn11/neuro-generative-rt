import queue

class pipe_queue():
    def __init__(self, name):
        self.queue = queue.Queue()
        self.name = name

    def queue_item(self, item):
        self.queue.put(item)

    def dequeue_item(self):
        item = self.queue.get()
        return item

    def queue_len(self):
        return self.queue.qsize()