from live_coding_boilerplate import CoffeeMaker, TimerService, RecipeService

from datetime import datetime, timedelta

time_is_within_office_hours = datetime(2025, 8, 23, 14, 0).time()
time_is_not_within_office_hours = datetime(2025, 8, 23, 20, 0).time()


def test_coffee_maker__makes_coffee():
    is_off_hours = False
    current_time = time_is_within_office_hours
    crunch_time = False
    timer_service = TimerService(is_off_hours=is_off_hours, current_time=current_time, crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer_service)
    assert maker.make_coffee() == "Enjoy your delicious coffee"

def test_coffee_maker_does_not_brew_during_off_hours():
    is_off_hours = True
    current_time = time_is_not_within_office_hours
    crunch_time = False
    timer_service = TimerService(is_off_hours=is_off_hours, current_time=current_time, crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer_service)
    assert maker.make_coffee() == "Off hours, no coffee"

def test_timer_service_should_return_true_when_it_is_office_hours():
    is_off_hours = False
    current_time = time_is_within_office_hours
    crunch_time = False
    timer = TimerService(is_off_hours=is_off_hours, current_time=current_time, crunch_time=crunch_time)
    assert timer.off_hours_resolver() == False

def test_timer_service_should_override_time_setting_if_it_is_crunch_time():
    crunch_time = True
    is_off_hours = False
    current_time = time_is_not_within_office_hours
    timer = TimerService(is_off_hours=is_off_hours, current_time=current_time, crunch_time=crunch_time)
    assert timer.off_hours_resolver() == False

def test_recipe_service_should_return_black_coffee():
    recipe_service = RecipeService()
    recipe = "black"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Standard black coffee"

def test_recipe_service_should_return_latte_coffee():
    recipe_service = RecipeService()
    recipe = "latte"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Latte with cow milk"


def test_recipe_service_should_return_vegan_latte_coffee():
    recipe_service = RecipeService()
    recipe = "vegan-latte"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Latte with oat milk"

def test_coffee_maker_brews_black_coffee_during_office_hours():
    crunch_time = False
    is_off_hours = False
    current_time = time_is_within_office_hours
    recipe = "black"
    recipe_service = RecipeService()
    timer = TimerService(is_off_hours=is_off_hours, current_time=current_time, crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer, recipe_service=recipe_service)
    assert maker.make_coffee(recipe) == "Enjoy your delicious coffee"

def test_coffee_maker_does_not_brew_unknown_recipes_during_office_hours():
    crunch_time = False
    is_off_hours = False
    current_time = time_is_within_office_hours
    recipe = "macchiato"
    recipe_service = RecipeService()
    timer = TimerService(is_off_hours=is_off_hours, current_time=current_time, crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer, recipe_service=recipe_service)
    assert maker.make_coffee(recipe) == "Recipe not found"