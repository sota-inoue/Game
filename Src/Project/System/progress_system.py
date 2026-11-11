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


def pouse_update(command: Command, flag: GameFlag) -> None:

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


def title_update(command: Command, flag: GameFlag) -> bool:

    state = flag.get_title_selection()

    if state == TitleSceneSelection.START:
        if command == Command.JUMP:
            flag.set_game_phase(GamePhase.STAGE)
        elif command == Command.RIGHT:
            flag.set_title_selection(TitleSceneSelection.EXIT)

    elif state == TitleSceneSelection.EXIT:
        if command == Command.JUMP:
            return False
        elif command == Command.LEFT:
            flag.set_title_selection(TitleSceneSelection.START)

    return True

                
            

def gameover_update(command: Command, flag: GameFlag) -> None:

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
