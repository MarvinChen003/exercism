# ToDo - Plan to finish it by May

letter_value = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"],
}


def score(word):
    score = []
    for letter in word.upper():
        for value_item in letter_value:
            if letter in letter_value[value_item]:
                score.append(value_item)
    return sum(score)

