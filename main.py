import os, sys


from backend.serv import run as run_serv
from model.ai import Model



class App:
    def __init__(self):
        self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.current_dir = os.getcwd()
        self.model = Model()
        if '--train' in sys.argv:
            self.model.train(20, self.current_dir)
        else:
            self.model.load(os.path.join(self.current_dir, '...'))
        run_serv('0.0.0.0', 8000, self.model.process)



if __name__ == "__main__":
    os.system("cls||clear")
    App()
