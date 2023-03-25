"""Basic version, roll 2D6"""
from random import randint
from typing import Optional


def _score_print(p_1_: list[int, int], virtual_p: list[int, int]) -> Optional[int]:
    """
    Printing score, checking win conditions
    :param p_1_: player 1
    :param virtual_p: virtual player
    :return: win condition or None
    """
    print(f"You throw {p_1_[1]}!      \t I throw {virtual_p[1]} points!")
    print(f"You have {p_1_[0]} points!\t I have {virtual_p[0]} points!")
    if p_1_[0] > 2000:
        return 0
    if virtual_p[0] > 2000:
        return 1
    input("\n")
    return None


def _throws(value_: int) -> Optional[list[int, int]]:
    """
    Throws 2D6, special cases 7 divide by 7 and 11 multiple by 11
    :param value_: player value
    :return: list[value, throw]
    """
    throw_ = randint(2, 12)
    if throw_ == 7:
        value_ = int(value_ / 7)
    elif throw_ == 11:
        value_ *= 11
    else:
        value_ += throw_
    return [value_, throw_]


def main1() -> None:
    """
    Start the game plus first throw, then the game is looping
    :return: None
    """
    player_, v_player, check_ = 0, 0, None
    print("Let the game begin!")
    print(f"You have {player_} points! \nI have {v_player} points!")
    input("Press Enter to throw")
    player_, v_player = [randint(2, 12)] * 2, [randint(2, 12)] * 2
    _score_print(player_, v_player)
    while True:
        player_ = _throws(player_[0])
        v_player = _throws(v_player[0])
        check_ = _score_print(player_, v_player)
        if check_ == 0:
            print("\n\t\t\t!!You win!!")
            return None
        if check_ == 1:
            print("\n\t\t\t!!I win!!")
            return None
