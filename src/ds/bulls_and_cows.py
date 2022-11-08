"""
https://leetcode.com/problems/bulls-and-cows/
"""


def bulls_and_cows(secret: str, guess: str) -> str:
    secret_dict = {}
    guess_dict = {}
    bull = 0
    cow = 0
    for i, j in zip(secret, guess):
        if i == j:
            bull += 1
        secret_dict[i] = secret_dict.get(i, 0) + 1
        guess_dict[j] = guess_dict.get(j, 0) + 1
    for i in secret_dict:
        cow += min(secret_dict[i], guess_dict.get(i, 0))
    cow -= bull
    return "{}A{}B".format(bull, cow)


if __name__ == '__main__':
    print(bulls_and_cows("1807", "7810"))
