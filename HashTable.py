from HashMethods import HashMethod
from enum import Enum


class CollStrategy(Enum):
    NEXT = 0
    CHAINING = 1
    LINEAR = 2
    SQUARE = 3


class HashTable:

    def __init__(self, table_size: int,
                 hash_method: HashMethod = None,
                 coll_strategy: CollStrategy = None,
                 coll_params: dict = None):
        self.table_size = table_size
        self.hash_table = [None] * table_size
        self.hash_func = None
        self.coll_strategy = CollStrategy.NEXT
        self.coll_params = {}

        if hash_method is not None:
            self.set_hash_method(hash_method)

        if coll_strategy is not None:
            self.set_collision_strategy(coll_strategy, coll_params)

    def set_hash_method(self, method: HashMethod):
        method.set_table_size(self.table_size)
        self.hash_func = method.get_hash

    def set_collision_strategy(self, strategy: CollStrategy, params: dict):
        self.coll_strategy = strategy
        self.coll_params = params

    def add_item(self, item):
        if CollStrategy.NEXT == self.coll_strategy:
            self._add_item_next_strategy(item)

        elif CollStrategy.LINEAR == self.coll_strategy:
            self._add_item_linear_strategy(item)

        elif CollStrategy.SQUARE == self.coll_strategy:
            self._add_item_square_strategy(item)

        elif CollStrategy.CHAINING == self.coll_strategy:
            self._add_item_chaining_strategy(item)

    def _add_item_next_strategy(self, item):
        h = self.hash_func(item)

        init_h = h

        while self.hash_table[h] is not None:
            h = (h + 1) % self.table_size

            if h == init_h:
                raise Exception("HashTable is full")

        self.hash_table[h] = item

    def _add_item_linear_strategy(self, item):
        h = self.hash_func(item)
        q = self.coll_params.get("q")
        i = 1
        init_h = h

        while self.hash_table[h] is not None:
            h = (h + (i * q)) % self.table_size

            if h == init_h:
                raise Exception("HashTable is full")

        self.hash_table[h] = item

    def _add_item_square_strategy(self, item):
        h = self.hash_func(item)
        init_h = h
        q = 0

        while self.hash_table[h] is not None:
            q = (q + 1) ** 2
            h = (h + q) % self.table_size

            if h == init_h:
                raise Exception("HashTable is full")

        self.hash_table[h] = item

    def _add_item_chaining_strategy(self, item):
        h = self.hash_func(item)

        if self.hash_table[h] is None:
            self.hash_table[h] = []

        self.hash_table[h].append(item)

    def print_table(self):
        for i in range(self.table_size):
            print(f"h(key)={i}", self.hash_table[i])
