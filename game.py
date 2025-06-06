from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Global variables
board = [" " for _ in range(9)]
current_player = "X"


def check_winner(b):
    # Rows, columns, diagonals
    lines = [
        [b[0], b[1], b[2]],
        [b[3], b[4], b[5]],
        [b[6], b[7], b[8]],
        [b[0], b[3], b[6]],
        [b[1], b[4], b[7]],
        [b[2], b[5], b[8]],
        [b[0], b[4], b[8]],
        [b[2], b[4], b[6]],
    ]
    for line in lines:
        if line[0] == line[1] == line[2] and line[0] != " ":
            return line[0]
    if " " not in b:
        return "Draw"
    return None


@app.route("/")
def index():
    winner = check_winner(board)
    return render_template("index.html", board=board, winner=winner, player=current_player)


@app.route("/move/<int:cell>")
def move(cell):
    global board, current_player
    if board[cell] == " " and check_winner(board) is None:
        board[cell] = current_player
        current_player = "O" if current_player == "X" else "X"
    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    global board, current_player
    board = [" " for _ in range(9)]
    current_player = "X"
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)
