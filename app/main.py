import toga
from const import *

class Pokedex(toga.App):
    def __init__(self, title, id):
        toga.App.__init__(self, title, id)

        self.title = title
        self.size = (WIDTH, HEIGHT)

        self.heading = ['Name']
        self.data = ['Python', 'Ruby']

        self.create_elements()

    def startup(self):
        self.main_window = toga.MainWindow('main',title=self.title, size=(self.size))

        box = toga.Box()

        split = toga.SplitContainer()
        split.content = [self.table, box]

        self.main_window.content = split

        self.main_window.show()

    def create_elements(self):
        self.create_table()


    def create_table(self):
        self.table = toga.Table(self.heading, data=self.data, on_select = self.select_element)


    #Callback

    def select_element(self, widget, row):
        print(row.name)

if __name__ == '__main__':
    pokedex = Pokedex('Pokedex', 'com.tutankadev.pokedex')
    pokedex.main_loop()