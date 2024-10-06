# Acronyms Creator

# This project creates an acronym from the input
# string. An acronym is a short form of a word. For
# example, CN is an acronym for Coding Ninjas.

def create_acronym(phrase):
   acronym = ""
   words = phrase.split()
   for word in words:
      acronym += word[0].upper()
   return acronym

input_phrase = "Python is Amazing"
result = create_acronym(input_phrase)
print(result) 