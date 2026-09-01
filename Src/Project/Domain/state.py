from enum import Enum, auto


class Command(Enum):
    LEFT = auto()
    JUMP = auto()
    RIGHT = auto()
    STAY = auto()


class TitleState(Enum):
    START = auto()
    SETTING = auto()
    EXIT = auto()


class GameState(Enum):
    TITLE = auto()
    OP = auto()
    STAGE = auto()
    OVER = auto()
    CLEAR = auto()


class State:
    def __init__(self):
        self.game_state = GameState.TITLE
        self.game_command = Command.STAY
        self.title_state = TitleState.START

    # game_state
    def get_game_state(self):
        return self.game_state

    def set_game_state(self, game_state: GameState):
        if not isinstance(game_state, GameState):
            raise TypeError(
                f"game_stateにはGameState型を指定してください。"
                f"受け取った値: {game_state}、型: {type(game_state).__name__}"
            )
        if self.game_state != game_state:
            self.game_state = game_state

    # game_command
    def get_game_command(self):
        return self.game_command

    def set_game_command(self, game_command: Command):
        if not isinstance(game_command, Command):
            raise TypeError(
                f"game_commandにはCommand型を指定してください。"
                f"受け取った値: {game_command}、型: {type(game_command).__name__}"
            )
        self.game_command = game_command

    # title_state
    def get_title_state(self):
        return self.title_state

    def set_title_state(self, title_state: TitleState):
        if not isinstance(title_state, TitleState):
            raise TypeError(
                f"title_stateにはTitleState型を指定してください。"
                f"受け取った値: {title_state}、型: {type(title_state).__name__}"
            )
        self.title_state = title_state


