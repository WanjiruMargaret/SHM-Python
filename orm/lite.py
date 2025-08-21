import sqlite3

class LITE:
    def __init__(self):
        # FIXED: use forward slashes instead of backslashes
        db_path = "C:/Users/SGM/Phase3/SHM-Python/orm/database.db"
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        # row 

    def lite_query(self, query, params=()):
        cur = self.conn.cursor()
        cur.execute(query, params)

        result = None
        try:
            result = cur.fetchall()
        except Exception:
            pass

        self.conn.commit()
        cur.close()
        return result
