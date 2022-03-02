from click import prompt
from stories import story
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

@app.route("/")
def words_page():
    prompts = story.prompts
    return render_template("words.html", prompts=prompts)

@app.route("/story")
def story_page():
    text = story.generate(request.args)
    return render_template("story.html", text=text)