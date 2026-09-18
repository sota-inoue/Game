def calculate_score(current_score: int, amount: int) -> int:
    """
    現在のスコアと加減算値を受け取り、計算後のスコアを返します。

    :param current_score: 現在のスコア
    :param amount: 加減算する値（正の数・負の数ともに指定可能）
    :return: 計算後の新しいスコア
    """
    return current_score + amount