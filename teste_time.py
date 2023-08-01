# meu_codigo.py

import time

@profile
def minha_funcao():
    for i in range(5):
        time.sleep(1)
        print("Linha", i)

if __name__ == "__main__":
    minha_funcao()


# kernprof -l -v meu_codigo.py
# pip install line-profiler

