
from collections import deque
import pygame


class PygameInput:
    def __init__(self):
        self._events = deque()

    def update(self):
        # イベントをまとめて取得する
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self._events.append(event.pos)

            elif event.type == pygame.QUIT:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    def get_input(self):
        if self._events:
            return self._events.popleft()

        return -1, -1

    def has_input(self):
        return bool(self._events)
