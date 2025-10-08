from datetime import datetime, time, timedelta


class CoffeeMaker:
    def __init__(self, timer_service, recipe_service):
        self.timer_service = timer_service
        self.recipe_service = recipe_service

    def make_coffee(self, recipe):
        if self.timer_service.off_hours_resolver():
            print("Off hours, no coffee")
            return "Off hours, no coffee"
        elif self.recipe_service.return_recipe(recipe) == "Recipe not found":
            print("Recipe not found")
            return "Recipe not found"
        else:
            print("Enjoy your delicious coffee", self.recipe_service.return_recipe(recipe))
            return "Enjoy your delicious coffee"

class TimerService:
    def __init__(self, is_off_hours, current_time, crunch_time):
        self.is_off_hours = is_off_hours
        self.current_time = current_time
        self.start_time = time(9,0)
        self.end_time = time(17,0)
        self.crunch_time = crunch_time


    def off_hours_resolver(self):
        if self.crunch_time:
            return False
        if self.start_time <= self.current_time <= self.end_time:
            return False
        else:
            return True

class RecipeService:
    def __init__(self):
        self.recipes = {"black": "Standard black coffee", "latte": "Latte with cow milk", "vegan-latte": "Latte with oat milk"}

    def return_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            return "Recipe not found"


if __name__ == "__main__":
    is_off_hours = True
    current_time = datetime.now().time()
    crunch_time = False
    recipe_service = RecipeService()
    timer_service = TimerService(is_off_hours, current_time, crunch_time)
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    recipe = "black"
    maker.make_coffee(recipe)
    recipe = "latte"
    maker.make_coffee(recipe)
    recipe = "vegan-latte"
    maker.make_coffee(recipe)
    recipe = "macchiato"
    maker.make_coffee(recipe)