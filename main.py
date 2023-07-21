para = input("Enter paragraph/sentences to get count \n")
consonants = []
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
alphernumeric = ['!', ',', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '=',
                 '+', '/', '\\', ']']


def letter_counter(paragraph):
    array_of_letters(paragraph)


def array_of_letters(sentence):
    letters = alphabetsfn()
    vowels = vowelsfn()
    consonantsfn(letters, vowels)

    heading = f'\tLetter ' \
              f'\t\tIndex ' \
              f'\t\t\tAppearance '
    print(heading)

    for letter in letters:
        if letter in sentence.lower():
            final_result = f'\t   {letter}' \
                           f'\t\t   {letters.index(letter) + 1}' \
                           f'\t\t\t   {sentence.lower().count(letter, 0, len(sentence) + 1)}'
            print(final_result)

    checkcase(sentence)

    checknumbers(sentence)

    checkalphernumeric(sentence)


def alphabetsfn():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    print('Alphabetical letters are: ' + str(alphabets))
    return alphabets


def vowelsfn():
    vowel = ['a', 'e', 'i', 'o', 'u']
    print('Vowels are: ' + str(vowel))
    return vowel


def consonantsfn(alphabets, vowels):
    for leta in alphabets:
        if leta not in vowels:
            consonants.append(leta)
    print('Consonants are: ' + str(consonants))


def checkcase(paragraph):
    upperCase = []
    lowerCase = []

    for letter in paragraph:
        upperLetter = paragraph.upper()
        lowerLetter = paragraph.lower()

        if letter in upperLetter and letter.isalpha():
            upperCase.append(letter)

        elif letter in lowerLetter and letter.isalpha():
            lowerCase.append(letter)

    print('Letters in upper Case: ' + str(upperCase))
    print('Letters in lower case: ' + str(lowerCase))


def checknumbers(paragraph):
    numbersFound = []

    for number in paragraph:
        if number.isdigit():
            numbersFound.append(number)

    print('numbers found are: ' + str(numbersFound))


def checkalphernumeric(paragraph):
    presentAlphanumerics = []
    for symbol in paragraph:
        if symbol.isalnum():
            presentAlphanumerics.append(symbol)

    print('alphanumerical characters: ' + str(presentAlphanumerics))


letter_counter(para)
