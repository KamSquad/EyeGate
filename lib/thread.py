import json

from threading import Thread
import queue


def run(thread_function, args):
    queued_request = queue.Queue()
    Thread(target=thread_function, args=(args, queued_request)).start()
    thread_answer = queued_request.get()
    try:
        thread_answer = json.loads(thread_answer)
    except: pass
    return thread_answer
