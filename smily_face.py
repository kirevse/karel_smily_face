from stanfordkarel import *
from stanfordkarel.world_editor import *


TUPLE_ROWS = [
    [(8, 12, BLACK)],
    [(6, 8, BLACK), (8, 12, YELLOW), (12, 14, BLACK)],
    [(4, 6, BLACK), (6, 14, YELLOW), (14, 16, BLACK)],
    [(3, 4, BLACK), (4, 16, YELLOW), (16, 17, BLACK)],
    [(2, 3, BLACK), (3, 17, YELLOW), (17, 18, BLACK)],
    [(2, 3, BLACK), (3, 17, YELLOW), (17, 18, BLACK)],
    [(1, 2, BLACK), (2, 5, YELLOW), (5, 7, BLACK), (7, 13, YELLOW), (13, 15, BLACK), (15, 18, YELLOW), (18, 19, BLACK)],
    [(1, 2, BLACK), (2, 5, YELLOW), (5, 7, BLACK), (7, 13, YELLOW), (13, 15, BLACK), (15, 18, YELLOW), (18, 19, BLACK)],
    [(0, 1, BLACK), (1, 19, YELLOW), (19, 20, BLACK)],
    [(0, 1, BLACK), (1, 19, YELLOW), (19, 20, BLACK)],
    [(0, 1, BLACK), (1, 19, YELLOW), (19, 20, BLACK)],
    [(0, 1, BLACK), (1, 19, YELLOW), (19, 20, BLACK)],
    [(1, 2, BLACK), (2, 5, YELLOW), (5, 6, BLACK), (6, 14, YELLOW), (14, 15, BLACK), (15, 18, YELLOW), (18, 19, BLACK)],
    [(1, 2, BLACK), (2, 6, YELLOW), (6, 7, BLACK), (7, 13, YELLOW), (13, 14, BLACK), (14, 18, YELLOW), (18, 19, BLACK)],
    [(2, 3, BLACK), (3, 7, YELLOW), (7, 8, BLACK), (8, 12, YELLOW), (12, 13, BLACK), (13, 17, YELLOW), (17, 18, BLACK)],
    [(2, 3, BLACK), (3, 8, YELLOW), (8, 12, BLACK), (12, 17, YELLOW), (17, 18, BLACK)],
    [(3, 4, BLACK), (4, 16, YELLOW), (16, 17, BLACK)],
    [(4, 6, BLACK), (6, 14, YELLOW), (14, 16, BLACK)],
    [(6, 8, BLACK), (8, 12, YELLOW), (12, 14, BLACK)],
    [(8, 12, BLACK)]
]

def turn_right():
    for _ in range(3):
        turn_left()


def move_to_beginning_of_next_line_up():
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        move()
        turn_left()
    

def move_to_beginning_of_next_line_down():
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
        move()
        turn_left()


def draw_row(color_range_tuples):
    p = 0
    for t in color_range_tuples:
        for _ in range(p, t[0]):
            move()
            p += 1
        for _ in range(p, t[1]):
            paint_corner(t[2])
            if front_is_blocked():
                break
            move()
            p += 1
    
def draw_circle():
    turn_left()
    while front_is_clear():
        move()
    turn_right()
    for tuple_row in TUPLE_ROWS:
        draw_row(tuple_row)
        move_to_beginning_of_next_line_down()
        
def main():
    draw_circle()

if __name__ == "__main__":
    run_karel_program("smily_face")
