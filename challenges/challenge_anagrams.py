def sort_string(string):
    character_table = {
        "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6,
        "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
        "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
        "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25,
    }
    character_count = [0] * 26
    sorted_string = ''
    for char in string:
        character_count[character_table[char]] += 1
    for index in range(26):
        sorted_string += chr(index + 97) * character_count[index]
    return sorted_string


def is_anagram(first_string, second_string):
    if first_string == '' and second_string == '':
        return (first_string, second_string, False)

    sorted_first_string = sort_string(first_string.lower())
    sorted_second_string = sort_string(second_string.lower())

    if sorted_first_string == sorted_second_string:
        return (sorted_first_string, sorted_second_string, True)

    return (sorted_first_string, sorted_second_string, False)
