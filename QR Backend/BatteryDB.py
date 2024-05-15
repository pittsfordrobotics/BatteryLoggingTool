import sqlite3


class Battery:
    def __init__(self, _id, percentage):
        self._id = _id
        self.percentage = percentage

    def get_id(self):
        return self._id


class BatteryDB:
    def __init__(self, db_file="batteries.db"):
        self.db_file = db_file
        conn = sqlite3.Connection(self.db_file)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS batteries (id INTEGER PRIMARY KEY, percentage INTEGER NOT NULL)")
        # should percentage (0-100) be an int or a float?
        self.batteries = cursor.execute("SELECT * FROM batteries").fetchall()
        conn.commit()
        conn.close()

    def add_battery(self, battery: Battery):
        self.batteries.append(battery)
        conn = sqlite3.Connection(self.db_file)
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO batteries (id, percentage) VALUES " +
                       # the "or ignore" is so it doesn't crash in case of accidental duplicates
                       f"({battery.get_id()}, {battery.percentage})")
        self.batteries = cursor.execute("SELECT * FROM batteries").fetchall()
        conn.commit()
        conn.close()
