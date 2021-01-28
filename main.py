from match import Match
from scoreboard import Scoreboard
import multiprocessing


def start_match(q):
    q.put(Match(800, 8).loop_match())


def start_scoreboard(v):
    Scoreboard(200, 400).main_loop(v)


def main():
    queue = multiprocessing.Queue()
    value = multiprocessing.Value('d', 0)
    scoreboard = multiprocessing.Process(target=start_scoreboard, args=(value,))
    scoreboard.start()
    while True:
        match = multiprocessing.Process(target=start_match, args=(queue,))
        match.start()
        match.join()
        result = queue.get()
        queue.empty()
        if result == 'WHITE':
            value.value = 1
        if result == 'BLACK':
            value.value = 2


if __name__ == '__main__':
    main()
