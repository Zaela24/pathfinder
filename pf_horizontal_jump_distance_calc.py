# (c) Zaela Rose 2021

# This calculator is to help calculate the minimum acrobatics check required to jump between two points in 1e Pathfinder

# Pathfinder is a trademark of Pazio Inc., this calculator is unofficial and is in no way associated with Pazio Inc.

# There is an assumption that the player has a falling speed of 500 ft per round without featherfall when over 10 feet
# of vertical distance downwards is covered

# The featherfall spell indicates that falling speeds are reduced to 60 ft per round, which will be assumed to be the
# same speed when players are falling a vertical distance of less than 10 feet.

# The apex of a long jump will be assumed to be a quarter of the horizontal distance from the player's starting point
# to a point at the same height vertically in the direction the player is jumping

MIN_FALLING_SPEED = 60
MAX_FALLING_SPEED = 500

FEATHER_HEIGHT = 3

def quadratic_upper(a, b, c):
    d = (b ** 2) - (4 * a * c)
    return (-b - d ** 0.5) / (2 * a)

def long_jump(height_difference, distance, featherfall):
    """
    Takes an int indicating the difference in height between the starting and ending points of the jump. If the ending
    height is below the starting point, the number will be negative. If the desired ending point is above the starting
    point the number will be positive. Also takes an int indicating the horizontal distance between the two points, and
    a bool indicating whether or not the player is affected by featherfalling.
    Returns an int indicating the minimum acrobatics check required in order to make the jump. Returns -1 if the jump
    is impossible (for example, if a player tries to long jump when they need to vertical jump).

    Both height_difference and distance should be increments of 5 feet,
    though values not divisible by 5 are accounted for just in case a user enters a non-complying number.

    :param height_difference: int
    :param distance: int
    :param featherfall: bool
    :return: int
    """
    if height_difference == 0:

        max_height = distance / 4

        if featherfall and max_height > FEATHER_HEIGHT:
            # horizontal distance (x-axis coord) where the player reaches max_height - FEATHER_HEIGHT
            feather_point = quadratic_upper(-1, distance, -distance * (max_height - FEATHER_HEIGHT))

            # calculate slope at feather_point by using derivative of jump equation
            slope = 1 - feather_point / (distance / 2)


        # distances should always be in increments of 5 feet, though the ternary expression below was written on the
        # off chance a user enters a value not divisible by five.
        return distance if distance % 5 == 0 else distance + (5 - distance % 5)  # rounds up to nearest 5

    elif height_difference > 0:

        if height_difference >= distance:
            return -1  # impossible jump

        #if featherfall:
            # calc

        acrobatics = 5
        # x - x^2 / desired_distance where desired_distance is the distance in feet between the starting point and where
        # the player would land if they jumped to a space at the same height is the equation for the parabola for long
        # jumps within Pathfinder 1e. In this case desired_distance is equivalent to the acrobatics check required to
        # make the jump.
        while distance - distance ** 2 / acrobatics < height_difference:
            acrobatics += 5
        return acrobatics

    elif height_difference < 0:

        #if featherfall:
            # calc

        acrobatics = 5
        while distance - distance ** 2 / acrobatics < height_difference:
            acrobatics += 5
        return acrobatics




    else:
        return -2

print(long_jump(0, 20, True))