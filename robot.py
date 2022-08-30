class Robot:
    def __init__(self, name, make, weight, height, strenght, intelligence):
        # battery level, name, make, weight, height, strenght, intelligence
        print("this is the init function running")
        self.name = name
        self.make = make
        self.weight =weight
        self.height = height
        self.strenght =strenght
        self.intelligence = intelligence
        self.batery_level = 100

    def run_comand (self,command):
        if (self.batery_level < 5):
            print(f"{self.name} is a lottle tires, recharge")
        else:
            print(f"{self.name} is now running the {command} command")
            self.batery_level -= 5

bob= Robot("Bob","Mercedes",3000,7,5,3)
# hal= Robot("Hal","supercomputer",5000,100,3,100)


# print(bob.name)
# print(bob.strenght)
print(bob.batery_level)
bob.run_comand("drive")

# print(hal.name)
# print(hal.strenght)
# print(hal.batery_level)