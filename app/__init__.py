import json
from time import strftime
from flask import Flask, render_template, request
from redis import Redis
from rq import Queue
from .task import count_words

app = Flask(__name__)
r = Redis()
q = Queue(connection=r)

@app.route("/")
def home():
    text = "My experiment text from someone"
    job = q.enqueue(count_words, text)
    task = job.get_id()
    result = {
        "Task": task,
        "Time": strftime('%a, %d %b %Y %H:%M:%S')
    }
    
    return json.dumps({"result": result})