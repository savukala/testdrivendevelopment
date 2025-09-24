
from CoffeeMaker import CoffeeMaker, RecipeService
from CoffeeMaker import TimerService
from datetime import datetime
time_within_office_hours = datetime(2025, 9, 23, 14, 0).time()
time_not_within_office_hours = datetime(2025, 9, 23, 18, 0).time()
time_placeholder = datetime(2025, 9, 23, 8, 0).time()
crunch_time = False
user_recipe = "black"

def test_should_make_coffee():
    current_time = time_within_office_hours
    recipe_service = RecipeService()
    timer_service = TimerService(is_off_hours=False, current_time=current_time, crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert maker.make_coffee(recipe = user_recipe) == "Enjoy your delicious coffee"

def test_should_not_make_coffee_if_off_hours():
    current_time = time_not_within_office_hours
    recipe_service = RecipeService()
    timer_service = TimerService(is_off_hours=True, current_time=current_time, crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert maker.make_coffee(recipe=user_recipe) == "No coffee during off hours"

def test_timer_service_should_return_false_when_off_hours():
    current_time = time_not_within_office_hours
    timer = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    assert timer.is_off_hours == False

def test_timer_service_should_return_true_when_office_hours():
    current_time = time_within_office_hours
    timer = TimerService(is_off_hours=True, current_time=current_time, crunch_time=crunch_time)
    assert timer.is_off_hours == True

def test_timer_service_should_change_state_internally():
    current_time = time_not_within_office_hours
    timer_service = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    timer_service.change_state()
    assert timer_service.is_off_hours == True
    timer_service.change_state()
    assert timer_service.is_off_hours == False

def test_coffee_maker_behavior_changes_with_timer_service_state():
    current_time = time_placeholder
    timer_service = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    recipe_service = RecipeService()
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert maker.make_coffee(recipe = user_recipe) == "Enjoy your delicious coffee"
    timer_service.change_state()
    assert maker.make_coffee(recipe = user_recipe) == "No coffee during off hours"

def test_timer_service_state_should_change_with_datetimes():
    current_time = time_within_office_hours
    timer_service = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    assert timer_service.off_hours_resolver() == "Good to go"
    current_time = time_not_within_office_hours
    timer_service = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    assert timer_service.off_hours_resolver() == "Off hours"

def test_timer_service_should_override_office_hours_if_crunch_time():
    current_time = time_not_within_office_hours
    crunch_time = True
    timer_service = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    recipe_service = RecipeService()
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert maker.make_coffee(recipe=user_recipe) == "Enjoy your delicious coffee"

def test_recipe_service_brews_black_coffee():
    recipe_service = RecipeService()
    recipe = "black"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Standard black coffee"

def test_recipe_service_returns_latte():
    recipe_service = RecipeService()
    recipe = "latte"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Latte with cow milk"

def test_recipe_service_returns_vegan_latte():
    recipe_service = RecipeService()
    recipe = "vegan-latte"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Latte with oat milk"

def test_recipe_service_should_return_error_for_unknown_recipes():
    recipe_service = RecipeService()
    recipe = "unknown"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Recipe not found"

def test_coffee_maker_brews_black_coffee_during_office_hours():
    current_time = time_within_office_hours
    recipe_service = RecipeService()
    timer_service = TimerService(is_off_hours = False, current_time=current_time, crunch_time=crunch_time)
    coffee_maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert coffee_maker.make_coffee(recipe = user_recipe) == "Enjoy your delicious coffee"

def test_coffee_maker_brews_latte_during_office_hours():
    user_recipe = "latte"
    current_time = time_within_office_hours
    recipe_service = RecipeService()
    timer_service = TimerService(is_off_hours=False, current_time=current_time, crunch_time=crunch_time)
    coffee_maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert coffee_maker.make_coffee(recipe=user_recipe) == "Enjoy your delicious coffee"

def test_coffee_maker_brews_vegan_latte_during_office_hours():
    user_recipe = "vegan-latte"
    current_time = time_within_office_hours
    recipe_service = RecipeService()
    timer_service = TimerService(is_off_hours=False, current_time=current_time, crunch_time=crunch_time)
    coffee_maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert coffee_maker.make_coffee(recipe=user_recipe) == "Enjoy your delicious coffee"
