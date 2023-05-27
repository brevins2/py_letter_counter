def letter_counter():
    para = input("Enter paragraph/sentences to get count ")
    array_of_letters(para)


def array_of_letters(sentence):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    heading = f'Letter ' \
              f'Index ' \
              f'Appearance '
    print(heading)

    for letter in letters:
        if letter in sentence.lower():
            final_result = f'   {letter}' \
                           f'     {letters.index(letter) + 1}' \
                           f'       {sentence.lower().count(letter, 0, len(sentence)+1)}'
            print(final_result)


letter_counter()
