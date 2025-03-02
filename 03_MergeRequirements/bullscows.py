import os
import sys
import random
import argparse
import urllib.request


parser = argparse.ArgumentParser(prog=os.path.basename(
    sys.argv[0]), description="Bulls and cows game")
parser.add_argument(type=str, dest="dict_file",
                    help="Path or URL of dictionary")
parser.add_argument(type=int, default=5, dest="wordlen",
                    help="what length of words do you want to use")


def bullscows(guess: str, answer: str):
    bulls = []
    for i, guess_i in enumerate(guess):
        if guess_i == answer[i]:
            bulls.append(i)
    for i in reversed(bulls):
        guess = guess[:i] + guess[i+1:]
        answer = answer[:i] + answer[i+1:]
    cows = 0
    for g in guess:
        if g in answer:
            answer = answer.replace(g, "", 1)
            cows += 1
    return len(bulls), cows


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    answer = random.choice(words)
    i = 0
    while True:
        i += 1
        guess = ask("Введите слово: ", words)
        inform("Быки: {}, Коровы: {}", *bullscows(guess, answer))
        if guess == answer:
            return i


def ask(prompt: str, valid: list[str] = None) -> str:
    while True:
        s = input(prompt)
        if valid is not None and s not in valid:
            print("Word", s, "not in the dictionary. Try again!")
            continue
        return s


if __name__ == "__main__":
    args = parser.parse_args()
    try:
        with open(args.dict_file, "r") as f:
            data = f.read()
    except Exception as e1:
        try:
            data = urllib.request.urlopen(args.dict_file).read()
        except Exception as e2:
            print("can't open dictionary:\n", e1, "\n", e2)
            sys.exit(1)
    all_words = (p.strip() for p in data.split("\n"))
    good_words = list(filter(lambda x: len(x) == args.wordlen, all_words))
    res = gameplay(ask, print, good_words)
    print(f"You asked {res} times")
