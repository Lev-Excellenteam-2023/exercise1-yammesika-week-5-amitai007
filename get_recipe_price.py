# region piece of cake

def get_recipe_price(prices, optionals=[], **ingredients):
    # Keep track of the total price
    total_price = 0
    # Loop through each key-value pair in the ingredients dictionary
    for name, quantity in ingredients.items():
        # Check if the ingredient is not optional (if it should be included in the price calculation)
        if name not in optionals:
            # Look up the price per 100g for the ingredient in the prices dictionary
            price_per_100g = prices.get(name, 0)
            # Calculate the price for the quantity of the ingredient we want to buy, and add it to the total price
            total_price += price_per_100g * quantity / 100
    # Return the total price
    return total_price


# endregion
