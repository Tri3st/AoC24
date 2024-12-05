class Order:
    """
    'page' always come before page Y, Z and A
    ordering is {
                    page: X,
                    page2: [Y, Z, A]
    """
    def __init__(self,data):
        self.ordering = {}
        self.pages_lists = []
        self.calc(data)

    def calc(self, data):
        datas = data.split('\n\n')
        for datas2 in datas[0].split("\n"):
            print(datas2)
            page1, page2 = datas2.split('|')
            if int(page1) in self.ordering.keys():
                self.ordering[int(page1)].append(int(page2))
            else:
                self.ordering[int(page1)] = [int(page2)]
        for line in datas[1].split('\n'):
            self.pages_lists.append(int(line))