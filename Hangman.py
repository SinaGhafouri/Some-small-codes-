correct_list = []
wrong_list = []
def main(name1):
    name = name1.lower()
    heart = 5
    x = 0
    print('The word has {} letters.\nYou have 5 hearts.'.format(len(name)))
    while True:
        guess1 = input('\nGuess with one letter: ')
        guess = guess1.lower()
        if guess == '':
            print('Print something!')
            continue
        elif len(guess) != 1:
            print('Enter one letter!')
            continue
        elif ord(guess) not in range(ord('a'), ord('z')+1):
            print('Enter a letter!')
            continue
        elif guess in name:
            z = name.count(guess)
            if guess in correct_list:
                print('You\'ve already guessed that correctly!')
                continue
            elif guess not in correct_list:
                print('Correct! Way to go :)')
                correct_list.append(guess)
                x += z
                for _ in name:
                    if _ in correct_list:
                        print(_,end=' ')
                    else:
                        print('_',end=' ')
        elif guess not in name:
            if guess in wrong_list:
                print('You\'ve already guessed that, and it was wrong!')
                continue
            elif guess not in wrong_list:
                heart -= 1
                wrong_list.append(guess)
                if heart > 0:
                    print('Wrong! You have {} heart left.'.format(heart))
        if heart == 0:
            print('Wrong! You lost!')
            break
        if x == len(name):
            print('\nYou won!')
            break
if __name__=='__main__':main('Terena')
