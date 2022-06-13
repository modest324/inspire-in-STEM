#checking if a word is a palindrome

word_str = "eye"
word_str = word_str.casefold()
rev_word = reversed(word_str)


if list(word_str) == list(rev_word):
    print("word is a palindrome")
else:
    print("word is not a palindrome")     
