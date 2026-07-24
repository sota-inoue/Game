# src/project/system/health/health_system.py
from Domain.game_state import GameState, GameProgressState

class HealthSystem:
    def __init__(self):
        pass

    def increase_urgency(self, state: GameState, amount: int) -> None:
        """
        障害物への衝突やペナルティで切迫度を増やす
        """
        current_urgency = state.get_urgency_level()
        new_urgency = current_urgency + amount
        state.set_urgency_level(new_urgency)

    def update(self, state: GameState) -> None:
        """
        毎フレーム呼び出される更新処理。
        100%に達しているか確認し、到達していればゲームオーバーへ遷移させる。
        """
        current_urgency = state.get_urgency_level()
        max_urgency = state.get_max_urgency_level()

        # 切迫度が100%以上になったらゲームオーバー
        if current_urgency >= max_urgency:
            state.set_game_state(GameProgressState.GAMEOVER)