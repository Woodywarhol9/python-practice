from typing import Optional, Generic, TypeVar

T = TypeVar("T")  # item에 대한 TypeVar


class Node(Generic[T]):
    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer
        
        
class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None

    @property
    def length(self) -> int:
        if self.head is None:
            return 0
        cur_node = self.head
        count: int = 1
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            count += 1
        return count

    def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result
        cur_node = self.head
        result += f"{cur_node.item}"
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
            result += f", {cur_node.item}"
        return result

# Stack을 상속 대신 composition 하여 push만 가져오는 방법도 가능.


class Queue(Generic[T], LinkedList[T]):
    def enqueue(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.pointer is not None:
            cur_node = cur_node.pointer
        cur_node.pointer = new_node

    def dequeue(self) -> T:
        if self.head is None:
            raise ValueError("queue is empty")
        cur_node = self.head
        if cur_node.pointer is None:
            self.head = None
            return cur_node.item
        result = cur_node.item
        self.head = cur_node.pointer
        return result


if __name__ == "__main__":
    queue = Queue[int]()
    queue.enqueue(12)
    queue.enqueue(1)
    queue.enqueue(13)
    queue.enqueue(16)

    queue.dequeue()
    print(queue.length)
    print(queue)
