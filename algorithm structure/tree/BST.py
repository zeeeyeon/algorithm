'''
7
3 5 1 2 7 4 -5
'''

class Node:
    # left-data-rigth 구조
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        #  관리할 데이터는 최상위 루트
        self.root = None

    def insert(self, key):
        # 없다면 그냥 삽입
        if self.root is None:
            self.root = Node(key)
        else:
            # 자리를 찾아서 삽입
            self._insert(self.root, key)

    #  key는 삽입하고자 하는 데이터
    def _insert(self, node, key):
        # 찾고자하는 key가 더 작으면 왼쪽을 고려
        if key < node.key:
            if node.left is None:
                # 왼쪽에 삽입가능 => 그냥 삽입
                node.left = Node(key)
            else:
                # 왼쪽에 데이터가 있으면 => 재귀로 한번 더 탐색
                self._insert(node.left, key)
        else:
            # 오른쪽에 넣을 수 있으면 삽입
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    #  key = target, node = 현재 바라보고 있는 node
    def _search(self, node, key):
        #  탐색하고자하는 노드가 없거나, 탐색 성공하면 해당 노드 반환
        if node is None or node.key == key:
            return node
        # 작으니까 left
        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, node):
        if node:
            self._inorder_traversal(node.left)
            print(node.key, end=' ')
            self._inorder_traversal(node.right)

N = int(input())
arr = list(map(int, input().split()))

bst = BinarySearchTree()

for num in arr:
    bst.insert(num)

print("중위 순회 결과:", end=' ')
bst.inorder_traversal()  # 중위 순회: -5 1 2 3 4 5 7

# 탐색 예제
key = 5
result = bst.search(key)
if result:
    print(f"\n키 {key} 찾음.")
else:
    print(f"\n키 {key} 못 찾음.")
