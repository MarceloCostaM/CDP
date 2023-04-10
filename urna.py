# Define a lista de candidatos
candidatos = ["João", "Maria", "Pedro"]

# Define uma variável para contar os votos
votos = [0, 0, 0]

# Função para mostrar a lista de candidatos
def listar_candidatos():
    print("Candidatos:")
    for i, candidato in enumerate(candidatos):
        print(f"{i+1}. {candidato}")

# Função para registrar um voto
def votar():
    listar_candidatos()
    voto = int(input("Digite o número do candidato desejado: "))
    if voto < 1 or voto > len(candidatos):
        print("Voto inválido!")
    else:
        votos[voto-1] += 1
        print("Voto registrado com sucesso!")

# Função para mostrar os resultados
def mostrar_resultados():
    print("Resultado da votação:")
    for i, candidato in enumerate(candidatos):
        print(f"{candidato}: {votos[i]} voto(s)")

# Loop principal
while True:
    print("\nUrna Eleitoral")
    print("1. Listar candidatos")
    print("2. Votar")
    print("3. Mostrar resultados")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        listar_candidatos()
    elif opcao == 2:
        votar()
    elif opcao == 3:
        mostrar_resultados()
    elif opcao == 4:
        break
    else:
        print("Opção inválida!")