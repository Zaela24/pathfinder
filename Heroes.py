# Zaela

# Abstract class for creating playable characters; will be extended by classes
# for spellcasters and non-spellcasters, then likely further by character class.

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

class Heroes:
    def __init__(self, name, pf_class, race, lvl, hp):
        """Enter class(es), race, level(s), and hp

        If multiple classes, enter total character lvl
        followed by each class lvl in order"""
        self.name = name
        self.pf_class = pf_class

        if isinstance(self.pf_class, list):  # in case of multiclassing
            for i in self.pf_class:
                self.pf_class = self.pf_class[i].lower()
        else:
            self.pf_class = self.pf_class.lower()

        self.race = race.lower()
        self.level = lvl
        self.hp = hp
        self.class_lvl_dict = self.make_cl_dict()

    def make_cl_dict(self):
        cl_dict = dict()
        if isinstance(self.level, list):  # If multi-multiclassing/has >1 lvls
            cl_dict.update({"character": self.level[0]})  # adds character level
            for i in self.pf_class:
                cl_dict.update({self.pf_class[i]: self.level[i + 1]})
                # i+1 used since level[0] has the cumulative level
        else:
            cl_dict.update({self.pf_class: self.level})
        return cl_dict
