class HashMethod:
    def __init__(self):
        self.table_size = 0

    def set_table_size(self, table_size):
        self.table_size = table_size

    def get_hash(self, key):
        raise Exception("Hash function is not defined")


class DivisionMethod(HashMethod):

    def get_hash(self, key):
        return key % self.table_size


class MultiplicativeMethod(HashMethod):

    def __init__(self, a):
        super().__init__()
        self.a = a

    def get_hash(self, key):
        t = (key * self.a) % 1
        t = (t * self.table_size) // 1
        return int(t)


class MidSquareMethod(HashMethod):

    def get_hash(self, key):
        t = key**2
        t = t >> 11
        return t % 1024

