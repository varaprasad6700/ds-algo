"""
https://leetcode.com/problems/unique-morse-code-words/
"""
from typing import List


def unique_morse_representations(words: List[str]) -> int:
    morse_codes = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    s = set()
    for i in words:
        temp = []
        for j in i:
            temp.append(morse_codes[ord(j) - ord('a')])
        s.add("".join(temp))
    return len(s)


if __name__ == '__main__':
    print(unique_morse_representations(["gin", "zen", "gig", "msg"]))
