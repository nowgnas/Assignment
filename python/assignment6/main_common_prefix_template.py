# FIND LONGEST COMMON PREFIX

from collections import defaultdict


class Node:
    def __init__(self, char):
        self.char = char
        self.is_leaf = False  # 끝에 위치하는 지 여부
        self.children = defaultdict(Node)


class Trie:
    def __init__(self, arr):
        self.root = Node("")
        self.construct(arr)

    # Construct trie
    def construct(self, arr):
        print(f'arr string :{arr}')
        for i in range(len(arr)):
            self.insert(arr[i])
            print(f'word: {arr[i]}')
            print('----------------')

    def insert(self, key):
        print(f'key: {key}')
        node = self.root
        print(f'node : {node.char} is empty??')
        for char in key:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]  # 다음 노드로 이동
        print(f'node out :{node.char}')
        node.is_leaf = True

    # Perform walk on trie and return longest common prefix
    def find_common_prefix(self):
        node = self.root
        prefix = ""
        print(node.children)
        print(node.children[0])

        return prefix


# Function that returns longest common prefix
def solution(arr):
    trie = Trie(arr)
    answer = trie.find_common_prefix()
    return answer


if __name__ == '__main__':
    arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
    print(solution(arr))
