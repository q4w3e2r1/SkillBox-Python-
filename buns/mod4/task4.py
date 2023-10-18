word = input()
possible_to_do = True
result = ""
if len(word) % 2 == 0:
    for i in word:
        if word.count(i) % 2 == 1:
            checker = False
            break
if len(word) % 2 == 1:
    countCheck = 0
    for i in word:
        if word.count(i) % 2 == 1:
            countCheck += 1
            result += i
        if countCheck > 1:
            checker = False
            break
if possible_to_do:
    for i in set(word):
        result += i * (word.count(i) // 2)
    if len(word) % 2 == 1:
        result = result[::-1] + result[1::]
    if len(word) % 2 == 0:
        result += result[::-1]
    print(result)