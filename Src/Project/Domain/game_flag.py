from enum import Enum, auto

# ゲーム全体の進行状態
class GameState(Enum):
    TITLE = auto()
    OPENING = auto()
    STAGE = auto()
    GAMEOVER = auto()
    CLEAR = auto()
    ENDING = auto()


# タイトル画面の選択状態
class TitleState(Enum):
    START = auto()
    SETTING = auto()
    EXIT = auto()


# オープニング画面の進行状態
class OpeningState(Enum):
    OPENING_PAGE1 = auto()
    OPENING_PAGE2 = auto()
    OPENING_PAGE3 = auto()
    OPENING_PAGE4 = auto()


# ゲームオーバー画面の選択状態
class GameOverState(Enum):
    CONTINUE = auto()
    TITLE = auto()


# クリア画面の選択状態
class ClearState(Enum):
    NEXT = auto()
    TITLE = auto()


# 現在のステージ
class StageState(Enum):
    STAGE1 = auto()
    STAGE2 = auto()
    STAGE3 = auto()


# ゲームの進行に関するフラグを保持するクラス
class GameFlag:
    def __init__(self):
        """各画面・ゲーム進行の状態"""
        self._game_state: GameState = GameState.TITLE
        self._title_state: TitleState = TitleState.START
        self._opening_state: OpeningState = OpeningState.OPENING_PAGE1
        self._gameover_state: GameOverState = GameOverState.CONTINUE
        self._clear_state: ClearState = ClearState.NEXT
        self._stage_state: StageState = StageState.STAGE1

        """ゲーム進行の判定に使用するフラグ"""
        # 画面がタッチされたか
        self._is_gameclear: bool = False
        # ゲームオーバー条件を満たしているか
        self._is_gameover: bool = False
        # 初回プレイか
        self._is_first_play: bool = True


    # 各フラグを初期状態に戻す
    def reset(self) -> None:
        self._game_state = GameState.TITLE
        self._title_state = TitleState.START
        self._opening_state = OpeningState.OPENING_PAGE1
        self._gameover_state = GameOverState.CONTINUE
        self._clear_state = ClearState.NEXT
        self._stage_state = StageState.STAGE1
        self._is_gameclear = False
        self._is_gameover = False

    # GameStateのGetterとSetter
    def get_game_state(self) -> GameState:
        return self._game_state
    
    def set_game_state(self, state: GameState) -> None:
        if not isinstance(state, GameState):
            raise TypeError(f"受け取った型: {type(state).__name__} : GameState型を指定してください。")
        self._game_state = state

    # TitleStateのGetterとSetter
    def get_title_state(self) -> TitleState:
        return self._title_state

    def set_title_state(self, state: TitleState) -> None:
        if not isinstance(state, TitleState):
            raise TypeError(f"受け取った型: {type(state).__name__} : TitleState型を指定してください。")
        self._title_state = state

    # OpeningStateのGetterとSetter
    def get_opening_state(self) -> OpeningState:
        return self._opening_state

    def set_opening_state(self, state: OpeningState) -> None:
        if not isinstance(state, OpeningState):
            raise TypeError(f"受け取った型: {type(state).__name__} : OpeningState型を指定してください。")
        self._opening_state = state

    # GameOverStateのGetterとSetter
    def get_gameover_state(self) -> GameOverState:
        return self._gameover_state

    def set_gameover_state(self, state: GameOverState) -> None:
        if not isinstance(state, GameOverState):
            raise TypeError(f"受け取った型: {type(state).__name__} : GameOverState型を指定してください。")
        self._gameover_state = state

    # ClearStateのGetterとSetter
    def get_clear_state(self) -> ClearState:
        return self._clear_state

    def set_clear_state(self, state: ClearState) -> None:
        if not isinstance(state, ClearState):
            raise TypeError(f"受け取った型: {type(state).__name__} : ClearState型を指定してください。")
        self._clear_state = state
    
    # StageStateのGetterとSetter
    def get_stage_state(self) -> StageState:
        return self._stage_state

    def set_stage_state(self, state: StageState) -> None:
        if not isinstance(state, StageState):
            raise TypeError(f"受け取った型: {type(state).__name__} : StageState型を指定してください。")
        self._stage_state = state

    # is_gameclearのGetterとSetter
    def get_is_gameclear(self) -> bool:
        return self._is_gameclear

    def set_is_gameclear(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"受け取った型: {type(value).__name__} : bool型を指定してください。")
        self._is_gameclear = value

    # is_gameoverのGetterとSetter
    def get_is_gameover(self) -> bool:
        return self._is_gameover

    def set_is_gameover(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"受け取った型: {type(value).__name__} : bool型を指定してください。")
        self._is_gameover = value

    # is_first_playのGetterとSetter
    def get_is_first_play(self) -> bool:
        return self._is_first_play

    def set_is_first_play(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise TypeError(f"受け取った型: {type(value).__name__} : bool型を指定してください。")
        self._is_first_play = value