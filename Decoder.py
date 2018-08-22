import enchant

def decode(word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict = enchant.Dict("en_US")

    for i in range(1, 27):
        new_word = ''
        for c in word:
            new_word += alphabet[(alphabet.index(c) + i) % len(alphabet)]
        if dict.check(new_word):
            print('Your decrypted word is: ' + new_word)
            break
    if i == 26:
        print("No results")


if __name__ == '__main__':
    word = input('Enter the text you wish to decode: ')
    decode(word)