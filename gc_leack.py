import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 노드를 생성하고 연결 리스트를 형성합니다.
def create_linked_list():
    head = Node(1)
    current = head
    for i in range(2, 100):
        new_node = Node(i)
        current.next = new_node
        current = new_node
    # 연결 리스트의 끝을 처음 노드로 연결하여 사이클을 형성합니다.
    current.next = head
    return head

def main():
    linked_list = create_linked_list()
    # 연결 리스트를 출력합니다. 이 작업은 사이클을 통해 모든 노드에 대한 참조를 유지합니다.
    current = linked_list
    while current is not None:
        print(current.value)
        current = current.next

    # GC를 수동으로 호출하여 메모리 정리를 시도합니다.
    gc.collect()

    # 여전히 사이클을 통해 연결 리스트에 대한 참조가 남아있으므로 메모리 누수가 발생합니다.
    # GC 모듈은 이러한 종류의 누수를 해결할 수 없습니다.
    # 참조 사이클을 끊거나 다른 메모리 관리 기법을 사용해야 합니다.

if __name__ == '__main__':
    main()
