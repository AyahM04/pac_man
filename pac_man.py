import sys
import pygame
from conf import read_json
from menu import show_menu
from maze import Maze

argv = sys.argv
t = read_json(argv[1])
pygame.init()

info = pygame.display.Info()
window_width = min(1600, info.current_w - 100)
window_height = min(900, info.current_h - 100)

screen = pygame.display.set_mode((window_width, window_height))
fram_clock = pygame.time.Clock()
mode = "menu"

maze = None
current_level = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if mode == "game":
                mode = "menu"
            else:
                sys.exit()

    if mode == "menu":
        mode = show_menu(screen)

    elif mode == "start":
        level_conf = t.levels[current_level]
        try:
            maze = Maze(
                width=level_conf["width"],
                height=level_conf["height"],
                seed=42 if current_level == 0 else 0,
                perfect=False,
            )
            mode = "game"
        except RuntimeError as exc:
            print(f"Warning: {exc}")
            mode = "menu"

    elif mode == "game":
        screen.fill((0, 0, 0))
        cell_size = maze.cell_size_for(
            window_width - 100, window_height - 150
        )
        maze.draw(screen, cell_size, origin=(50, 50))

    elif mode == "exit":
        sys.exit()

    pygame.display.update()
    fram_clock.tick(60)
