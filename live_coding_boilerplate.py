
class CoffeeMaker:
    def __init__(self):
        self.is_off_hours = False

    def make_coffee(self):
        print("Enjoy your delicious coffee")
        return "Enjoy your delicious coffee"

if __name__ == "__main__":
    maker = CoffeeMaker()
    maker.make_coffee()