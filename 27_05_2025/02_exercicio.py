def palindrome_verif(word: str) -> bool:
  word = word.lower().replace(" ", "")  # Ignora espaços e coloca em minúsculas
  return word == word[::-1]

print(palindrome_verif('ovo'))
print(palindrome_verif('Giovanny'))