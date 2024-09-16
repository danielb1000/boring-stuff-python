import random
import logging
from pathlib import Path

here = Path(__file__).resolve().parent

logging.basicConfig(filename=f'{here}\coin_toss_corrected.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.info(f"USER FIRST GUESSED: {guess}")
logging.info(f"ALLOWED FIRST GUESS: {guess}")

toss = random.choice(["heads", "tails"]) 
logging.info(f"FIRST TOSS: {toss}")

if toss == guess:
    print('You got it!')
    logging.info(f"CORRECT GUESS: USER: {guess} TOSS: {toss}")

else:
    print('Nope! Guess again!')
    logging.info(f"WRONG GUESS: USER: {guess} TOSS: {toss}")

    guess = input()
    logging.info(f"USER 2nd GUESS: {guess}")

    if toss == guess:
        print('You got it!')
        logging.info(f"CORRECT GUESS: USER: {guess} TOSS: {toss}")
    else:
        print('Nope. You are really bad at this game.')
        logging.info(f"USER 2nd GUESS:{guess} TOSS: {toss}")