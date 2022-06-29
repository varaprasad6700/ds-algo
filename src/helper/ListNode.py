from typing import List


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return ListNode.get_list(self).__str__()

    @staticmethod
    def get_list(ll) -> List[int]:
        out = []
        while ll is not None:
            out.append(ll.val)
            ll = ll.next
        return out

    @classmethod
    def list_node_from_list(cls, l: List[int]):
        if len(l) == 0:
            return None
        else:
            head = cls(l[0])
            curr = head
            for i in range(1, len(l)):
                curr.next = cls(l[i])
                curr = curr.next
            return head
