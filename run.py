import os
from caixeiro_viajante.main import App

BASEDIR = os.getcwd()
PATH = os.path.join(BASEDIR, 'caixeiro_viajante', 'data', 'coordenadas.csv')

def main():
    app = App(PATH, 'Curitiba', 'Foz do Iguaçu')
    app.run()

if __name__ == '__main__':
    main()