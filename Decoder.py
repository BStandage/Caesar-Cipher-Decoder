import enchant

'''function key_finder: This function accepts a single word and returns the key used
   to decrypt the word.'''
def key_finder(word):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = enchant.Dict("en_US")

    for i in range(1, 27):
        new_word = ''
        for c in word:
            if c.isalpha():
                if c.isupper():
                    new_word += upper_alpha[(upper_alpha.index(c) + i) % len(upper_alpha)]
                else:
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
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for c in word:
        if c.isalpha():
            if c.isupper():
                new_word += upper_alpha[(upper_alpha.index(c) + key) % len(upper_alpha)]
            else:
                new_word += alphabet[(alphabet.index(c) + key) % len(alphabet)]
        else:
            new_word += c
    return new_word

'''function decode_message: This function breaks a message apart into a list of 
   words that can be passed to the decode functions, then prints the decoded message'''
def decode_message(message):
    words = message.split()
    decoded_words = []
    keys = []

    for w in words:
        keys.append(key_finder(w))

    for w in words:
        # here the mode of the keys is passes to decode_key.
        # this prevents unintentional words from being printed
        decoded_words.append(decode_key(w, max(set(keys), key=keys.count)))

    print(str.join(' ', decoded_words))


if __name__ == '__main__':
    message = input('Enter the text you wish to decode: ')
    decode_message(message)