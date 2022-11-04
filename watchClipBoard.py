import pyperclip
import time
import requests

HOST = ""
PORT = "5000"
URL = "http://" + HOST + ":" + PORT


def get_clipboard():
    """获取剪贴板数据"""
    content = pyperclip.paste()
    return content


def set_remote_clipboard(content):
    """设置对端的剪贴板"""
    try:
        requests.post(url=URL+"/setClipboard", json={"content": content}, timeout=(1, 1))
    except Exception as e:
        print(e)


def watch(content):
    while True:
        new_content = get_clipboard()
        if content != new_content:
            content = new_content
            set_remote_clipboard(new_content)
        time.sleep(1)
