import datetime

def insert_query(start:str, finish:str, memo:str, create_at:datetime.datetime):
    """記録データをデータベースに保存

        start:出発地点名
        finish:到着地点名
        memo:メモ欄のデータ
        create_at:作成日時

        return: None
    """
    DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
    insert_row = {"start":start, "finish":finish, "memo":memo, "create_at":create_at.strftime(DATE_TIME_FORMAT)}
    query = f"INSERT INTO USER ({','.join(insert_row.keys())}) VALUES {tuple(insert_row.values())}"
    return query