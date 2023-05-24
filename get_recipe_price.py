import random
# region piece of cake

def get_price_per_100g(prices, name):
    """Gets the price per 100g for the ingredient from the prices dictionary."""
    return prices.get(name, 0)

def is_optional(name, optionals):
    """Checks if the ingredient is optional."""
    return name in optionals

def calculate_ingredient_price(price_per_100g, quantity):
    """Calculates the price for the quantity of the ingredient we want to buy."""
    return price_per_100g * quantity / 100

def get_recipe_price(prices, optionals=[], **ingredients):
    """Calculates the total price of the recipe."""
    total_price = 0
    for name, quantity in ingredients.items():
        if not is_optional(name, optionals):
            price_per_100g = get_price_per_100g(prices, name)
            ingredient_price = calculate_ingredient_price(price_per_100g, quantity)
            total_price += ingredient_price
    return total_price


# endregion

def main():
    """Runs the main program."""
    prices = {"flour": 1.2, "sugar": 2.5, "salt": 0.5, "butter": 3.0, "eggs": 1.0}
    optionals = ["salt"]
    ingredients = {"flour": 500, "sugar": 250, "salt": 5, "butter": 100, "eggs": 2}
    recipe_price = get_recipe_price(prices, optionals, **ingredients)
    print(f"The total price of the recipe is: {recipe_price}")

if __name__ == '__main__':
    main()
