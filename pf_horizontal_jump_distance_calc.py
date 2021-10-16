# (c) Zaela Rose 2021

# This calculator is to help calculate the minimum acrobatics check required to long jump between two points in
# 1e Pathfinder

# Pathfinder is a trademark of Pazio Inc., this calculator is unofficial and is in no way associated with Pazio Inc.

# The apex of a long jump will be assumed to be a quarter of the horizontal distance from the player's starting point
# to a point at the same height vertically in the direction the player is jumping

# The height that Feather Fall mimics a fall from
FEATHER_HEIGHT = 3


def quadratic_upper(a, b, c):
    d = (b ** 2) - (4 * a * c)
    return (-b - d ** 0.5) / (2 * a)


def featherfall_calc(height_difference, distance, max_height):
    acrobatics = 5

    distance_made = False

    while not distance_made:
        # horizontal distance (x-axis coord) where the player reaches max_height - FEATHER_HEIGHT
        feather_point = quadratic_upper(-1, acrobatics, -acrobatics * (max_height - FEATHER_HEIGHT))

        if isinstance(feather_point, complex):
            acrobatics += 5
            continue

        # calculate slope at feather_point by using derivative of jump equation
        slope = 1 - feather_point / (acrobatics / 2)

        # use slope to find new linear equation that takes over the jump trajectory at the feather_point
        y_intercept = (max_height - FEATHER_HEIGHT) - slope * feather_point

        # use x = (y - b) / m = (height_difference - y_intercept) / slope to find new acrobatics check
        effective_distance = int((height_difference - y_intercept) / slope)

        if effective_distance >= distance:
            distance_made = True
        else:
            acrobatics += 5

    return acrobatics
    # round up to nearest increment of 5 and return result
    # return acrobatics if acrobatics % 5 == 0 else acrobatics + (5 - acrobatics % 5)


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
    max_height = distance / 4

    if distance < 5:
        return -3  # Error, impossible distance

    if height_difference == 0:

        if featherfall and max_height > FEATHER_HEIGHT:
            return featherfall_calc(height_difference, distance, max_height)

        # distances should always be in increments of 5 feet, though the ternary expression below was written on the
        # off chance a user enters a value not divisible by five.
        return distance if distance % 5 == 0 else distance + (5 - distance % 5)  # rounds up to nearest 5

    elif height_difference > 0:

        if height_difference >= distance:
            return -1  # Error, impossible jump

        if featherfall and max_height - height_difference > FEATHER_HEIGHT:
            return featherfall_calc(height_difference, distance, max_height)

        acrobatics = 5
        # x - x^2 / desired_distance where desired_distance is the distance in feet between the starting point and where
        # the player would land if they jumped to a space at the same height is the equation for the parabola for long
        # jumps within Pathfinder 1e. In this case desired_distance is equivalent to the acrobatics check required to
        # make the jump.
        while distance - distance ** 2 / acrobatics < height_difference:
            acrobatics += 5
        return acrobatics

    elif height_difference < 0:

        if featherfall and max_height - height_difference > FEATHER_HEIGHT:
            return featherfall_calc(height_difference, distance, max_height)

        acrobatics = 5
        while distance - distance ** 2 / acrobatics < height_difference:
            acrobatics += 5
        return acrobatics

    else:
        return -2  # Error, unknown error


def main():
    done = False
    while not done:
        h = int(input("Enter the height difference between the starting and ending points of the jump\n" +
                      "(if jumping down enter a negative number): "))
        d = int(input("Enter the horizontal distance between the starting and ending points of the jump: "))
        feather_entered = False
        while not feather_entered:
            f = input("Is Feather Fall active? (y, n) : ")
            if f in ["Y", "y", "Yes", "yes"]:
                f = True
                feather_entered = True
            elif f in ["N", "n", "No", "no"]:
                f = False
                feather_entered = True
        print("The minimum acrobatics check to make the jump is: %d" % (long_jump(h, d, f)))
        cont = input("Continue? (y, n) : ")
        if cont in ["N", "n"]:
            done = True


if __name__ == '__main__':
    main()
