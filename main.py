import sys
from random import random
from random import choices
from distance import Distance
from pathfinder import PathFinder
import pygame
import numpy as np
from pygame.locals import QUIT

pygame.init()
pygame.font.init()
pygame.display.set_caption('A*Pathfinding Traversal')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 11)
buttonfont = pygame.font.SysFont(None, 20)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
GREEN = (105, 205, 105)
DEEP_BLUE = (7, 42, 108)
GRAY = (128, 128, 128)
DARK_GRAY = (169, 169, 169)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)

start = [3, 5]
destination = [26, 61]

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def originalMap():
    map = [[0] * 2 + [1] * 39 + [0] * 40,
           [0] * 3 + [1] * 41 + [0] * 40,
           [1] * 2 + [0] + [1] * 45 + [0] * 40,
           [1] * 46 + [0] * 4 + [1] + [0] * 25 + [1] + [0] * 40,
           [1] * 45 + [0] * 4 + [1] + [0] * 26 + [1] * 3 + [0] * 40,
           [0] + [1] * 55 + [0] * 19 + [1] * 4 + [0] * 40,
           [0] + [1] * 53 + [0] + [1] + [0] * 19 + [1] * 4 + [0] * 40,
           [0] + [1] * 51 + [0] * 3 + [1] + [0] * 18 + [1] * 5 + [0] * 40,
           [0] + [1] * 51 + [0] + [1] * 4 + [0] * 11 + [1] * 11 + [0] * 40,
           [0] + [1] * 50 + [0] * 2 + [1] * 4 + [0] * 10 + [1] * 11 + [0] * 40,
           [0] + [1] * 50 + [0] * 2 + [1] * 3 + [0] + [1] + [0] * 9 + [1] * 9 + [0] * 40,
           [1] * 51 + [0] * 2 + [1] * 5 + [0] * 5 + [1] * 2 + [0] + [1] * 9 + [0] * 40,
           [1] * 51 + [0] * 2 + [1] * 5 + [0] * 5 + [1] * 11 + [0] * 40,
           [1] * 51 + [0] * 2 + [1] * 5 + [0] * 4 + [1] * 12 + [0] * 40,
           [0] + [1] * 50 + [0] + [1] * 5 + [0] * 3 + [1] * 15 + [0] * 40,
           [0] + [1] * 70 + [0] * 40,
           [1] * 70 + [0] * 40,
           [1] * 69 + [0] * 40,
           [0] + [1] * 68 + [0] * 40,
           [0] + [1] * 66 + [0] * 40,
           [0] * 2 + [1] * 66 + [0] * 40,
           [0] * 3 + [1] * 62 + [0] + [1] + [0] * 40,
           [0] * 3 + [1] * 63 + [0] * 40,
           [0] * 4 + [1] * 62 + [0] * 40,
           [0] * 4 + [1] * 62 + [0] * 40,
           [0] * 5 + [1] * 62 + [0] * 40,
           [0] * 5 + [1] * 61 + [0] * 40,
           [0] * 7 + [1] * 57 + [0] * 40,
           [0] * 9 + [1] * 54 + [0] * 40,
           [0] * 10 + [1] * 52 + [0] * 40,
           [0] * 13 + [1] * 48 + [0] * 40,
           [0] * 16 + [1] * 43 + [0] * 40,
           [0] * 25 + [1] * 32 + [0] * 40,
           [0] * 26 + [1] * 31 + [0] * 40,
           [0] * 27 + [1] * 18 + [0] * 6 + [1] * 6 + [0] * 40,
           [0] * 27 + [1] * 2 + [0] * 3 + [1] * 6 + [0] * 4 + [1] * 4 + [0] * 8 + [1] * 3 + [0] * 40,
           [0] * 32 + [1] * 5 + [0] * 18 + [1] * 3 + [0] * 40,
           [0] * 33 + [1] * 3 + [0] * 19 + [1] * 3 + [0] * 40,
           [0] * 34 + [1] * 2 + [0] * 19 + [1] * 3 + [0] * 40,
           [0] * 56 + [1] * 1 + [0] * 40,
           [0] * 100
           ]
    return map

def originalDist():
    dist = [[Distance(1000, [0, 0]) for i in range(90)] for j in range(79)]
    return dist

map = originalMap()
dist = PathFinder(originalDist())


