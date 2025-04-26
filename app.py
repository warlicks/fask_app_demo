from flask import Flask
import datetime as dt 
app = Flask(__name__)


@app.route("/your_name")
def name(name=None):
    return f"Hello World from Sean"
    
@app.route("/datetime")
def current_datetime():
    now = dt.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
