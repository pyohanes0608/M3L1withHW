from flask import Flask
import random
from logic import *

app = Flask(__name__)
facts_list = ["Elon Musk claims that social networks are designed to keep us on the platform, so that we spend as much time as possible viewing content.",
            "According to a study conducted in 2018, more than 50% of people aged 18 to 34 consider themselves dependent on their smartphones.",
            "Social networks have both positive and negative sides, and we must be aware of both when using these platforms.",
            "The study of technology addiction is one of the most relevant areas of modern scientific research.", 
            "One way to combat technology addiction is to find activities that bring pleasure and improve your mood."]

@app.route("/")
def index():
    return f'''
        <h1>Hi! on this page, you can learn some interesting facts about technology addiction!</h1>
        <a href="/random_fact">View a random fact!</a>
        <br><br><a href="/password">Generate your password!</a>
        '''

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Go Back</a>'

@app.route("/password")
def gen_password():
    return f'<p>{gen_pass(10)}</p> <a href="/">Go Back</a>'

app.run(debug=True)