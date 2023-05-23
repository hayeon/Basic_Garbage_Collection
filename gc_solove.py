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
    # 마지막 노드의 next 참조를 None으로 설정하여 사이클을 방지합니다.
    current.next = None
    return head

def main():
    linked_list = create_linked_list()
    # 연결 리스트를 출력합니다.
    current = linked_list
    while current is not None:
        print(current.value)
        current = current.next

    # GC를 수동으로 호출하여 메모리 정리를 시도합니다.
    gc.collect()

if __name__ == '__main__':
    main()
