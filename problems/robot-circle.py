
# A robot can accept 3 types of commands - G (go forward), L (turn left on the spot), R (turn right on the spot). A robot accepts a finite list of commands, and loops those commands indefinitely.

# An example command would be "LGL", it will turn left on the spot, go forward one step, then turn left again. Then it will turn left again, go forward one step, and turn left, ad naseum.

# Given a list of commands, write a function to determine if the robot will ever return to its starting position.

def calc(position, direction, commands):

    x,y = position
    d = direction

    for i in commands:
        print(x,y,d)
        if i == 'G':
            if d == 'N':
                y += 1
            elif d == 'E':
                x += 1
            elif d == 'S':
                y -= 1
            elif d == 'W':
                x -= 1
        if i =='L':
            if d == 'N':
                d = 'W'
            elif d == 'E':
                d = 'N'
            elif d == 'S':
                d = 'E'
            elif d == 'W':
                d = 'S'
        if i == 'R':
            if d == 'N':
                d = 'E'
            elif d == 'E':
                d = 'S'
            elif d == 'S':
                d = 'W'
            elif d == 'W':
                d = 'N'

    return (x,y)

def doesCircleExist(commands):

    final_position = calc((0,0), 'N', commands * 4)

    return final_position == (0,0)

print(doesCircleExist('LGRGRGLGRGRGLGRGRGLGRGRG'))