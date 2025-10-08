from datetime import datetime, time

class CoffeeMaker:
    def __init__(self, timer_service, recipe_service):
        self.on = True
        self.timer_service = timer_service
        self.recipe_service = recipe_service

    def make_coffee(self, recipe):
        if self.timer_service.time_resolver() == "It is off hours":
            print("Off hours, no coffee")
            return "Off hours, no coffee"
        elif self.recipe_service.return_recipe(recipe_name=recipe) == "Recipe not found":
            print("Recipe not found")
            return "Recipe not found"
        else:
            print("Enjoy your delicious coffee")
            return "Enjoy your delicious coffee"

class TimerService:
    def __init__(self, crunch_time, current_time):
        self.is_off_hours = False
        self.crunch_time = crunch_time
        self.current_time = current_time
        self.start_time = time(9,0)
        self.end_time = time(17,0)

    def change_state(self):

        if self.is_off_hours:
            print("It's on hours")
            self.is_off_hours = False
        else:
            print("It's off hours")
            self.is_off_hours = True

    def return_state(self):
        if self.crunch_time:
            self.is_off_hours = False
        print("State is:", self.is_off_hours)
        return self.is_off_hours

    def time_resolver(self):
        if self.start_time <= self.current_time <= self.end_time:
            print("It is office hours")
            return "It is office hours"
        else:
            print("It is off hours")
            return "It is off hours"

class RecipeService:
    def __init__(self):
        self.recipes = {"black": "Standard black coffee", "latte": "Latte with cow milk", "vegan-latte": "Latte with oat milk"}

    def return_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            print(self.recipes[recipe_name])
            return self.recipes[recipe_name]
        else:
            return "Recipe not found"

if __name__ == "__main__":
    crunch_time = True
    current_time = datetime.now().time()
    timer_service = TimerService(crunch_time=crunch_time, current_time=current_time)
    maker = CoffeeMaker(timer_service=timer_service)
    maker.make_coffee()