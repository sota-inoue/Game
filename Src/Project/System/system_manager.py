from StageObject.player import Player
from StageObject.stage_object import StageObject
from Domain.state import Command, TitleState

from System.title_system import TitleSystem

from System.sound_system import SoundSystem
from System.Map.map_system import Map
from System.Player.player_position import PlayerPosition
from System.Player.player_move import PlayerMove
from System.Player.player_hit_check import PlayerHitCheck
from System.Player.player_attack import PlayerAttack
from System.Player.attack_factory import AttackObjectFactory

class System:
    def __init__(self, width, height):
        self.sound = SoundSystem()
        self._map = Map(width, height)
        self.position = PlayerPosition()
        self.hit_check = PlayerHitCheck()
        self.attack = PlayerAttack()
        self.attack_factory = AttackObjectFactory(width, height)
        self.move = PlayerMove(width, height)

        self.title = TitleSystem()


    def player_locate_update(self, player: Player) -> None:
        self.move.update(player)

    def player_position_update(self, cmd: Command, player: Player) -> None:
        self.position.update(cmd, player)

    def player_hit_check(self, count: int, player: Player, objects: list[list[StageObject | None]] ) -> None:
        self.hit_check.update(count, player, objects)

    def map_update(self, count: int, objects: list[list[StageObject | None]] ) -> None:
        self._map.map_update(objects, count)

    def player_attack(self, player: Player, objects: list[list[StageObject | None]]) -> list[StageObject | None]:
        obj = self.attack.attack(player, objects)
        return self.attack_factory.get_attack_object(player, obj)
    

    def title_update(self, cmd: Command, state: TitleState) -> TitleState:
        return self.title.update(cmd, state)

    def play_PushButton(self) -> None:
        self.sound.play_se_push_button()

    def play_TitleBGM(self) -> None:
        self.sound.play_bgm_title()

    def set_se_volume(self, volume: int) -> None:
        self.sound.set_se_volume(volume)

    def set_bgm_volume(self, volume: int) -> None:
        self.sound.set_bgm_volume(volume)
