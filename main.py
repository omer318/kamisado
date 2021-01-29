from match import Match
from scoreboard import Scoreboard
import multiprocessing

from win import Win


def start_match(q, sumo_pieces):
    q.put(Match(800, 8, sumo_pieces).loop_match())


def start_scoreboard(v):
    Scoreboard(200, 400).main_loop(v)


def main():
    sumo_pieces = set()
    match_queue = multiprocessing.Queue()
    value = multiprocessing.Array('c', Win.SERIALIZED_LENGTH)
    scoreboard = multiprocessing.Process(target=start_scoreboard, args=(value,))
    scoreboard.start()
    while True:
        match = multiprocessing.Process(target=start_match, args=(match_queue, sumo_pieces))
        match.start()
        match.join()
        result = match_queue.get()
        match_queue.empty()
        value.value = result.serialize()
        sumo_pieces.add((result.piece, result.winner))


if __name__ == '__main__':
    main()
