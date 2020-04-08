# Zaela

# This class will likely be extended by classes for specific spellcasting
# Pathfinder classes.

# Note: if multiclassing put each class and their corresponding level in a list
# Begin the level list with the cummulative character level, then each level
# in the corresponding order with your class list. The length of the level list
# will be one greater than the length of the class list if you're multiclassing
# and following these directions.

# Examples:
#    No multiclassing:
#        Sarah = Heroes("Sarah", "Ranger", "Elf", 1, 10)
#
#    With multiclassing:
#        class_lst = ["Fighter", "Alchemist"]
#        lvl_lst = [12, 8, 4]
#        Tim = Heroes("Tim", class_lst, "Ratfolk", lvl_lst, 67)

import Heroes

class Spellcaster(Heroes.Heroes):
    def __init__(self, name, pf_class, race, lvl, hp):
        super().__init__(name, pf_class, race, lvl, hp)
        self.spell_stats = self.update_spell_stats()

    def update_spell_stats(self):#requests user input to get stats per spell lvl
    #Considering replacing this and automatically calculating these values for
    # the user if they enter the character's Str/Dex/Con/Int/Wis/Cha scores
        spell_stats = dict()
        for i in range(0, 10): # for 0th-9th level spells
            print("For %d level spells:" % (i))
            spells_per_day = int(input("Enter spells per day: "))
            spell_dc = int(input("Enter spell DC: "))
            bonus_spells = int(input("Enter number of bonus spells: "))
            spell_stats.update({
            "Level " + str(i) + " Spells Per Day" : spells_per_day,
            "Level " + str(i) + " Spell DC" : spell_dc,
            "Level " + str(i) + " Bonus Spells" : bonus_spells
            })
            cont = input("Continue to next spell level (y / n): ").lower()
            if cont == 'n':
                break # if done entering info for all needed lvls, breaks early
        return spell_stats

    # I'm considering adding a database to keep track of the actual spells
