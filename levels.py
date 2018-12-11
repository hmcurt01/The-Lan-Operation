from wall import Wall
from weapon import Weapon
Levels = {1: [
        "                                    W",
        "                W                   W",
        "                W                   W",
        "                W                   W",
        "    R           W                   W",
        "                                    W",
        "                                    W",
        "                                    W",
        "                     S              W",
        "            S                       W",
        "                                    W",
        "                              S     W",
        "                                    W",
        "             S                      W",
        "                                    W",
        "    R               R               W",
        "                                    W",
        "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    ]
}

# Parse the level string above. W = wall, E = exit
def parse_level(level):
    x = y = 0
    for row in level:
        for col in row:
            if col == 'W':
                Wall((x, y))
            if col == 'S':
                Weapon((x, y), (255, 0, 0), 'Stapler')
            if col == 'R':
                Weapon((x, y), (0, 255, 0), 'Ruler')
            x += 16
        y += 16
        x = 0