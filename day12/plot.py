class Plot:
    def __init__(self, name, coords):
        self.name = name
        self.coords = [coords]
        self.area = 0
        self.perim = 0
        self.nr_of_plants = len(self.coords)
        self.price = 0
        self.calc()

    def calc(self):
        self.area = self.nr_of_plants

    def add_plant(self, coords):
        self.coords.append(coords)
        self.nr_of_plants = len(self.coords)
        self.calc()

    def plant_already_in_plot(self, coords):
        return coords in self.coords

    def set_perimeter(self, perim):
        self.perim = perim
        self.price = self.perim * self.area

    def __str__(self):
        return f"{self.name} : area - {self.area} perimeter {self.perim}"