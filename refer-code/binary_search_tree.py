class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return "[NODE - key: {0}, parent key: {1}]".format(self.key, self.parent.key)


class BST(object):
    def __init__(self, max_num_keys=3):
        self.root = None
        self.size = 0

    # 중위 순회 (Inorder traversal)
    def _inorder(self, node=None):
        if node is not None:
            # 왼쪽으로 순회
            self._inorder(node.left)

            # 중앙 노드 키 출력
            print(str(node.key), end=" ")

            # 오른쪽으로 순회
            self._inorder(node.right)

    def print_bst(self):
        self._inorder(self.root)
        print(": SIZE = {0}".format(self.size))

    # 노드 검색 (비재귀적 버전)
    def tree_search(self, key=None):
        if self.root is None:
            return None
        else:
            current_node = self.root
            while current_node is not None:
                if key == current_node.key:
                    return current_node

                if key < current_node.key:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

            return None

    # 노드 추가 (비재귀적 버전)
    def tree_insert(self, key=None):
        new_node = Node(key=key)

        if self.root is None:
            self.root = new_node
        else:
            # 새로운 노드를 위한 올바른 위치까지 순회하여 새로운 노드의 부모 설정
            current_node = self.root
            parent_node_for_new_node = None
            
            ################################
            # [[[[이곳에 코드 추가 (약 10줄)]]] # 
            ################################

            # 새로운 노드의 부모 노드 설정
            new_node.parent = parent_node_for_new_node

        self.size += 1

    # 노드 삭제 (비재귀적 버전)
    def tree_delete(self, key):
        node_to_be_deleted = self.tree_search(key)
        if node_to_be_deleted is None:
            return
        else:
            # node_to_be_deleted가 루트인 경우
            if node_to_be_deleted == self.root:
                self.root = self._delete_node(node_to_be_deleted)
            elif node_to_be_deleted == node_to_be_deleted.parent.left:
                node_to_be_deleted.parent.left = self._delete_node(node_to_be_deleted)
            else:
                node_to_be_deleted.parent.right = self._delete_node(node_to_be_deleted)

            self.size -= 1

    def _delete_node(self, node_to_be_deleted):
        if node_to_be_deleted.left is None and node_to_be_deleted.right is None:
            return None
        elif node_to_be_deleted.left is None and node_to_be_deleted.right is not None:
            return node_to_be_deleted.right
        elif node_to_be_deleted.left is not None and node_to_be_deleted.right is None:
            return node_to_be_deleted.left
        else:
            # 삭제할 노드의 오른쪽 자식을 smallest_node로 설정
            smallest_node = node_to_be_deleted.right

            # 처음에는 smallest_node의 부모는 삭제할 노드 자신
            parent_of_smallest_node = None

            ################################
            # [[[[이곳에 코드 추가 (약 10줄)]]] # 
            ################################

            del smallest_node

            return node_to_be_deleted


if __name__ == "__main__":
    bst = BST()

    bst.tree_insert(8)
    bst.tree_insert(3)
    bst.tree_insert(1)
    bst.tree_insert(6)
    bst.tree_insert(7)
    bst.tree_insert(10)
    bst.tree_insert(14)
    bst.tree_insert(4)

    bst.print_bst()
    print("\nSearch 10:", bst.tree_search(10))
    print("\nSearch 100:", bst.tree_search(100))

    print("\nDelete 10")
    bst.tree_delete(10)
    bst.print_bst()

    print("\nDelete 10")
    bst.tree_delete(10)
    bst.print_bst()

    print("\nDelete 3")
    bst.tree_delete(3)
    bst.print_bst()

    print("\nDelete 4")
    bst.tree_delete(4)
    bst.print_bst()

    print("\nDelete 8")
    bst.tree_delete(8)
    bst.print_bst()

