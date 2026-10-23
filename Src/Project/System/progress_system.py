from State.game_flag import (
    GameFlag,
    GamePhase,
    TitleSceneSelection,
    GameOverSceneSelection,
    GameClearSceneSelection,
    StageNumber,
    PauseSceneSelection
)
from Input.command_converter import Command

from config import OPENING_MOVIE_COUNT, BOSS_INTRO_COUNT, BOSS_DEFEAT_COUNT, GAME_CLEAR_COUNT


class ProgressSystem:

    def progress_update(self, command: Command, flag: GameFlag, count: int) -> bool:
        phase = flag.get_game_phase()

        if command == Command.PAUSE and phase == GamePhase.STAGE:
            flag.set_game_phase(GamePhase.PAUSE)
            return True

        if phase == GamePhase.TITLE:
            return self._title_update(command, flag)
        elif phase == GamePhase.OPENING:
            self._opening_update(count, flag)
        elif phase == GamePhase.CLEAR:
            self._clear_update(count, flag)
        elif phase == GamePhase.STAGE:
            self._stage_update(flag)
        elif phase == GamePhase.GAMEOVER:
            self._gameover_update(command, flag)
        elif phase == GamePhase.PAUSE:
            self._pouse_update(command, flag)

        return True

    def _pouse_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_pause_selection()

        if state == PauseSceneSelection.RESUME:

            if command == Command.JUMP:
                flag.set_game_phase(GamePhase.STAGE)

            elif command == Command.RIGHT:
                flag.set_pause_selection(PauseSceneSelection.TITLE)

        elif state == PauseSceneSelection.TITLE:

            if command == Command.JUMP:
                flag.set_game_phase(GamePhase.TITLE)
                flag.set_pause_selection(PauseSceneSelection.RESUME)

            elif command == Command.LEFT:
                flag.set_pause_selection(PauseSceneSelection.RESUME)

    def _title_update(self, command: Command, flag: GameFlag) -> bool:

        state = flag.get_title_selection()
        is_first_play = flag.get_is_first_play()

        if state == TitleSceneSelection.START:
            if command == Command.JUMP:
                # 初回プレイの場合はオープニングへ進む
                if is_first_play:
                    flag.set_is_first_play(False)
                    flag.set_game_phase(GamePhase.OPENING)
                # 2回目以降はステージへ進む
                else:
                    flag.set_game_phase(GamePhase.STAGE)
            elif command == Command.RIGHT:
                flag.set_title_selection(TitleSceneSelection.EXIT)


        elif state == TitleSceneSelection.EXIT:
            if command == Command.JUMP:
                return False

            elif command == Command.LEFT:
                flag.set_title_selection(TitleSceneSelection.START)

        return True


    def _opening_update(self, count: int, flag: GameFlag) -> None:
        if count >= OPENING_MOVIE_COUNT:
            flag.set_game_phase(GamePhase.STAGE)


    def _clear_update(self, count: int, flag: GameFlag) -> None:

        state = flag.get_gameclear_selection()
        stage = flag.get_stage_number()

        if state == GameClearSceneSelection.CLEAR and count >= GAME_CLEAR_COUNT:
            flag.set_gameclear_selection(GameClearSceneSelection.MOVIE)
        elif stage == StageNumber.STAGE_1 and count >= GAME_CLEAR_COUNT + BOSS_INTRO_COUNT:
            flag.set_game_phase(GamePhase.STAGE)
            flag.set_stage_number(StageNumber.STAGE_2)
            flag.set_gameclear_selection(GameClearSceneSelection.CLEAR)
        elif stage == StageNumber.STAGE_2 and count >= GAME_CLEAR_COUNT + BOSS_DEFEAT_COUNT:
            flag.set_game_phase(GamePhase.ENDING)

                
            

    def _gameover_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_gameover_selection()

        if state == GameOverSceneSelection.CONTINUE:

            if command == Command.JUMP:
                flag.set_game_phase(GamePhase.STAGE)
            elif command == Command.RIGHT:
                flag.set_gameover_selection(GameOverSceneSelection.TITLE)

        elif state == GameOverSceneSelection.TITLE:

            if command == Command.JUMP:
                flag.set_game_phase(GamePhase.TITLE)
                flag.set_gameover_selection(GameOverSceneSelection.CONTINUE)

            elif command == Command.LEFT:
                flag.set_gameover_selection(GameOverSceneSelection.CONTINUE)

    def _stage_update(self, flag: GameFlag) -> None:

        is_gameclear = flag.get_is_gameclear()
        is_gameover = flag.get_is_gameover()

        if is_gameclear == True:
            flag.set_game_phase(GamePhase.CLEAR)
            flag.set_is_gameclear(False)

        if is_gameover == True:
            flag.set_game_phase(GamePhase.GAMEOVER)
            flag.set_is_gameover(False)