from Domein.state import GameState

def progress_system(state, input_x, input_y, count):
    """
    ゲームの進行を管理する
    """
    # タイトル画面でタッチされた場合
    if state == GameState.TITLE and input_x == input_y == -1:
        return GameState.OP

    # オープニング画面を2秒表示したらゲーム画面へ遷移
    elif state == GameState.OP and count > 20:
        return GameState.STAGE

    # ゲーム画面を表示している間の処理
    elif state == GameState.STAGE:
        return GameState.STAGE

    # クリア画面でタッチされたらタイトル画面へ戻る
    elif state == GameState.CLEAR and input_x == input_y == -1:
        return GameState.TITLE