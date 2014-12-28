def binone(n):
    """Calculate close binary aproximation of decimal .1 where n is a number of binary floating points. This apparently has an upper limit of 56 decimal places. After that the interpreter just returns ones."""
    holding = []
    progress = 0
    for i in range(1, n+1):
        if progress + (1 / (1 << i)) < 0.1:
            holding.append('1')
            progress += (1 / (1 << i))
        else:
            holding.append('0')
    print('0.' + ''.join(holding))
