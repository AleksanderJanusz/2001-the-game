"""Modification of game 2001, here you can pick the dice"""
from random import randint
from game2001 import _throws, _score_print

types_of_dices = [3, 4, 6, 8, 10, 12, 20, 100]


def _dices(id_: int) -> int:
    """
    Pick the dice function
    :param id_: number of the dice
    :return: picked dice
    """
    while True:
        dice_ = list(input(f"\nEnter dice {id_}: "))
        if dice_[0] == "D":
            try:
                dice_ = int("".join(dice_[1:]))
            except ValueError:
                print("Wrong value!")
                continue
        else:
            print("Wrong value!")
            continue
        if dice_ in types_of_dices:
            return dice_
        print("Wrong value!")


def _rand_dices():
    """
    Draw of the dice for program
    :return: sum of the draw dices
    """
    dices = [types_of_dices[randint(0, 7)], types_of_dices[randint(0, 7)]]
    print(f"\nI pick D{dices[0]} and D{dices[1]}\n")
    return sum(dices)


def main2() -> None:
    """
    First rund and then looped game
    :return: None
    """
    player_, v_player, check_, p_dices, v_dices = 0, 0, None, ["", ""], ["", ""]
    print("Let the game begin!")
    print(f"You have {player_} points! \nI have {v_player} points!")
    print("You can chose the dice from set: D3, D4, D6, D8, D10, D12, D20, D100.")
    for i in range(2):
        p_dices[i] = _dices(i + 1)
    p_dices = sum(p_dices)
    v_dices = _rand_dices()
    player_, v_player = [randint(2, p_dices)] * 2, [randint(2, v_dices)] * 2
    _score_print(player_, v_player, 1)
    while True:
        p_dices = ["", ""]
        for i in range(2):
            p_dices[i] = _dices(i + 1)
        p_dices = sum(p_dices)
        v_dices = _rand_dices()
        player_ = _throws(player_[0], p_dices)
        v_player = _throws(v_player[0], v_dices)
        check_ = _score_print(player_, v_player, 1)
        if check_ == 0:
            print("\n\t\t\t!!You win!!")
            return None
        if check_ == 1:
            print("\n\t\t\t!!I win!!")
            return None
