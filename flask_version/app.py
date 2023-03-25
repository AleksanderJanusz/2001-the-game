from random import randint
from mod1 import types_of_dices

from flask import Flask, request, render_template


def _throw_flask(value_: int, dice_: int) -> list[int, int]:
    throw_ = randint(2, dice_)
    if throw_ == 7:
        value_ = int(value_ / 7)

    elif throw_ == 11:
        value_ *= 11

    else:
        value_ += throw_
    return [value_, throw_]


app = Flask(__name__, template_folder="./templates")


@app.route("/", methods=["POST", "GET"])
def _start():
    if request.method == "GET":
        return render_template("start.html")
    if request.method == "POST":
        return render_template("form.html", p_score=0, v_score=0)

@app.route("/game", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        player_, v_player = int(request.form["score_p"]), int(request.form["score_v"])

        p_dice = int(request.form["dice1"]) + int(request.form["dice2"])
        v_dice = sum([types_of_dices[randint(0, 7)], types_of_dices[randint(0, 7)]])

        player_, p_throw = _throw_flask(player_, p_dice)
        v_player, v_throw = _throw_flask(v_player, v_dice)

        if player_ > 2000:
            return render_template("win.html",
                                who_="You",
                                score_win=v_player,
                                thr="Throw: ",
                                p_thr=str(p_throw),
                                v_thr=str(v_throw),
                                p_score=player_,
                                v_score=v_player)
        if v_player > 2000:
            return render_template("win.html", who_="I", score_win=v_player)

        return render_template("form.html",
                               thr="Throw: ",
                               p_thr=str(p_throw),
                               v_thr=str(v_throw),
                               p_score=player_,
                               v_score=v_player)

    if request.method == "GET":
        return render_template("form.html", p_score=0, v_score=0)


if __name__ == "__main__":
    app.run(debug=True)
