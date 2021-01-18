class BufferFullException(Exception):
    def __str__(self):
        return "Buffer is full"


class BufferEmptyException(Exception):
    def __str__(self):
        return "Buffer is empty"


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = []
        self.buffer_len = capacity

    def read(self):
        if self.buffer:
            val = self.buffer[0]
            del self.buffer[0]
            return val
        else:
            raise BufferEmptyException

    def write(self, data):
        if self.buffer_len == len(self.buffer):
            raise BufferFullException
        else:
            self.buffer.append(data)

    def overwrite(self, data):
        if self.buffer_len > len(self.buffer):
            self.write(data)
        else:
            self.clear()
            self.write(data)

    def clear(self):
        try:
            if not self.buffer:
                raise BufferEmptyException
        except BufferEmptyException:
            pass
        else:
            del self.buffer[0]
