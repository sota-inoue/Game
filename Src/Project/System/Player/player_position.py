from Domain.state import Command
from StageObject.player import Player, Player_Move_State_x, Player_Move_State_y, Player_Position_x, Player_Position_y

class PlayerPosition:

    def __init__(self):
        self.is_jumping = False
        self.jump_count = 0
        self.jump_pattern = (
            Player_Position_y.Y1,
            Player_Position_y.Y2,
            Player_Position_y.Y2,
            Player_Position_y.Y1
        )

    def update(self, command: Command, player: Player) -> None:

        if command == Command.LEFT:
            player.set_state_x(Player_Move_State_x.LEFT)
        elif command == Command.RIGHT:
            player.set_state_x(Player_Move_State_x.RIGHT)
        elif command == Command.JUMP and player.get_state_y() == Player_Move_State_y.STAY:
            player.set_state_y(Player_Move_State_y.JUMP)
            self.is_jumping = True
            self.jump_count = 0

        position_x = player.get_position_x()
        next_position_x = self.get_next_position_x(command, position_x)
        next_position_y = self.get_next_position_y()
        player.set_position_x(next_position_x)
        player.set_position_y(next_position_y)

        # self.debug_log(command, player)


    def get_next_position_x(self, command: Command, player_position_x: Player_Position_x) -> Player_Position_x:
        if command == Command.LEFT:
            if player_position_x == Player_Position_x.X1:
                return Player_Position_x.X1
            elif player_position_x == Player_Position_x.X2:
                return Player_Position_x.X1
            elif player_position_x == Player_Position_x.X3:
                return Player_Position_x.X2
            elif player_position_x == Player_Position_x.X4:
                return Player_Position_x.X3
            elif player_position_x == Player_Position_x.X5:
                return Player_Position_x.X4
            else:
                raise ValueError("Invalid player position_x")
        elif command == Command.RIGHT:
            if player_position_x == Player_Position_x.X1:
                return Player_Position_x.X2
            elif player_position_x == Player_Position_x.X2:
                return Player_Position_x.X3
            elif player_position_x == Player_Position_x.X3:
                return Player_Position_x.X4
            elif player_position_x == Player_Position_x.X4:
                return Player_Position_x.X5
            elif player_position_x == Player_Position_x.X5:
                return Player_Position_x.X5
            else:
                raise ValueError("Invalid player position_x")
        else:
            return player_position_x

    def get_next_position_y(self) -> Player_Position_y:
        if self.is_jumping == True:
            if self.jump_count < len(self.jump_pattern):
                next_position_y = self.jump_pattern[self.jump_count]
                self.jump_count += 1
            else:
                self.is_jumping = False
                self.jump_count = 0
                next_position_y = Player_Position_y.Y1
        else:
            next_position_y = Player_Position_y.Y1

        return next_position_y

    def debug_log(self, command: Command, player: Player) -> None:
        position_x = player.get_player_position_x()
        position_y = player.get_player_position_y()

        print(
            f" command = {command.name} "
            f": position = ({position_x.name}, {position_y.name})"
        )