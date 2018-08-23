import enchant

'''Disclaimer: Still in a rough draft state. Will be condensed and modified greatly
               Punctuation not yet accepted.'''


'''function decode: This function accepts a single word and returns the key used
   to decrypt the word.'''
def decode(word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict = enchant.Dict("en_US")

    for i in range(1, 27):
        new_word = ''
        for c in word:
            new_word += alphabet[(alphabet.index(c) + i) % len(alphabet)]
        if dict.check(new_word):
            return i
            break
    if i == 26:
        print("No results")


'''function deocde_key: This function decodes an Caesar encrypted word when the key is known'''
def decode_key(word, key):
    new_word = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for c in word:
        new_word += alphabet[(alphabet.index(c) + key) % len(alphabet)]
    return new_word

'''function decode_message: This function breaks a message apart into words that can be
   passed to the decode functions'''
def decode_message(message):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dict = enchant.Dict("en_US")
    words = message.split()
    decoded_words = []
    keys = []


    
    for w in words:
        keys.append(decode(w))

    for w in words:
        decoded_words.append(decode_key(w, max(set(keys), key=keys.count)))

    print(words)
    print(decoded_words)


if __name__ == '__main__':
    message = input('Enter the text you wish to decode: ')
    decode_message(message)