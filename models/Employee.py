class Employee:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f'The name is:',self.name)

    def count(self):
        return 45     