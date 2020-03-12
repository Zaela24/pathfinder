# Zaela
#
# Class to store HP and DR values for enemies
# can subtract with either int to bypass DR, or a list with strings including
# DR type after damage to check if it bypasses DR or not (if damage type doesn't
# bypass damage, then it applies damage reduction before reducing HP)

class Monster:
    def __init__(self, hp, dr=0, dr_type=None):
        self.hp = hp
        self.dr = dr
        self.dr_type = dr_type
        if self.dr_type != None:
            if isinstance(dr_type, str):
                self.dr_type = self.dr_type.lower()
            else:
                for i in range(0, len(self.dr_type)):
                    self.dr_type[i] = self.dr_type[i].lower()

    def __sub__(self, rhs):
        if isinstance(rhs, int):
            self.hp -= rhs
            print(self.hp)
            return
        else:
            dr_pass = False
            for i in range(1, len(rhs)):
                if rhs[i].lower() in self.dr_type:
                    dr_pass = True
                    break
            if dr_pass == True:
                self.hp -= rhs[0]
            else:
                self.hp -= (rhs[0] - self.dr)
            print(self.hp)


