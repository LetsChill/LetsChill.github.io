from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    counts = {
        "count" : 1200,
        "player_count" : 4075
    }
    return render_template('index.html', counts=counts)

@app.route("/quit")
def main():
    return quit()
    
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(threaded=True, port=5000)
