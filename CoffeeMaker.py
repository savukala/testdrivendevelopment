from datetime import datetime, time

class CoffeeMaker:
    def __init__(self, timer_service, recipe_service):
        self.timer_service = timer_service
        self.recipe_service = recipe_service

    def make_coffee(self, recipe):
        if self.timer_service.is_off_hours:
            print("No coffee during off hours")
            return "No coffee during off hours"
        elif self.recipe_service.return_recipe(recipe) == "Recipe not found":
            print("Recipe not found for", recipe)
            return "Recipe not found"
        else:
            print("Enjoy your delicious", self.recipe_service.return_recipe(recipe))
            return "Enjoy your delicious coffee"

class TimerService:
    def __init__(self, is_off_hours, current_time, crunch_time):
        self.is_off_hours = is_off_hours
        self.current_time = current_time
        self.crunch_time = crunch_time
        self.start_time = time(9,0)
        self.end_time = time(17,0)

    def change_state(self):
        if self.is_off_hours:
            self.is_off_hours = False
        else:
            self.is_off_hours = True

    def off_hours_resolver(self):
        if self.start_time <= self.current_time <= self.end_time:
            self.is_off_hours = False
        elif self.crunch_time:
            self.is_off_hours = False
        else:
            self.is_off_hours = True
        return "Good to go" if self.is_off_hours == False else "Off hours"

class RecipeService:
    def __init__(self):
        self.recipes = {"black": "Standard black coffee", "latte": "Latte with cow milk", "vegan-latte": "Latte with oat milk"}

    def return_recipe(self, recipe_name):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name]
        else:
            return "Recipe not found"



if __name__ == "__main__":
    current_time = datetime.now().time()
    crunch_time = False
    timer_service = TimerService(is_off_hours = False, current_time = current_time, crunch_time = crunch_time)
    timer_service.off_hours_resolver()
    recipe_service = RecipeService()
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    recipe = "black"
    maker.make_coffee(recipe)
    recipe = "latte"
    maker.make_coffee(recipe)
    recipe = "macchiato"
    maker.make_coffee(recipe)
    recipe = "vegan-latte"
    maker.make_coffee(recipe)