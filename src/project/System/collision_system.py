class CollisionSystem:
    EMPTY = 0
    ENEMY = 1
    OBSTACLE = 51

    def check_collision(self, stage_data, x, y):
        # xが0～4の範囲内か確認
        if x < 0 or x > 4:
            return False

        # xのマスにあるデータを取得
        object_number = stage_data[x]

        # 何もない場合
        if object_number == self.EMPTY:
            return False

        # 敵がいる場合
        if object_number == self.ENEMY:
            return True

        # 障害物の場合はyを確認
        if object_number == self.OBSTACLE:
            if y == 0:
                return True

            if y == 1:
                return False

        return False