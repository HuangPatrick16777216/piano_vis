#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import pygame
from .video import Video
from .utils import PreciseClock

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)


def launch(resizable=True):
    """
    Starts pianovis app.
    :param resizable: Make the window resizable?
    """
    pygame.display.set_caption("Piano Visualizer - App")
    if resizable:
        window = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    else:
        window = pygame.display.set_mode((1600, 900))

    width, height = 1280, 720
    video = Video((1920, 1080), 30, 1)

    resized = False
    clock = PreciseClock(60)
    while True:
        clock.tick()
        pygame.display.update()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.VIDEORESIZE:
                resized = True
                width, height = event.size

            elif event.type == pygame.ACTIVEEVENT and resized:
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                resized = False

        vid_loc = list(map(int, (width//8, 50)))
        vid_size = list(map(int, (width/2, width*9/32)))

        window.fill(BLACK)
        window.blit(pygame.transform.scale(video._render(0), vid_size), vid_loc)
        pygame.draw.rect(window, WHITE, (*vid_loc, *vid_size), 1)
