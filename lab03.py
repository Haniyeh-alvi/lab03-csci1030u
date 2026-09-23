# Fill in the body of each function below (look for the TODO comments).
#
# The function names and their arguments are already written for you - do NOT
# rename them or change their arguments, because the automated tests call them by
# name. Replace each `pass` with your code, and use `return` to send the answer
# back (not `print`).


def pig_latin(word):
    # TODO (Part 1): return the Pig Latin form of a single lowercase word.
    #   If it starts with a vowel (a, e, i, o, u): add "way" to the end.
    #   Otherwise: move the first letter to the end and add "ay".

        if word[0] in "aeiou":
            return word + "way"
        else:
            return word[1:] + word[0] + "ay"

print(pig_latin("banana"))   # returns "ananabay"
   


def word_lengths(sentence):
    # TODO (Part 2): return a list with the length of each word in `sentence`
    #   (words are separated by spaces).
    word = sentence.split()
    lengths = []

    for word in word:
        lengths.append(len(word))
    return lengths

print(word_lengths("the quick brown fox"))    # [3, 5, 5, 3]



def reverse_words(sentence):
    # TODO (Part 3): return `sentence` with the order of its words reversed.
    #   e.g. "hello world" -> "world hello"
    
    words = sentence.split()
    words = words[::-1]
    return words

print(reverse_words("the quick brown fox"))   # fox brown quick the
   
