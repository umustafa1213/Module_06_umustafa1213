import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Accessing alchemy/elements.py using",
          "'from ... import ...' structure")
    print("Testing create_air:", alchemy.elements.create_air())
    print()


if __name__ == "__main__":
    main()
