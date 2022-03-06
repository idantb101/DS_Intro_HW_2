

from operator import index


def reverse(sentence, reverse_word):
    words = sentence.split()
    if isinstance(reverse_word, str) == False:
        return'invalid input'
    if (reverse_word  not in words):
        return'The word was not found'
    for index,word in enumerate(words):
        if (word == reverse_word):
           words[index] = word[::-1]
           break
    return(" ".join(words)) 

print(reverse("I like apples and I also like bananas", "like"))
#"I ekil apples and I also like bananas". 
print(reverse("I like apples and I also like bananas", "oranges"))
#no match
print(reverse("I like apples and I also like bananas", "Bananas"))
#no match 
print(reverse("I like apples and I also like bananas", 3))
#invalid