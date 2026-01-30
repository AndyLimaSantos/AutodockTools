import os
import subprocess

# Pastas-alvo dentro da pasta atual com os compostos que precisamos analizar
pastas = ["pasta 1° compost0","pasta 2° compost0","pasta 3° compost0",]

# Comandos a executar em cada pasta
comando1 = "autogrid4 -p grid.gpf -l grid.glg"
comando2 = "autodock4  -p dock.dpf -l dock.dlg"

# Caminho da pasta atual (onde o script está rodando)
pasta_mae = os.getcwd()

for pasta in pastas:
    caminho = os.path.join(pasta_mae, pasta)
    print(f"\nEntrando na pasta: {caminho}")
    
    if os.path.isdir(caminho):
        # Executa o primeiro comando
        resultado1 = subprocess.run(comando1, shell=True, cwd=caminho, capture_output=True, text=True)
        print("Saída do comando 1:")
        print(resultado1.stdout)

        # Executa o segundo comando
        resultado2 = subprocess.run(comando2, shell=True, cwd=caminho, capture_output=True, text=True)
        print("Saída do comando 2:")
        print(resultado2.stdout)
    else:
        print(f"A pasta {pasta} não foi encontrada.")

