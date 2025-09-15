def solution(s):
    words = sorted(s, reverse = True)
    return ''.join(words)