from nltk.corpus import words
from numpy.random import randint
from playsound import playsound


def pick_word():
    words_list = words.words()
    list_length = int(len(words_list))
    word_index = int(randint(0,list_length,1))
    picked_word = words_list[word_index]
    return picked_word

def main():
    word_length = 0
    
    while word_length<10:
        word = pick_word()
        word_length = len(word)
    
    
    vowels = ['a','e','i','o','u']
    original_word = word
    new_word = original_word
    for i in range(0,4):
        new_word = new_word.replace(vowels[i],'_')
        
    print(new_word)
           
    i=1
    while i<=3:
        user_input = input('Guess the Word: ')
        if user_input == original_word:
            print('Correct')
            playsound('E:\\Python Practice\\correct answer.mp3')
        else:
            print('Incorrect')
            playsound('E:\\Python Practice\\wrong answer.mp3')
        i=i+1
        
    print('Correct Word:'+ original_word)
    
main()
replay = 'Yes'
while replay=='Yes':
    replay = input('Play Again? (yes/no): ')
    main()

