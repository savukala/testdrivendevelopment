from live_coding_boilerplate import CoffeeMaker

def test_coffee_maker__makes_coffee():
    maker = CoffeeMaker()
    assert maker.make_coffee() == "Enjoy your delicious coffee"

