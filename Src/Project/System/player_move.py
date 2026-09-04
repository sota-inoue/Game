from Domain.StageObject.player import Player, Player_Move_State_x, Player_Move_State_y, Player_Position_x, Player_Position_y

class PlayerMove:
    def __init__(self, width, height):

        # マス目のx座標
        self.X1 = width // 6
        self.X2 = width * 2 // 6
        self.X3 = width * 3 // 6
        self.X4 = width * 4 // 6
        self.X5 = width * 5 // 6
        
        # Y1 = 地面
        self.Y1 = height - (width // 20)
        # Y2 = ジャンプ時の最高到達点
        self.Y2 = self.Y1 - width // 10

        
        # プレイヤーのx方向の移動速度
        self.speed_x = (self.X2 - self.X1) // 5
        # プレイヤーのy方向の移動速度
        self.speed_y = (self.Y1 - self.Y2) // 10

    def update(self, player: Player) -> None:

        player_state_x = player.get_state_x()
        player_state_y = player.get_state_y()

        # 目標座標取得
        player_position_x = player.get_position_x()
        target_x = self.get_target_x(player_position_x)

        x = player.get_x()
        y = player.get_y()

        # -------------------------
        # X方向の移動処理
        # -------------------------

        if player_state_x == Player_Move_State_x.STAY:
            x = target_x

        # 横方向の状態がLEFTの場合、左方向へ移動する
        elif player_state_x == Player_Move_State_x.LEFT:
            # 一番左にいる場合は、これ以上左に移動できないため横移動を停止する
            if x <= self.X1:
                x = self.X1
                player.set_state_x(Player_Move_State_x.STAY)
            else:
                # プレイヤーを左方向へ移動させる
                x -= self.speed_x
                # 次の移動先に到達、または通り過ぎた場合
                if x <= target_x:
                    # 座標を次の移動先に補正する
                    x = target_x
                    # 横方向の移動状態を停止に戻す
                    player.set_state_x(Player_Move_State_x.STAY)
        
        # 横方向の状態がRIGHTの場合、右方向へ移動する
        elif player_state_x == Player_Move_State_x.RIGHT:
            # 一番右にいる場合は、これ以上右に移動できないため横移動を停止する
            if x >= self.X5:
                x = self.X5
                player.set_state_x(Player_Move_State_x.STAY)
            else:
                # プレイヤーを右方向へ移動させる
                x += self.speed_x
                # 次の移動先に到達、または通り過ぎた場合
                if x >= target_x:
                    # 座標を次の移動先に補正する
                    x = target_x
                    # 横方向の移動状態を停止に戻す
                    player.set_state_x(Player_Move_State_x.STAY)

        player.set_x(x)

        # -------------------------
        # Y方向の移動処理
        # -------------------------
        if player_state_y == Player_Move_State_y.STAY:
            y = self.Y1
        # 縦方向の状態がJUMPの場合、上方向へ移動する
        elif player_state_y == Player_Move_State_y.JUMP:
            # プレイヤーを上方向へ移動させる
            y -= self.speed_y
        
            # ジャンプの頂点に到達、または通り過ぎた場合
            if y <= self.Y2:
                # 座標をジャンプの頂点に補正する
                y = self.Y2
                # 縦方向の状態を下降状態に変更する
                player.set_state_y(Player_Move_State_y.DOWN)
        
        # 縦方向の状態がDOWNの場合、下方向へ移動する
        elif player_state_y == Player_Move_State_y.DOWN:
            # プレイヤーを下方向へ移動させる
            y += self.speed_y
            # 地面の位置に到達、または通り過ぎた場合
            if y >= self.Y1:
                # 座標を地面の位置に補正する
                y = self.Y1
                # 縦方向の状態を停止状態に戻す
                player.set_state_y(Player_Move_State_y.STAY)

        player.set_y(y)

    def get_target_x(self, player_position_x: Player_Position_x) -> int:
        if player_position_x == Player_Position_x.X1:
            return self.X1
        elif player_position_x == Player_Position_x.X2:
            return self.X2
        elif player_position_x == Player_Position_x.X3:
            return self.X3
        elif player_position_x == Player_Position_x.X4:
            return self.X4
        elif player_position_x == Player_Position_x.X5:
            return self.X5
        else:
            raise ValueError("Invalid player position_x")