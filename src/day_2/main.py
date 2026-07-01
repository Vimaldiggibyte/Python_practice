from game import start_game


def main():
    print("=" * 35)
    print("    NUMBER GUESSING GAME")
    print("=" * 35)

    while True:
        start_game()

        choice = input("\nDo you want to play again? (y/n): ").strip().lower()

        if choice != "y":
            print("\nThank you for playing!")
            break


if __name__ == "__main__":
    main()