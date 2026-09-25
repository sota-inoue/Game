from Input.command_converter import Command
from Domain.player import Player, Player_Move_State_x, Player_Move_State_y, Player_Position_x, Player_Position_y, Player_Layout_x, Player_Layout_y

def player_move(player: Player) -> None:

    state_x = player.get_state_x()
    state_y = player.get_state_y()

    layout_x = player.get_layout_x()
    layout_y = player.get_layout_y()

    # X方向の移動
    if state_x == Player_Move_State_x.LEFT and layout_x != Player_Layout_x.X1_0:
        player.set_layout_x(Player_Layout_x(layout_x.value - 1))
    elif state_x == Player_Move_State_x.RIGHT and layout_x != Player_Layout_x.X5_0:
        player.set_layout_x(Player_Layout_x(layout_x.value + 1))

    # Y方向の移動
    if state_y == Player_Move_State_y.JUMP and layout_y != Player_Layout_y.Y3_0:
        player.set_layout_y(Player_Layout_y(layout_y.value + 1))
    elif state_y == Player_Move_State_y.DOWN and layout_y != Player_Layout_y.Y1_0:
        player.set_layout_y(Player_Layout_y(layout_y.value - 1))

def move_state_update(command: Command, player: Player) -> None:

    # 横方向の移動状態を更新する
    if command == Command.LEFT:
        player.set_state_x(Player_Move_State_x.LEFT)

    elif command == Command.RIGHT:
        player.set_state_x(Player_Move_State_x.RIGHT)

    # 地面にいる状態でジャンプ入力された場合、ジャンプを開始する
    elif (command == Command.JUMP and player.get_state_y() == Player_Move_State_y.STAY):
        player.set_state_y(Player_Move_State_y.JUMP)


def position_update(player: Player) -> None:

    layout_x = player.get_layout_x()

    # X方向のマス位置を更新する
    if layout_x == Player_Layout_x.X1_0:
        player.set_position_x(Player_Position_x.X1)
        player.set_state_x(Player_Move_State_x.STAY)

    elif layout_x == Player_Layout_x.X2_0:
        player.set_position_x(Player_Position_x.X2)
        player.set_state_x(Player_Move_State_x.STAY)

    elif layout_x == Player_Layout_x.X3_0:
        player.set_position_x(Player_Position_x.X3)
        player.set_state_x(Player_Move_State_x.STAY)

    elif layout_x == Player_Layout_x.X4_0:
        player.set_position_x(Player_Position_x.X4)
        player.set_state_x(Player_Move_State_x.STAY)

    elif layout_x == Player_Layout_x.X5_0:
        player.set_position_x(Player_Position_x.X5)
        player.set_state_x(Player_Move_State_x.STAY)

    layout_y = player.get_layout_y()

    # Y方向のマス位置を更新する
    if layout_y == Player_Layout_y.Y1_0:
        player.set_position_y(Player_Position_y.Y1)

        # 地面まで下降した場合はジャンプを終了する
        if player.get_state_y() == Player_Move_State_y.DOWN:
            player.set_state_y(Player_Move_State_y.STAY)

    elif layout_y == Player_Layout_y.Y2_0:

        # 下降中は地面側の当たり判定にする
        if player.get_state_y() == Player_Move_State_y.DOWN:
            player.set_position_y(Player_Position_y.Y1)

        # 上昇中は上側の当たり判定にする
        elif player.get_state_y() == Player_Move_State_y.JUMP:
            player.set_position_y(Player_Position_y.Y2)

    elif layout_y == Player_Layout_y.Y3_0:
        # 最高地点では上側の当たり判定にする
        player.set_position_y(Player_Position_y.Y2)

        # 下降状態に切り替える
        player.set_state_y(Player_Move_State_y.DOWN)



        

