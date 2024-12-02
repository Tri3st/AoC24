class ReportItem:
    def __init__(self, rep_id ,num):
        self.id = rep_id
        self.num = num

    def __str__(self):
        return f"{self.id}:{self.num}"