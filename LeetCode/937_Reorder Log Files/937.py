from typing import List

def a(logs: List[str]):
    letters, digits = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits



logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

print(a(logs))

# a(logs)