class Jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Whoah! Too many Cookies!")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
           raise ValueError("Don't take too many Cookies!")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        if size < 0 or size > self.capacity:
            raise ValueError
        self._size = size
