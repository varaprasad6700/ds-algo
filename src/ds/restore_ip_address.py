"""
https://leetcode.com/problems/restore-ip-addresses/
"""
from typing import List


def restore_ip_addresses(s: str) -> List[str]:
    out = []

    def valid_ip(l: List[str]) -> bool:
        return len(l) == 4 and all(0 <= int(i) <= 255 for i in l)

    def dfs(i: int, store: List[str]) -> None:
        if i == len(s):
            if valid_ip(store):
                out.append(".".join(store))
            return

        if store[-1] != "0" and int(store[-1] + s[i]) <= 255:
            temp = store[-1]
            store[-1] = store[-1] + s[i]
            dfs(i + 1, store)
            store[-1] = temp

        if len(store) < 4:
            dfs(i + 1, store + [s[i]])

    dfs(1, [s[0]])
    return out


if __name__ == '__main__':
    print(restore_ip_addresses("25525511135"))
