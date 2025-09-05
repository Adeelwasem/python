word = input("Enter a word: ")
myletter = input("Enter a letter: ")

for letter in word:

    if (letter == myletter):

        print (myletter , "is found")
        break

    else: 

        print (myletter , "is not found") 

