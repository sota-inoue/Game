class Attack:
    def __init__(self) -> None:

        # 攻撃物のX座標をフレームごとに保持する
        self._x: list[int] = []

        # 攻撃物のY座標をフレームごとに保持する
        self._y: list[int] = []

        # 攻撃物の画像パスをフレームごとに保持する
        self._path: list[str] = []

        self._is_attack: bool = False
        self._count = 0

    def reset(self) -> None:
        # 攻撃描画用データを初期化する
        self._x = []
        self._y = []
        self._path = []

        # 攻撃状態を解除する
        self._is_attack = False

        # 描画フレーム番号を先頭に戻す
        self._count = 0

    def get_attack_data(self) -> dict:
        # 現在のフレームの攻撃描画データを取得する
        data = {
            "x": self._x[self._count],
            "y": self._y[self._count],
            "path": self._path[self._count]
        }

        # 最後のフレームまで描画した場合は攻撃状態を終了する
        if self._count == 3:
            self._count = 0
            self._is_attack = False

        # 次のフレームへ進む
        else:
            self._count += 1

        return data

    def get_is_attack(self) -> bool:
        return self._is_attack

    def create_attack_date(self, target_x: int, target_y: int, path: str | None) -> None:

        self._is_attack = True

        # 攻撃物は攻撃対象と同じ列を移動するため、すべてのフレームで同じX座標を使用する
        self._x = [target_x, target_x, target_x, target_x]

        # 攻撃対象のレーン位置に応じて、フレームごとのY座標を設定する
        self._y = self._calculate_attack_position(target_y)

        # 攻撃対象が存在しない場合は、すべてのフレームでお札画像を使用する
        if path is None:
            self._path = [None, None, None, None]
        # 攻撃対象が存在する場合は、前半はお札、後半は攻撃対象の画像を使用する
        else:
            self._path = [None, None, path, path]

    def _calculate_attack_position(self, y: int) -> list[int]:
        # 攻撃対象が存在しない場合は画面奥まで攻撃物を移動する
        if y == -1:
            return [1, 2, 4, 6]

        # 手前側の敵の場合は同じ位置に表示する
        elif y in [0, 1]:
            self._is_attack = False
            return [0, 0, 0, 0]
        elif y == 2:
            return [0, 0, 1, 1]
        elif y == 3:
            return [0, 1, 2, 2]
        elif y == 4:
            return [1, 2, 3, 3]
        elif y == 5:
            return [1, 3, 4, 4]
        elif y == 6:
            return [1, 3, 5, 5]

        self._is_attack = False
        return [0, 0, 0, 0]