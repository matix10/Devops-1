from Flask import Flask
import render_template
from templates import main


app = Flask (__name__)


app.route("/")
def main():
    return render_template("main")
