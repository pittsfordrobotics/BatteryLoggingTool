import sqlite3


class Battery:
    def __init__(self, _id, name, percentage, num_cycles):
        self._id = _id
        self.name = name
        self.percentage = percentage
        self.num_cycles = num_cycles

    def __init__(self, sql_input):
        self._id = sql_input[0]
        self.name = sql_input[1]
        self.percentage = sql_input[2]
        self.num_cycles = sql_input[3]

    def get_id(self):
        return self._id
    
class BatteryData:
    def __init__(self, battery: Battery, is_charged: bool, percentage: int, voltage: float, load_voltage: float):
        self.battery = battery
        self.is_charged = is_charged
        self.percentage = percentage
        self.voltage = voltage
        self.load_voltage = load_voltage
        self.battery_id = battery.get_id()

class BatteryDB:
    def __init__(self):
        conn = sqlite3.Connection("batteries.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS batteries (id INTEGER PRIMARY KEY, name STRING, percentage INTEGER NOT NULL, num_cycles INTEGER NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS batteries_data (data_id INTEGER PRIMARY KEY, battery_id INTEGER NOT NULL, cycle_num INTEGER NOT NULL, is_charged BOOLEAN NOT NULL, percentage INTEGER NOT NULL, voltage FLOAT NOT NULL, load_voltage FLOAT NOT NULL)")
        # should percentage be an int or a float?
        self.batteries = cursor.execute("SELECT * FROM batteries").fetchall()
        conn.commit()
        conn.close()

    def add_battery(self, battery: Battery):
        conn = sqlite3.Connection("batteries.db")
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO batteries (id, name, percentage, num_cycles) VALUES " +
                       f"({battery.get_id()}, {battery.name}, {battery.percentage}, {battery.num_cycles})")
        self.batteries = [Battery(t) for t in cursor.execute("SELECT * FROM batteries").fetchall()]
        print(self.batteries)
        conn.commit()
        conn.close()

    def add_battery_data(self, battery_data: BatteryData):
        battery_id = battery_data.battery_id
        conn = sqlite3.Connection("batteries.db")
        cursor = conn.cursor()
        current_battery = Battery(cursor.execute("SELECT * FROM batteries WHERE id="+ str(battery_id) +"").fetchall()[0])
        print(current_battery)
        #do stuff here
        cursor.execute("UPDATE batteries (id, name, percentage, num_cycles) VALUES " +
                       f"({current_battery.get_id()}, {current_battery.name}, {current_battery.percentage}, {current_battery.num_cycles})")
        self.batteries = [Battery(t) for t in cursor.execute("SELECT * FROM batteries").fetchall()]
        conn.commit()
        conn.close()
    
    def get_battery(self, _id: int):
        return self.batteries[_id]
