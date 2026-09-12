from StageObject.player import Player
from StageObject.stage_object import StageObject
from Input.command_converter import Command

from Domain.game_flag import GameFlag, StageState

from System.sound_system import SoundSystem
from System.Map.map_system import Map
from System.Player.player_position import PlayerPosition
from System.Player.player_move import PlayerMove
from System.Player.player_hit_check import PlayerHitCheck
from System.Player.player_attack import PlayerAttack
from System.Player.attack_factory import AttackObjectFactory

from System.progress_system import ProgressSystem

class System:
    def __init__(self, width, height):
        self.sound = SoundSystem()
        self._map = Map(width, height)
        self.position = PlayerPosition()
        self.hit_check = PlayerHitCheck()
        self.attack = PlayerAttack()
        self.attack_factory = AttackObjectFactory(width, height)
        self.move = PlayerMove(width, height)

        self._progress = ProgressSystem()


    def player_locate_update(self, player: Player) -> None:
        self.move.update(player)

    def player_position_update(self, cmd: Command, player: Player) -> None:
        self.position.update(cmd, player)

    def player_hit_check(self, count: int, player: Player, objects: list[list[StageObject | None]] ) -> None:
        self.hit_check.update(count, player, objects)

    def map_update(self, count: int, objects: list[list[StageObject | None]], state: StageState) -> bool:
        return self._map.stage_update(objects, count, state)

    def object_hit_check(self,  objects: list[list[StageObject | None]] ) -> None:
        self._map.object_hit_check(objects)

    def player_attack(self, player: Player, objects: list[list[StageObject | None]]) -> list[StageObject | None]:
        obj = self.attack.attack(player, objects)
        return self.attack_factory.get_attack_object(player, obj)
    

    def title_update(self, command: Command, flag: GameFlag) -> bool:
        return self._progress.title_update(command, flag)

    def opening_update(self, command: Command, flag: GameFlag) -> None:
        self._progress.opening_update(command, flag)

    def gameclear_update(self, command: Command, flag: GameFlag) -> None:
        self._progress.clear_update(command, flag)

    def gameover_update(self, command: Command, flag: GameFlag) -> None:
        self._progress.gameover_update(command, flag)

    def stage_update(self, flag: GameFlag) -> None:
        self._progress.stage_update(flag)



    def play_PushButton(self) -> None:
        self.sound.play_se_push_button()

    def play_TitleBGM(self) -> None:
        self.sound.play_bgm_title()

    def set_se_volume(self, volume: int) -> None:
        self.sound.set_se_volume(volume)

    def set_bgm_volume(self, volume: int) -> None:
        self.sound.set_bgm_volume(volume)
