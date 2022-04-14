from HashTable import HashTable, CollStrategy
from HashMethods import DivisionMethod, MultiplicativeMethod, MidSquareMethod


def main():
    """
    Hash methods:
        - DivisionMethod()
        - MultiplicativeMethod(a=<fraction in range from 0 to 1>)
        - MidSquareMethod()

    Collision strategies:
        - NEXT
        - LINEAR (params: q)
        - SQUARE
        - CHAINING
    """

    table = HashTable(
        table_size=8,
        hash_method=DivisionMethod(),
        coll_strategy=CollStrategy.LINEAR,
        coll_params={
            "q": 3
        }
    )

    for num in [1, 89, 78, 13, 33, 14]:
        table.add_item(num)

    table.print_table()


if __name__ == "__main__":
    main()
