import pytest
from coffee_maker_by_chatgpt import CoffeeMaker

# Python

def test_initial_state():
    maker = CoffeeMaker()
    assert maker.water == 0
    assert maker.coffee_beans == 0
    assert not maker.is_on

def test_add_water():
    maker = CoffeeMaker()
    maker.add_water(300)
    assert maker.water == 300
    maker.add_water(200)
    assert maker.water == 500

def test_add_coffee_beans():
    maker = CoffeeMaker()
    maker.add_coffee_beans(10)
    assert maker.coffee_beans == 10
    maker.add_coffee_beans(5)
    assert maker.coffee_beans == 15

def test_turn_on_and_off():
    maker = CoffeeMaker()
    maker.turn_on()
    assert maker.is_on
    maker.turn_off()
    assert not maker.is_on

def test_brew_coffee_not_on(capsys):
    maker = CoffeeMaker()
    maker.add_water(300)
    maker.add_coffee_beans(20)
    maker.brew_coffee()
    captured = capsys.readouterr()
    assert "Turn on the coffee maker first." in captured.out

def test_brew_coffee_not_enough_water(capsys):
    maker = CoffeeMaker()
    maker.add_water(100)
    maker.add_coffee_beans(20)
    maker.turn_on()
    maker.brew_coffee()
    captured = capsys.readouterr()
    assert "Not enough water." in captured.out

def test_brew_coffee_not_enough_beans(capsys):
    maker = CoffeeMaker()
    maker.add_water(300)
    maker.add_coffee_beans(5)
    maker.turn_on()
    maker.brew_coffee()
    captured = capsys.readouterr()
    assert "Not enough coffee beans." in captured.out

def test_brew_coffee_success(capsys):
    maker = CoffeeMaker()
    maker.add_water(300)
    maker.add_coffee_beans(20)
    maker.turn_on()
    maker.brew_coffee()
    captured = capsys.readouterr()
    assert "Brewing coffee... Enjoy your cup!" in captured.out
    assert maker.water == 100
    assert maker.coffee_beans == 5