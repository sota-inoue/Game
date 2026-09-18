from Domain.game_flag import (
    GameFlag,
    GamePhase,
    TitleSceneSelection,
    OpeningPage,
    GameOverSceneSelection,
    GameClearSceneSelection,
    StageNumber,
)
from Input.command_converter import Command


class ProgressSystem:

    def title_update(self, command: Command, flag: GameFlag) -> bool:

        state = flag.get_title_selection()
        is_first_play = flag.get_is_first_play()

        if state == TitleSceneSelection.START:
            if command == Command.JUMP:
                # 初回プレイの場合はオープニングへ進む
                if is_first_play:
                    flag.set_is_first_play(False)
                    flag.set_opening_page(OpeningPage.PAGE_1)
                    flag.set_game_phase(GamePhase.OPENING)
                # 2回目以降はステージへ進む
                else:
                    flag.set_game_phase(GamePhase.STAGE)
            elif command == Command.RIGHT:
                flag.set_title_selection(TitleSceneSelection.SETTING)

        elif state == TitleSceneSelection.SETTING:
            if command == Command.RIGHT:
                flag.set_title_selection(TitleSceneSelection.EXIT)

            elif command == Command.LEFT:
                flag.set_title_selection(TitleSceneSelection.START)

        elif state == TitleSceneSelection.EXIT:
            if command == Command.JUMP:
                return False

            elif command == Command.LEFT:
                flag.set_title_selection(TitleSceneSelection.SETTING)

        return True


    def opening_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_opening_page()

        if command != Command.NONE:

            if state == OpeningPage.PAGE_1:
                flag.set_opening_page(OpeningPage.PAGE_2)

            elif state == OpeningPage.PAGE_2:
                flag.set_opening_page(OpeningPage.PAGE_3)

            elif state == OpeningPage.PAGE_3:
                flag.set_game_phase(GamePhase.STAGE)



    def clear_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_gameclear_selection()
        stage = flag.get_stage_number()

        # 最終ステージクリア後はエンディングへ
        if stage == StageNumber.STAGE_3:
            flag.set_game_phase(GamePhase.ENDING)

        if state == GameClearSceneSelection.NEXT:

            if command == Command.JUMP:
                # 次のステージを設定
                flag.set_stage_number(StageNumber(stage.value + 1))
                flag.set_game_phase(GamePhase.STAGE)

            elif command == Command.RIGHT:
                flag.set_gameclear_selection(GameClearSceneSelection.TITLE)

        elif state == GameClearSceneSelection.TITLE:

            if command == Command.JUMP:
                flag.set_game_phase(GamePhase.TITLE)
                flag.set_gameclear_selection(GameClearSceneSelection.NEXT)

            elif command == Command.LEFT:
                flag.set_gameclear_selection(GameClearSceneSelection.NEXT)


    def gameover_update(self, command: Command, flag: GameFlag) -> None:

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

    def stage_update(self, flag: GameFlag) -> None:

        is_gameclear = flag.get_is_gameclear()
        is_gameover = flag.get_is_gameover()

        if is_gameclear == True:
            flag.set_game_phase(GamePhase.CLEAR)
            flag.set_is_gameclear(False)

        if is_gameover == True:
            flag.set_game_phase(GamePhase.GAMEOVER)
            flag.set_is_gameover(False)