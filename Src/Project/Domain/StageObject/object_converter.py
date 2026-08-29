from Domain.StageObject.enemy import Ojisan
from Domain.StageObject.obstacle import Banana

from Domain.StageObject.stage_object import StageObject


class ObjectConverter:
    def __init__(self):
        self._objects = {
            0: None,
            1: Ojisan,
            51: Banana
        }

    def convert(self,lists: list[int]) -> list[StageObject | None]:

        # 引数がlist型であるか確認する
        if not isinstance(lists, list):
            raise TypeError("listsはlist型で指定してください")

        objects = []

        # 数値データをオブジェクトへ変換する
        i = 0
        while i < len(lists):
            object_class = self._objects.get(lists[i])

            # 0の場合はNoneを追加する
            if object_class is None:
                objects.append(None)

            # 対応するクラスのインスタンスを生成する
            else:
                objects.append(object_class())

            i += 1

        return objects

        