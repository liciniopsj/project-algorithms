def is_palindrome_iterative(word):
    word_length = len(word)
    # vazio, não pode ser palíndromo
    if word_length == 0:
        return False
    # Verificar a palavra em pares, comparando a primeira metade com a segunda metade
    # Se os caracteres em cada metade forem diferentes, não é um palíndromo
    for index in range(word_length // 2):
        
        if word[index] != word[word_length - index - 1]:
            return False
    return True
