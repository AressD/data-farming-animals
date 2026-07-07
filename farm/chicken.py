from farm.animal import Animal


class Chicken(Animal):
    def __init__(self, gender):
        super().__init__()
        self.gender = gender

    def talk(self):
        if self.gender == "male":
            return "cock-a-doodle-doo"
        return "cluck cluck"