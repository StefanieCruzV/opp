from fighter import Fighter


class Samus(Fighter):
    def __init__(self):
        print("samus construct here")
        super().__init__("Samus", "Metroid", "Human", "Arm cannon", 5, 8, 8, 4)
        self.charged = False

    def special(self, opponent):
        if (self.charged):
            damage = 35
            print(
                f"{self.name} fired her arm cannot at  {opponent.name} and dealt {damage}%!!! wow ")
            opponent.percentage += damage
            self.charged = False
        else:
            self.charged = True
            print("samus is chargun up her arm canon")


class Meta_Knight(Fighter):
    def __init__(self):
        print("meta knight constructor here")
        super().__init__()


samus = Samus()
samus.status()

pac_man = Fighter("Pac Man", "Pac Man", "Pac Man", "mouth", 6, 6, 4, 3)
pac_man.special(samus)
pac_man.status()
samus.special(pac_man)
pac_man.status()
samus.special(pac_man)
pac_man.status()
