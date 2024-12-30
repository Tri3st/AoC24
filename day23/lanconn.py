class LanConn:
    def __init__(self, name, conn):
        self.name = name
        self.conn = conn

    def __str__(self):
        return f"{self.name} - {self.conn}"