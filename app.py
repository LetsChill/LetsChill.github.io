from quart import Quart, render_template, websocket
import requests

app = Quart(__name__)


counts = {
        "count" : None,
        "player_count" : None
    }

async def counts_updat():
    return
    

@app.route('/')
async def hello_world():
    return render_template('index.html', counts=counts)

@app.route("/quit")
async def main():
    return quit()
    
if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(threaded=True, port=5000)
