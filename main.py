import os


from backend.serv import run as run_serv
from model.ai import Model


class App:
    def __init__(self):
        # self.current_dir = os.path.dirname(os.path.realpath(__file__))
        self.current_dir = os.getcwd()
        run_serv('0.0.0.0', 8000)
        self.model = Model()



if __name__ == "__main__":
    os.system("cls||clear")
    App()
