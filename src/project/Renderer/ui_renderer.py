# src/project/renderer/ui_renderer.py
import pygame
from Domain.game_state import GameState

class UIRenderer:
    def __init__(self, font_path: str = None):
        pygame.font.init()
        self.font = pygame.font.Font(font_path, 24)

    def draw(self, surface: pygame.Surface, state: GameState) -> None:
        """UI全体の描画を行う"""
        urgency = state.get_urgency_level()
        max_urgency = state.get_max_urgency_level()

        # 切迫度ゲージの描画位置・サイズ
        gauge_x, gauge_y = 20, 20
        gauge_width, gauge_height = 200, 25

        # 1. ゲージの背景枠（灰色）
        pygame.draw.rect(surface, (100, 100, 100), (gauge_x, gauge_y, gauge_width, gauge_height))

        # 2. ゲージの中身（切迫度に応じて赤くなるバー）
        fill_width = int((urgency / max_urgency) * gauge_width)
        # 危険度が高くなると色が変化（黄 → 赤）
        color = (255, 50, 50) if urgency > 70 else (255, 200, 0)
        
        if fill_width > 0:
            pygame.draw.rect(surface, color, (gauge_x, gauge_y, fill_width, gauge_height))

        # 3. 枠線（白色）
        pygame.draw.rect(surface, (255, 255, 255), (gauge_x, gauge_y, gauge_width, gauge_height), 2)

        # 4. パーセント表示テキスト（例: "おなか: 75%"）
        text_surface = self.font.render(f"おなか: {urgency}%", True, (255, 255, 255))
        surface.blit(text_surface, (gauge_x + gauge_width + 10, gauge_y))