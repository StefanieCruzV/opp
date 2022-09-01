import random


class Fighter:
    def __init__(self, name, origin, character_type, weapon, weight, strenght, height, speed=5):
        print("fighter construct here")
        #name,origin,type, speed, weight,strenght,height,weapon,percentage
        self.name = name
        self.origin = origin
        self.character_type = character_type
        self.weapon = weapon
        self.weight = weight
        self.strenght = strenght
        self.height = height
        self.speed = speed
        self.percentage = 0

    def attack(self, opponent):
        damage = 10
        print(f"{self.name} attaced {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage

        chance = random.randint(0, 9)
        if chance == 0:
            print(
                f"Critical hit! {self.name} attaced {opponent.name} and dealtand extra 5%%!!!")
            opponent.percentage += 5

    def status(self):
        print(
            f"Name {self.name}  origin  {self.origin}, type: {self.type}, percentage  {self.percentage}%")

    def special(self, opponent):
        damage = 15
        print(
            f"{self.name} performed a special move on {opponent.name} and dealt {damage}%!!!")
        opponent.percentage += damage


pac_man = Fighter("Pac Man", "Pac Man", "Pac Man", "mouth", 6, 6, 4, 3)
roy = Fighter("Roy", "Fire Emblem", "Human", "Sword", 5, 8, 6, 6)

# # print(roy.percentage)
# pac_man.attack(roy)
# print(roy.percentage)
