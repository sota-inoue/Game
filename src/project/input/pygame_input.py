import pygame

def pygame_input():
    # pygameイベント取得
    events = pygame.event.get()
    for event in events:
        # マウスクリックの場合の処理(仕様でマウスクリックをタッチ入力として拾ってくれ、Windows上でのデバックも楽なため)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            return x, y
    return 0, 0