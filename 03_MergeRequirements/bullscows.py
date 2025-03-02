import random


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
    
        
