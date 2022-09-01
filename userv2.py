
class User:
    def __init__(self, first_name, last_name, email, age):
        self.firs_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        if (self.is_rewards_member == False):
            regards = "you still have no rewards"
        else:
            regards = "You are Member"
        print(f"The name is: {self.firs_name} \nThe Last Name is :  {self.last_name} \nemail:{self.email} \nage : {self.age}  ")
        print(f"Rewards: {regards} \nCard points: {self.gold_card_points} ")
        return self

    def enroll(self):
        if (self.is_rewards_member == True):
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            # print(self.is_rewards_member,self.gold_card_points)
            print("Now you are a member")
        return self
         

    def spend_points(self, amount):
        if (self.gold_card_points <= 40):
            print("you have  less than 40 points")
        if (self.gold_card_points < amount):
            print("you don't have enough points")
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(f"Your Card points now : {self.gold_card_points}")
        return self
        


alo = User("Stefanie", "Alondra", "alo@gmail", 25)

marian = User("Marian", "Terens", "marian@gmail", 33)
alain = User("Alan", "Monterey", "alan@gmail", 55)


alain.display_info().enroll().spend_points(30).display_info()
