import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask---Egor Sidelnikov----GLITCH"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# My web:
# create git with only this directory on git. just files of that github
# My Projects: https://glitch.com/dashboard?group=owned&sortColumn=boost&sortDirection=DESC&page=1&showAll=false&filterDomain=