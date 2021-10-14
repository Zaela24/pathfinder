# Zaela
#
# Calculates time and DC for crafting magical items in Pathfinder
# assumes all pre-requisits are met by the crafter and none are needed from the
# co-op crafter

import random


def craft_magical_calc(craft_gp, casterlvl_of_item, co_op=False, days_co_op=0):
    dc = casterlvl_of_item + 5
    if co_op:  # co-op crafting adds a +2 circumstance bonus to the roll
        dc -= 2  # I took that off the DC instead
    days = craft_gp // 1000
    if craft_gp % 1000 >= 50:  # if more than 50 gp left after dividing by 1000 gp
        days += 1  # then add another day
    if co_op:
        half_days = days / 2
        if half_days % 2 != 0:  # rounds up
            half_days += 1
        half_days = int(half_days)
        days -= days_co_op
        if days < half_days:  # checks to make sure assisting doesn't lower days
            days = half_days  # to less than half of the original time
    return [days, dc]


def main():
    done = False
    while not done:
        price = int(input("Enter crafting price of item in gp: "))
        cl = int(input("Enter caster level of item: "))
        co_op = input("Co-op crafting? (y, n) : ")
        if co_op in ["Y", "y"]:
            days_coop = int(input("Enter number of days assisting: "))
            out = craft_magical_calc(price, cl, True, days_coop)
        else:
            out = craft_magical_calc(price, cl)
        print("%d days, DC = %d" % (out[0], out[1]))
        cont = input("Continue? (y, n) : ")
        if cont in ["N", "n"]:
            done = True


if __name__ == "__main__":
    main()
