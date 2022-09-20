from flask import Flask, render_template, request
import Utils
import webbrowser

app = Flask(__name__)


@app.route('/')
def score_server_html():
    data = get_score()
    return render_template('ScoreServer.html', data=data)


def get_score():
    try:
        score_file = open(Utils.SCORES_FILE_NAME, "r")
        data_file = score_file.read()
        if data_file == "":
            data_file = "0"
        return data_file
    except:
        return Utils.BAD_RETURN_CODE


def score_server():
    webbrowser.open("http://127.0.0.1:5001")
    app.run(host="0.0.0.0", port=5001, debug=False)





