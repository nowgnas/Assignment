# TEST BINARY SEARCH TREE (BST)

from enum import Enum
from bst import BinarySearchTree

MENU = Enum('MENU',
            ['Insert', 'Delete', 'Search', 'Print_in_order', 'Key_range', 'Exit'])


def select_menu() -> MENU:
    s = [f'({m.value}){m.name}' for m in MENU]
    while True:
        print(*s, sep='  ', end='')
        n = int(input(': '))
        if 1 <= n <= len(MENU):
            return MENU(n)


if __name__ == "__main__":
    tree = BinarySearchTree()

    while True:
        menu = select_menu()

        if menu == MENU.Insert:
            key = int(input('Type key: '))
            val = input('Type value: ')
            if not tree.add(key, val):
                print('Failed to insert')

        elif menu == MENU.Delete:
            key = int(input('Type key: '))
            tree.remove(key)

        elif menu == MENU.Search:
            key = int(input('Type key: '))
            t = tree.search(key)
            if t is not None:
                print(f'The value is {t}.')
            else:
                print('Not found.')

        elif menu == MENU.Print_in_order:
            tree.print_in_order()

        elif menu == MENU.Key_range:
            print(f'The minimum key is {tree.min_key()}.')
            print(f'The maximum key is {tree.max_key()}.')

        else:  # Exit
            break
