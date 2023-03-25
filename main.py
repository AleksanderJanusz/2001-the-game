"""Main modul of the game 2001"""
from game2001 import main1
from mod1 import main2


def main() -> None:
    """Menu of the game"""
    print("Hello! Roll the dice who get to 2001 first wins!")
    print("""\t o In this game you throw two dices
     o Every time sum of throws will be 7 you divide your points by 7
     o Every time sum of throws will be 11 you multiple your points by 11""")
    print("""There are two version of the game:
     1 Basic where you throw two D6 dices
     2 Modded where you pick dices before throws""")
    version_ = input("Enter version 1 or 2: ")
    print("\n\n")
    if version_ == "1":
        main1()
    elif version_ == "2":
        main2()


main()
