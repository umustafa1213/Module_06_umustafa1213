def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    spell_name = "Dark Fantasy"
    ingredients = "Bats, frogs and arsenic"

    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record
        print("Testing record_light_spell:",
              f"{dark_spell_record(spell_name, ingredients)}")
    except ImportError as e:
        print("Import Error! -", e)


if __name__ == "__main__":
    main()
