import sqlite3


class Battery:
    def __init__(self, _id, percentage):
        self._id = _id
        self.percentage = percentage

    def get_id(self):
        return self._id


class BatteryDB:
    def __init__(self):
        conn = sqlite3.Connection("batteries.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS batteries (id INTEGER PRIMARY KEY, percentage INTEGER NOT NULL)")
        # should percentage be an int or a float?
        self.batteries = cursor.execute("SELECT * FROM batteries").fetchall()
        conn.commit()
        conn.close()

    def add_battery(self, battery: Battery):
        self.batteries.append(battery)
        conn = sqlite3.Connection("batteries.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO batteries (id, percentage) VALUES " +
                       f"({battery.get_id()}, {battery.percentage})")
        self.batteries = cursor.execute("SELECT * FROM batteries").fetchall()
        conn.commit()
        conn.close()
