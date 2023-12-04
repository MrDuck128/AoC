with open('04.txt') as f:
    data = f.read().splitlines()

total = 0
sCards = [1] * len(data)
for i, line in enumerate(data):
    _, numbers = line.split(':')

    winning, guess = numbers.split('|')
    winning = set(winning.split())
    guess = set(guess.split())

    correct = len(guess.intersection(winning))
    total += 2**(correct-1) if correct > 0 else 0

    for j in range(correct):
        sCards[i+1+j] += sCards[i]

print('Part 1:', total)
print('Part 2:', sum(sCards))