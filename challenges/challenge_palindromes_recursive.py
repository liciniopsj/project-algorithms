def is_palindrome_recursive(word, left_index, right_index):
    word_length = len(word)

    # palavra vazia não é palindromo
    if word_length == 0:
        return False

    # É um palíndromo
    if left_index >= right_index:
        return True
    # metades diferentes, nao é palindromo
    if word[left_index] != word[right_index]:
        return False

    # apenas char no meio, palindromo
    if left_index + 1 == right_index:
        return True

    # chamar recursivamente
    return is_palindrome_recursive(word, left_index + 1, right_index - 1)