def setMap(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] != 0:
                map[i][j] = choices([1,2,3], weights=(75,12.5,12.5), k=1)[0]
    # start and destination
    map[start[0]][start[1]] = 1
    map[destination[0]][destination[1]] = 1
    return map


map = setMap(map)


def calcMap(map, dist):
    open_list = [start]
    dist.grid[start[0]][start[1]].distance = 0
    neighbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while open_list:
        cur_pos = open_list.pop(0)
        for neighbor in neighbors:
            new_pos = [cur_pos[0] + neighbor[0], cur_pos[1] + neighbor[1]]
            if new_pos[0] < 0 or new_pos[0] > 90 or new_pos[1] < 0 or new_pos[1] > 79 or map[new_pos[0]][new_pos[1]] != 1:
                continue
            if dist.grid[new_pos[0]][new_pos[1]].distance == 1000:
                dist.grid[cur_pos[0] + neighbor[0]][cur_pos[1] + neighbor[1]].distance = dist.grid[cur_pos[0]][cur_pos[1]].distance + 1
                open_list.append([cur_pos[0] + neighbor[0], cur_pos[1] + neighbor[1]])
                dist.grid[cur_pos[0] + neighbor[0]][cur_pos[1] + neighbor[1]].previous = cur_pos
    print(dist.grid[destination[0]][destination[1]].distance)
    return dist


dist = calcMap(map, dist)


def loadMap(map, dist):
    start_x = 50
    start_y = 50
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == destination[0] and j == destination[1]) or (i == start[0] and j == start[1]):
                pygame.draw.rect(screen, YELLOW, pygame.Rect(start_x, start_y, 10, 10))
                display = font.render(str(dist.grid[i][j].distance), True, BLACK)
                screen.blit(display, (start_x + 1, start_y + 1))
            elif map[i][j] == 1:
                pygame.draw.rect(screen, GREEN, pygame.Rect(start_x, start_y, 10, 10))
                if dist.grid[i][j].distance != 1000:
                    display = font.render(str(dist.grid[i][j].distance), True, BLACK)
                    screen.blit(display, (start_x+1, start_y+1))
            elif map[i][j] == 2:
                pygame.draw.rect(screen, DARK_GRAY, pygame.Rect(start_x, start_y, 10, 10))
                pygame.draw.polygon(screen, GRAY, points=[(start_x,start_y+10), (start_x+5,start_y), (start_x+10,start_y+10)])
            elif map[i][j] == 3:
                pygame.draw.rect(screen, DEEP_BLUE, pygame.Rect(start_x, start_y, 10, 10))
            start_x += 13
        start_x = 50
        start_y += 14


def findShortestPath(dist):
    cell = destination
    path = []
    while cell != start:
        path.append(cell)
        cell = dist.grid[cell[0]][cell[1]].previous
    for cell in path:
        print(cell)
        if cell == destination:
            print(dist.grid[cell[0]][cell[1]].distance)
            continue
        pygame.draw.rect(screen, WHITE, pygame.Rect(50 + cell[1] * 13, 50 + cell[0] * 14, 10, 10))
        display = font.render(str(dist.grid[cell[0]][cell[1]].distance), True, BLACK)
        screen.blit(display, (51 + cell[1] * 13, 51 + cell[0] * 14))
    pygame.display.update()


def click(dist):
    x, y = pygame.mouse.get_pos()
    if 80 < x < 210 and 550 < y < 590:
        map = originalMap()
        dist.grid = originalDist()
        map = setMap(map)
        calcMap(map, dist)
        updateScreen(map, dist)
    elif 80 < x < 210 and 610 < y < 650:
        findShortestPath(dist)


def updateScreen(map, dist):
    screen.fill(LIGHT_BLUE)
    pygame.draw.rect(screen, WHITE, pygame.Rect(80, 550, 130, 40))
    reload = buttonfont.render("Reload Map", True, BLACK)
    screen.blit(reload, (110, 562))
    pygame.draw.rect(screen, WHITE, pygame.Rect(80, 610, 130, 40))
    pathfind = buttonfont.render("Find Shortest Path", True, BLACK)
    screen.blit(pathfind, (87, 622))
    pygame.display.flip()
    loadMap(map, dist)
    pygame.display.update()


updateScreen(map, dist)

# Press the green button in the gutter to run the script.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            click(dist)
    clock.tick(10)