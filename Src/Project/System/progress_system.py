from Domain.game_flag import (
    GameFlag,
    GameState,
    TitleState,
    OpeningState,
    GameOverState,
    ClearState,
    StageState,
)
from Input.command_converter import Command


class ProgressSystem:

    def title_update(self, command: Command, flag: GameFlag) -> bool:

        state = flag.get_title_state()
        is_first_play = flag.get_is_first_play()

        if state == TitleState.START:
            if command == Command.JUMP:
                # 初回プレイの場合はオープニングへ進む
                if is_first_play:
                    flag.set_is_first_play(False)
                    flag.set_opening_state(OpeningState.OPENING_PAGE1)
                    flag.set_game_state(GameState.OPENING)
                # 2回目以降はステージへ進む
                else:
                    flag.set_game_state(GameState.STAGE)
            elif command == Command.RIGHT:
                flag.set_title_state(TitleState.SETTING)

        elif state == TitleState.SETTING:
            if command == Command.RIGHT:
                flag.set_title_state(TitleState.EXIT)

            elif command == Command.LEFT:
                flag.set_title_state(TitleState.START)

        elif state == TitleState.EXIT:
            if command == Command.JUMP:
                return False

            elif command == Command.LEFT:
                flag.set_title_state(TitleState.SETTING)

        return True


    def opening_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_opening_state()

        if command != Command.NONE:

            if state == OpeningState.OPENING_PAGE1:
                flag.set_opening_state(OpeningState.OPENING_PAGE2)

            elif state == OpeningState.OPENING_PAGE2:
                flag.set_opening_state(OpeningState.OPENING_PAGE3)

            elif state == OpeningState.OPENING_PAGE3:
                flag.set_opening_state(OpeningState.OPENING_PAGE4)

            elif state == OpeningState.OPENING_PAGE4:
                flag.set_game_state(GameState.STAGE)


    def clear_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_clear_state()
        stage = flag.get_stage_state()

        # 最終ステージクリア後はエンディングへ
        if stage == StageState.STAGE3:
            flag.set_game_state(GameState.ENDING)

        if state == ClearState.NEXT:

            if command == Command.JUMP:
                # 次のステージを設定
                flag.set_stage_state(StageState(stage.value + 1))
                flag.set_game_state(GameState.STAGE)

            elif command == Command.RIGHT:
                flag.set_clear_state(ClearState.TITLE)

        elif state == ClearState.TITLE:

            if command == Command.JUMP:
                flag.set_game_state(GameState.TITLE)
                flag.set_clear_state(ClearState.NEXT)

            elif command == Command.LEFT:
                flag.set_clear_state(ClearState.NEXT)


    def gameover_update(self, command: Command, flag: GameFlag) -> None:

        state = flag.get_gameover_state()

        if state == GameOverState.CONTINUE:

            if command == Command.JUMP:
                flag.set_game_state(GameState.STAGE)
            elif command == Command.RIGHT:
                flag.set_gameover_state(GameOverState.TITLE)

        elif state == GameOverState.TITLE:

            if command == Command.JUMP:
                flag.set_game_state(GameState.TITLE)
                flag.set_gameover_state(GameOverState.CONTINUE)

            elif command == Command.LEFT:
                flag.set_gameover_state(GameOverState.CONTINUE)

    def stage_update(self, flag: GameFlag) -> None:

        is_gameclear = flag.get_is_gameclear()
        is_gameover = flag.get_is_gameover()

        if is_gameclear == True:
            flag.set_game_state(GameState.CLEAR)
            flag.set_is_gameclear(False)

        if is_gameover == True:
            flag.set_game_state(GameState.GAMEOVER)
            flag.set_is_gameover(False)
