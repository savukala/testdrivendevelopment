class CoffeeMaker:
    def __init__(self):
        self.water = 0  # ml
        self.coffee_beans = 0  # grams
        self.is_on = False

    def add_water(self, amount):
        self.water += amount
        print(f"Added {amount}ml water. Total: {self.water}ml.")

    def add_coffee_beans(self, amount):
        self.coffee_beans += amount
        print(f"Added {amount}g coffee beans. Total: {self.coffee_beans}g.")

    def turn_on(self):
        self.is_on = True
        print("Coffee maker is now ON.")

    def turn_off(self):
        self.is_on = False
        print("Coffee maker is now OFF.")

    def brew_coffee(self, water_needed=200, beans_needed=15):
        if not self.is_on:
            print("Turn on the coffee maker first.")
            return
        if self.water < water_needed:
            print("Not enough water.")
            return
        if self.coffee_beans < beans_needed:
            print("Not enough coffee beans.")
            return
        self.water -= water_needed
        self.coffee_beans -= beans_needed
        print("Brewing coffee... Enjoy your cup!")

if __name__ == "__main__":
    maker = CoffeeMaker()
    maker.add_water(500)
    maker.add_coffee_beans(50)
    maker.turn_on()
    maker.brew_coffee()
    maker.brew_coffee()
    maker.brew_coffee()
    maker.brew_coffee()