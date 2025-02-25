import sys

def loading_bar(iteration, total, interval=100):
    if iteration % interval == 0 or iteration == total:
        porcentagem = (iteration / total) * 100
        barra = '#' * (iteration * 40 // total)
        sys.stdout.write(f'\r[{barra:<40}] {int(porcentagem)}%')
        sys.stdout.flush()
