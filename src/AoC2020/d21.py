class product:
    ingredients = []
    allergens = []

    def __init__(self, ingredients, allegrens):
        self.ingredients = ingredients
        self.allergens = allegrens


with open("/Users/tatianadidik/IdeaProjects/adventofcode2018/resources/AoC2020/d21.txt") as f:
    content = f.readlines()
    products = []
    allergen_to_ingredient = dict()
    ingredient_to_allergen = dict()
    for line in content:
        s = line.split('(contains')
        i = [x for x in s[0].split(" ") if x.strip() != '']
        a = [] if len(s) == 1 else [x for x in s[1].strip().replace(',', '')[:-1].split(" ") if x.strip() != '']
        products.append(product(i, a))
        for aa in a:
            allergen_to_ingredient[aa] = set(i)
        for ii in i:
            ingredient_to_allergen[ii] = set(a)
    for product in products:
        for a in product.allergens:
            for q in [x for x in allergen_to_ingredient[a] if x not in product.ingredients]:
                allergen_to_ingredient[a].remove(q)

    ingredients_to_count = dict.fromkeys(ingredient_to_allergen.keys(), 0)
    for product in products:
        for ing in product.ingredients:
            if ing in ingredients_to_count:
                for a, ings in allergen_to_ingredient.items():
                    if ing in ings and ing in ingredients_to_count:
                        del (ingredients_to_count[ing])
            if ing in ingredients_to_count:
                ingredients_to_count[ing] += 1
    s = 0
    for c in ingredients_to_count.values():
        s += c
    print(s)

    changed = True
    while changed:
        changed = False
        for a in allergen_to_ingredient.keys():
            if len(allergen_to_ingredient[a]) == 1:
                ingredient = list(allergen_to_ingredient[a])[0]
                for a1 in allergen_to_ingredient:
                    if a != a1 and ingredient in allergen_to_ingredient[a1]:
                        allergen_to_ingredient[a1].remove(ingredient)
                        changed = True

    allergens = sorted(list(allergen_to_ingredient.keys()))
    res = ''
    for a in allergens:
        if res == '':
            res += list(allergen_to_ingredient[a])[0]
        else:
            res += ',' + list(allergen_to_ingredient[a])[0]
    print(res)

