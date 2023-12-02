with open('02.txt') as f:
    data = f.read().splitlines()

r = 12
g = 13
b = 14
gameSum = 0
powerSum = 0

for line in data:
    x, y = line.split(':')
    game = int(x.split(' ')[1])
    sets = y.split(';')
    colorsCheck = 0
    rMax = gMax = bMax = 0

    for s in sets:
        colors = s.split(',')

        for c in colors:
            value, color = c[1:].split(' ')
            value = int(value)

            if color == 'red':
                if value > rMax:
                    rMax = value
                if value > r:
                    colorsCheck = 1
            elif color == 'green':
                if value > gMax:
                    gMax = value
                if value > g:
                    colorsCheck = 1
            else:
                if value > bMax:
                    bMax = value
                if value > b:
                    colorsCheck = 1
        
    if not colorsCheck:
        gameSum += game
    
    power = rMax * gMax * bMax
    powerSum += power

print('Part 1:', gameSum)
print('Part 2:', powerSum)