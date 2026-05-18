def format_coffee_order(order):
    total = 0
    result = []

    if "cold brew" in order:
        total += 4.50
        result.append("cold brew")

    if "oat latte" in order:
        total += 5.00
        result.append("oat latte")

    if "cappuccino" in order:
        total += 4.75
        result.append("cappuccino")

    if "espresso" in order:
        total += 3.00
        result.append("espresso")

    if "vanilla syrup" in order:
        total += 0.75
        result.append("vanilla syrup")

    if "caramel drizzle" in order:
        total += 0.60
        result.append("caramel drizzle")

    if "extra shot" in order:
        total += 0.50
        result.append("extra shot")

    if "oat milk" in order:
        total += 0.75
        result.append("oat milk")

    if "cream" in order:
        total += 0.75
        result.append("cream")

    return " + ".join(result) + f": ${total:.2f}"


print(format_coffee_order("I'd like an oat latte with vanilla syrup and an extra shot please."))
print(format_coffee_order("Just an espresso please."))