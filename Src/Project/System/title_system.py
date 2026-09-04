from Domain.state import TitleState, Command

class TitleSystem:
    def update(self, cmd: Command, state: TitleState) -> TitleState:
        if state == TitleState.START:
            if cmd == Command.JUMP:
                return TitleState.START_DECIDE
            elif cmd == Command.RIGHT:
                return TitleState.SETTING
        elif state == TitleState.SETTING:
            if cmd == Command.LEFT:
                return TitleState.START
            elif cmd == Command.JUMP:
                return TitleState.SETTING_DECIDE
            elif cmd == Command.RIGHT:
                return TitleState.EXIT
        elif state == TitleState.EXIT:
            if cmd == Command.LEFT:
                return TitleState.SETTING
            elif cmd == Command.JUMP:
                return TitleState.EXIT_DECIDE

        return state
