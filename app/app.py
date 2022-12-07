from flask import Flask, request, abort
import os
from command_engine import CommandEnginge

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def perform_query():
    try:
        params = request.json
        engine = CommandEnginge(params)
        result = engine.execute()
    except Exception:
        abort(400, "Cant parse request")
        
    return {
            "status": 'ok',
            "result": result
            }

if __name__ == '__main__':
    app.run()