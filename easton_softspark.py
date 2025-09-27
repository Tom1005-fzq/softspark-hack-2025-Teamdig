from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 游戏状态变量
target = random.randint(1, 100)
attempts = 0


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess_number():
    global target, attempts
    user_guess = int(request.form['guess'])
    attempts += 1

    if user_guess < target:
        return jsonify({"result": "Too Low"})
    elif user_guess > target:
        return jsonify({"result": "Too High"})
    else:
        msg = f"🎉 Correct! The number was {target}. You used {attempts} attempts. Rating: {rating}"

        target = random.randint(1, 100)
        attempts = 0
        return jsonify({"result": msg})


if __name__ == "__main__":
    app.run(debug=True)