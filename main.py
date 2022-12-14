import pyperclip
from flask import Flask
from flask import request
from threading import Thread
from watchClipBoard import watch

app = Flask(__name__)


@app.route('/setClipboard', methods=["POST"])
def set_clipboard():
    req = request.get_json()
    if "content" in req:
        pyperclip.copy(req.get('content'))
        return {"success": True, "code": 200}
    else:
        return {"success": False, "code": 500}


if __name__ == '__main__':
    watchClipBoard = Thread(target=watch)
    watchClipBoard.start()
    app.run(host="0.0.0.0", debug=False)
