#Zaela
#
# Range increment calculator for shooting diagonally in Pathfinder.
# Takes two arguments, length and height, then returns the distance of the shot.
# Rounds down if remainder when divided by 5 is less than 1, otherwise rounds
# up to the nearest 5 foot increment

def diagonal_shot(length, height):
    distance = (length ** 2 + height ** 2) ** 0.5 # c = sqrt(a^2 + b^2)
    if distance % 5 >= 1:
        distance += 5 - (distance % 5)
    #else:
        #distance -= distance % 5
    return int(distance)

def main():
    done = False
    while not done:
        l = int(input("Enter length of shot: "))
        h = int(input("Enter height from where shot originated: "))
        print("The shot is: %d feet" % (diagonal_shot(l, h)))
        cont = input("Continue? (y, n) : ")
        if cont in ["N", "n"]:
            done = True

if __name__ == '__main__':
    main()
