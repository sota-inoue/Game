# src/project/system/health/health_system.py
from Domain.game_state import GameState, GameProgressState

class HealthSystem:
    def __init__(self):
        self._time_accumulator: float = 0.0  # 経過時間の蓄積用タイマー（秒単位）

    def increase_urgency(self, state: GameState, amount: int) -> None:
        """
        障害物への衝突やペナルティで切迫度を増やす
        """
        current_urgency = state.get_urgency_level()
        new_urgency = current_urgency + amount
        state.set_urgency_level(new_urgency)

    def update(self, state: GameState, dt: float = 0.0) -> None:
        """
        毎フレーム呼び出される更新処理。
        時間経過（10秒で1%）による切迫度の増加
        100%に達しているか確認し、到達していればゲームオーバーへ遷移させる。
        """
        # 1. 時間経過による切迫度の増加（10秒ごとに1%）
        self._time_accumulator += dt #dt: 前フレームからの経過時間（秒単位、例: 0.016）
        if self._time_accumulator >= 10.0:
            self.increase_urgency(state, 1)
            self._time_accumulator -= 10.0  # 端数を保持して10秒差し引く

        # 2. 判定と状態遷移
        current_urgency = state.get_urgency_level()
        max_urgency = state.get_max_urgency_level()

        # 切迫度が100%以上になったらゲームオーバー
        if current_urgency >= max_urgency:
            state.set_game_state(GameProgressState.GAMEOVER)