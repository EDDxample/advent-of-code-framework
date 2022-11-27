class Ingredient:
    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories


# Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
# Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
# Butterscotch:  -1,  0,  5,  0,  6
# Sugar:  0,  0,  -2,  2,  1

frosting = Ingredient(4, -2, 0, 0, 5)
candy = Ingredient(0, 5, -1, 0, 8)
butterscotch = Ingredient(-1, 0, 5, 0, 6)
sugar = Ingredient(0, 0, -2, 2, 1)


def part1(puzzle_in: str):
    max_score = 0
    for f in range(100):
        for c in range(100-f):
            for b in range(100-f-c):
                s = 100-f-c-b
                capacity = max(0, f * frosting.capacity + c * candy.capacity + b * butterscotch.capacity + s * sugar.capacity)
                durability = max(0, f * frosting.durability + c * candy.durability + b * butterscotch.durability + s * sugar.durability)
                flavor = max(0, f * frosting.flavor + c * candy.flavor + b * butterscotch.flavor + s * sugar.flavor)
                texture = max(0, f * frosting.texture + c * candy.texture + b * butterscotch.texture + s * sugar.texture)

                score = capacity * durability * flavor * texture
                max_score = max(max_score, score)
    return max_score


def part2(puzzle_in: str):
    max_score = 0
    for f in range(100):
        for c in range(100-f):
            for b in range(100-f-c):
                s = 100-f-c-b

                calories = f * frosting.calories + c * candy.calories + b * butterscotch.calories + s * sugar.calories

                if calories != 500:
                    continue

                capacity = max(0, f * frosting.capacity + c * candy.capacity + b * butterscotch.capacity + s * sugar.capacity)
                durability = max(0, f * frosting.durability + c * candy.durability + b * butterscotch.durability + s * sugar.durability)
                flavor = max(0, f * frosting.flavor + c * candy.flavor + b * butterscotch.flavor + s * sugar.flavor)
                texture = max(0, f * frosting.texture + c * candy.texture + b * butterscotch.texture + s * sugar.texture)

                score = capacity * durability * flavor * texture
                max_score = max(max_score, score)
    return max_score


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
