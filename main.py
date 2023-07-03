from chatgpt import ask_for_word
from unicodedata import normalize

def get_word():
    unformatted_word = ask_for_word()
    if unformatted_word is not None:
        word = normalize('NFKD',unformatted_word).encode('ASCII','ignore').decode('ASCII')
        return {
            'formatted': word,
            'unformatted': unformatted_word
        }
    print("Um erro no ChatGPT aconteceu!")


def show_tries(tries: int):
    if tries:
        print(f'Tentativas: {tries}')


def show_inserted_letters(inserted_letters: list):
    if inserted_letters != []:
        print('Letras já inseridas:',end=' ')

        for index,item in enumerate(inserted_letters):
            end = '\n' if index == len(inserted_letters)-1 else ', '
            print(item,end=end)


def show_guessed_letters(guessed_letters: dict):
    for index, item in guessed_letters.items():
        end = '\n' if index == len(guessed_letters) - 1 else ''
        print(item, end=end)


def game_over(word: str, tries: int):
    print(f'\nParabéns, a palavra era {word}')
    print(f'Você acertou em {tries} tentativas.')


def play_again():
    YES_NO_DICT = {
        'sim': True,
        's': True,
        'yes': True,
        'y': True,
        'nao': False,
        'n': False,
        'no': False,
        '': False
    }

    while True:
        user_input = input('Você quer jogar de novo? (sim/não): ').lower().strip()
        user_input = normalize('NFKD',user_input).encode('ASCII','ignore').decode('ASCII')

        if yes:=YES_NO_DICT.get(user_input) is None:
            print("Insira uma resposta válida")
        elif yes:
            start_game()
        else:
            break
            
    
def start_game():
    word_dict = get_word()
    if word_dict is None:
        return None

    unformatted_word = word_dict['unformatted']
    word = word_dict['formatted']
    
    tries = 0
    inserted_letters = []

    correct_guesses = 0
    guessed_letters = {i: '_' for i in range(len(word))}

    while True:
        show_tries(tries)
        show_inserted_letters(inserted_letters)
        show_guessed_letters(guessed_letters)

        guess = input('Insira uma letra: ').strip().lower()

        if (len(guess) == 1) and (guess.isalpha()) and (guess not in inserted_letters):
            for index,item in enumerate(word):
                if guess == item:
                    guessed_letters[index] = item
                    correct_guesses += 1
                
            tries += 1
            inserted_letters.append(guess)

            if correct_guesses == len(word):
                break
        elif len(guess) != 1 or not guess.isalpha():
            print('Insira apenas letras!')
        elif guess in inserted_letters:
            print('Letra já inserida!')
        
    game_over(unformatted_word,tries)
    play_again()

start_game()