
def map_updata(datas, data):
    # レーン2～7のデータをレーン1～6へ移動する
    i = 0
    while i < len(datas) - 1:
        datas[i] = datas[i + 1].copy()
        i += 1

    # 一番奥のレーン7に新しいマップデータを設定する
    datas[6] = data.copy()

    return datas
