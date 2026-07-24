# src/project/domain/game_state.py
from enum import Enum, auto

class GameProgressState(Enum):
    TITLE = auto()
    PLAYING = auto()
    GAMEOVER = auto()
    CLEAR = auto()

class GameState:
    def __init__(self):
        # 切迫度（0%〜100%）。0からスタート
        self._urgency_level: int = 0
        self._max_urgency_level: int = 100
        
        # ゲームの進行状態
        self._game_state: GameProgressState = GameProgressState.PLAYING

    # --- Urgency Level の Getter / Setter ---
    def get_urgency_level(self) -> int:
        """現在の切迫度を取得する"""
        return self._urgency_level

    def set_urgency_level(self, value: int) -> None:
        """切迫度を更新する（0〜100の範囲内に制限）"""
        self._urgency_level = max(0, min(value, self._max_urgency_level))

    def get_max_urgency_level(self) -> int:
        """最大切迫度（100）を取得する"""
        return self._max_urgency_level

    # --- Game State の Getter / Setter ---
    def get_game_state(self) -> GameProgressState:
        return self._game_state

    def set_game_state(self, state: GameProgressState) -> None:
        self._game_state = state