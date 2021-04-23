#Ceaser's Cypher Code Project
import re

alphabet = "abcdefghijklmnopqrstuvwxynz"

choice = input("Do you want to decode a message, or encrypt one? ")

if choice == "encrypt":

    sentence = input("Write what you want to encrypt here: ").lower()
    final_word = []
    #changed_letters = []
    #first_char = ""

    #first_index = sentence.find(first_char, 0)

    characters = len(sentence)

    #test = []

    start = 2

    #for i in range(len(sentence)):
        #if sentence[i] == sentence[start]:
            #if i == start:
                #test.append(alphabet[alphabet.index(sentence[i]) - 3])
            #else:
                #test.append(sentence[i])
        #else:
            #test.append(sentence[i])

    breaker = False
    point_of_no_return = False

    #The for loop is used to go through all of the indexes of the sentence that the user writes without turning it into a list.
        #If the sentence is turned into a list, then all of the characters in the sentence that are the same (i.e the same letters) will all count as the same index, thus ruining the encryption.
    for repetitions in range(len(sentence)):
        #The if statement is then used to see which of the letters in the sentence that the user inputs is equal to the index that we have to change the letter for.
        if sentence[repetitions] == sentence[start] and repetitions == start:
            #Once the two indexes are matched, then we append the character to the "final_word" list.
                #We then increase the index by 3 as that is the cypher's rule.
            if sentence[repetitions] == sentence[start] and sentence[repetitions] == " ":
                final_word.append(sentence[repetitions])
            else:
                final_word.append(alphabet[alphabet.index(sentence[repetitions]) - 3])

            if sentence[repetitions] == sentence[len(sentence) - 2]:
                point_of_no_return = True

            start += 3

            #used for test purposes
            #print(final_word)
            #print((characters // 3), characters)

            #The if statement is created to make sure to break the loop so as to not get a TyperError where the index is outside of the range of the string.
                #To do this, the Boolean variable "breaker" is set to true so as to check it's status with a variable at the end of the each cycle.
            if ((characters // 3) == 1) and (characters == 3):
                breaker = True

        else:
            final_word.append(sentence[repetitions])
        #The reason that there are two if statements each used to break the for loop, is because of the following reasons.
            #The first if statement is used to stop the loop when the counter is on the last character that it has to add to the list, and there are only 2 other characters left to the sentence.
            #The reason that it will state 3 is because the diminuation to the number of characters is at the end of the loop, therefore it counts the character that it's adding as well.
                #Meaning without it, there would be a "index out of range" error.
        if ((characters // 3) == 1) and (characters == 3) and breaker == True:
            final_word.append(sentence[len(sentence) - 2])
            final_word.append(sentence[len(sentence) - 1])
            break

        #This if statement is the easiest to understand as it breaks the loop when the number in the characters variable can't be divided by 3 anymore (not giving an integer which isn't 0).
        elif (characters // 3) == 0:
            if characters == 2 and point_of_no_return == False:
                final_word.append(alphabet[alphabet.index(sentence[len(sentence) - 1]) - 3])
            elif characters == 2 and point_of_no_return == True:
                final_word.append(sentence[len(sentence) - 1])

            break

        characters -= 1
        #print(characters)

    print("Your encoded sentence is:", "".join(final_word))

elif choice == "decrpyt":
    #decrypt
    decypher = 2
    unscrambled_word = []

    word_to_decrypt = input("Insert the sentence that you want to decrypt: ")

    indexes = len(word_to_decrypt)

    for i in range(len(word_to_decrypt)):
        if word_to_decrypt[i] == word_to_decrypt[decypher] and i == decypher:
            if word_to_decrypt[i] != " ":
                unscrambled_word.append(alphabet[alphabet.index(word_to_decrypt[decypher]) + 3])

            else:
                unscrambled_word.append(word_to_decrypt[i])

            decypher += 3

        else:
            unscrambled_word.append(word_to_decrypt[i])

        indexes -= 1
        print(indexes // 3, indexes, unscrambled_word)

        if indexes // 3 == 0 and indexes == 2:
            unscrambled_word.append(word_to_decrypt[len(word_to_decrypt) - 2])
            unscrambled_word.append(word_to_decrypt[len(word_to_decrypt) - 1])
            break

    print("".join(unscrambled_word))
