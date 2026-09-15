from enum import Enum, auto

# ゲーム全体の進行状態
class GamePhase(Enum):
    TITLE = auto()
    OPENING = auto()
    STAGE = auto()
    GAMEOVER = auto()
    CLEAR = auto()
    ENDING = auto()


# タイトル画面の選択状態
class TitleSceneSelection(Enum):
    START = auto()
    SETTING = auto()
    EXIT = auto()


# オープニング画面の進行状態
class OpeningPage(Enum):
    PAGE_1 = auto()
    PAGE_2 = auto()
    PAGE_3 = auto()


# ゲームオーバー画面の選択状態
class GameOverSceneSelection(Enum):
    CONTINUE = auto()
    TITLE = auto()


# クリア画面の選択状態
class GameClearSceneSelection(Enum):
    NEXT = auto()
    TITLE = auto()


# 現在のステージ
class StageNumber(Enum):
    STAGE_1 = auto()
    STAGE_2 = auto()
    STAGE_3 = auto()


# ゲームの進行に関するフラグを保持するクラス
class GameFlag:
    def __init__(self):
        """各画面・ゲーム進行の状態"""
        self._game_phase: GamePhase = GamePhase.TITLE
        self._title_selection: TitleSceneSelection = TitleSceneSelection.START
        self._opening_page: OpeningPage = OpeningPage.PAGE_1
        self._gameover_selection: GameOverSceneSelection = GameOverSceneSelection.CONTINUE
        self._gameclear_selection: GameClearSceneSelection = GameClearSceneSelection.NEXT
        self._stage_number: StageNumber = StageNumber.STAGE_1

        """ゲーム進行の判定に使用するフラグ"""
        # 画面がタッチされたか
        self._is_gameclear: bool = False
        # ゲームオーバー条件を満たしているか
        self._is_gameover: bool = False
        # 初回プレイか
        self._is_first_play: bool = True


    # 各フラグを初期状態に戻す
    def reset(self) -> None:
        self._game_phase = GamePhase.TITLE
        self._title_selection = TitleSceneSelection.START
        self._opening_page = OpeningPage.PAGE_1
        self._gameover_selection = GameOverSceneSelection.CONTINUE
        self._gameclear_selection = GameClearSceneSelection.NEXT
        self._stage_number = StageNumber.STAGE_1
        self._is_gameclear = False
        self._is_gameover = False

    # GamePhaseのGetterとSetter
    def get_game_phase(self) -> GamePhase:
        return self._game_phase
    
    def set_game_phase(self, state: GamePhase) -> None:
        if not isinstance(state, GamePhase):
            raise TypeError(f"受け取った型: {type(state).__name__} : GamePhase型を指定してください。")
        self._game_phase = state

    # TitleSceneSelectionのGetterとSetter
    def get_title_selection(self) -> TitleSceneSelection:
        return self._title_selection

    def set_title_selection(self, state: TitleSceneSelection) -> None:
        if not isinstance(state, TitleSceneSelection):
            raise TypeError(f"受け取った型: {type(state).__name__} : TitleSceneSelection型を指定してください。")
        self._title_selection = state

    # OpeningPageのGetterとSetter
    def get_opening_page(self) -> OpeningPage:
        return self._opening_page

    def set_opening_page(self, state: OpeningPage) -> None:
        if not isinstance(state, OpeningPage):
            raise TypeError(f"受け取った型: {type(state).__name__} : OpeningPage型を指定してください。")
        self._opening_page = state

    # GameOverSceneSelectionのGetterとSetter
    def get_gameover_selection(self) -> GameOverSceneSelection:
        return self._gameover_selection

    def set_gameover_selection(self, state: GameOverSceneSelection) -> None:
        if not isinstance(state, GameOverSceneSelection):
            raise TypeError(f"受け取った型: {type(state).__name__} : GameOverSceneSelection型を指定してください。")
        self._gameover_selection = state

    # GameClearSceneSelectionのGetterとSetter
    def get_gameclear_selection(self) -> GameClearSceneSelection:
        return self._gameclear_selection

    def set_gameclear_selection(self, state: GameClearSceneSelection) -> None:
        if not isinstance(state, GameClearSceneSelection):
            raise TypeError(f"受け取った型: {type(state).__name__} : GameClearSceneSelection型を指定してください。")
        self._gameclear_selection = state
    
    # StageNumberのGetterとSetter
    def get_stage_number(self) -> StageNumber:
        return self._stage_number

    def set_stage_number(self, state: StageNumber) -> None:
        if not isinstance(state, StageNumber):
            raise TypeError(f"受け取った型: {type(state).__name__} : StageNumber型を指定してください。")
        self._stage_number = state

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