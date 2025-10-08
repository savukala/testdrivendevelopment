from live_coding_session2 import *

from datetime import datetime, timedelta

# Office hours is between 0900-1700
time_is_within_office_hours = datetime(2025, 8, 23, 14, 0).time()
time_is_not_within_office_hours = datetime(2025, 8, 23, 20, 0).time()


def test_coffee_maker__makes_coffee():
    crunch_time = True
    timer_service = TimerService(crunch_time=crunch_time)
    maker = CoffeeMaker(timer_service=timer_service)
    assert maker.make_coffee() == "Enjoy your delicious coffee"

def test_coffee_maker_does_not_make_coffee_during_off_hours():
    crunch_time = True
    timer_service = TimerService(crunch_time=crunch_time)
    timer_service.change_state()
    maker = CoffeeMaker(timer_service=timer_service)
    assert maker.make_coffee() == "Off hours, no coffee"

def test_timer_service_should_return_true_when_off_hours():
    crunch_time = True
    timer_service = TimerService(crunch_time=crunch_time)
    timer_service.change_state()
    assert timer_service.is_off_hours == True

def test_timer_service_should_override_state_when_it_is_crunch_hours():
    crunch_time = True
    timer_service = TimerService(crunch_time=crunch_time)
    timer_service.change_state()
    assert timer_service.return_state() == False

def test_timer_service_allows_to_make_coffee_when_office_hours():
    crunch_time = False
    current_time = time_is_within_office_hours
    timer_service = TimerService(crunch_time=crunch_time, current_time=current_time)
    assert timer_service.time_resolver() == "It is office hours"
    maker = CoffeeMaker(timer_service=timer_service)
    assert maker.make_coffee() == "Enjoy your delicious coffee"

def test_timer_service_does_not_allow_to_make_coffee_when_off_hours():
    crunch_time = False
    current_time = time_is_not_within_office_hours
    timer_service = TimerService(crunch_time=crunch_time, current_time=current_time)
    assert timer_service.time_resolver() == "It is off hours"
    maker = CoffeeMaker(timer_service=timer_service)
    assert maker.make_coffee() == "Off hours, no coffee"

def test_recipe_service_server_black_coffee():
    recipe_service = RecipeService()
    recipe = "black"
    assert recipe_service.return_recipe(recipe_name=recipe) == "Standard black coffee"

def test_coffee_maker_serves_black_coffee_during_office_hours():
    recipe_service = RecipeService()
    recipe = "black"
    crunch_time = False
    current_time = time_is_within_office_hours
    timer_service = TimerService(crunch_time=recipe_service, current_time=current_time)
    maker = CoffeeMaker(timer_service=timer_service, recipe_service=recipe_service)
    assert maker.make_coffee(recipe=recipe) == "Enjoy your delicious coffee"