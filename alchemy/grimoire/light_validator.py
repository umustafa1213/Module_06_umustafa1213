import alchemy.grimoire


def validate_ingredients(ingredients: str) -> str:
    for ingredient in alchemy.grimoire.light_spell_allowed_ingredients():
        if ingredient in ingredients.lower():
            return ingredients + " - VALID"
    return ingredients + " - INVALID"
