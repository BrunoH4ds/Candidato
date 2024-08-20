candidatos = [
    (1, 'isaias joga fofo', 'PT', 'Baianinho de moanga', 'Presidente', 18),
    (2, 'tiaguin', 'Novo', 'taxade', 'Presidente', 18),
    (3, 'Frango Bombeiro', 'PL', 'melsilva', 'Presidente', 23),
    (4, 'buscando o empoderavel', 'PMN', 'MIA', 'Presidente', 27),
    (5, 'advogado de deus', 'PP', 'MIAU', 'Prefeito', 29),
    (6, 'mister chefe', 'PDF', 'MIMTAXE', 'Prefeito', 37),
    (7, 'LULAO', 'PT', 'MESTRE DA TAXA', 'Chefe de estado', 98),
    (8, 'Captao Bolsonaro', 'PL', 'BISTECONE', 'Chefe de estado', 200),
    (9, 'Rei da XOXOTA', 'PSB', 'MARRYTADA', 'Chefe de estado', 400),
    (10, 'cirilo', 'FOL', 'maria joaquina', 'Presidente', 12)
             ] 

def eleitor():
    try:
        voto_id = int(input("\nDigite o ID do candidato que você deseja votar: "))
    except ValueError:
        print("ID deve ser um número inteiro.")
        return

    for candidato in candidatos:
        if voto_id == candidato[0]:  
            print(f"\nVoto Confirmado no Candidato:\nNome: {candidato[1]}\nPartido: {candidato[2]}\nVice: {candidato[3]}\nCargo: {candidato[4]}\nIdade: {candidato[5]}")
            return  

    print("ID", voto_id, "não é um candidato registrado")

def adicionar_candidato():
    id = len(candidatos) + 1
    nome = input('Digite o nome do candidato: ')

    if any(candidato[1] == nome for candidato in candidatos):
        print('Candidato já cadastrado')
        return

    partido = input('Digite o partido do candidato: ')
    vice = input('Digite o nome do vice: ')
    cargos = input('Digite os cargos do candidato: ')

    try:
        idade = int(input('Digite a idade do candidato: '))
    except ValueError:
        print('Idade deve ser um número inteiro.')
        return

    candidato = (id, nome, partido, vice, cargos, idade)
    candidatos.append(candidato)
    print('Candidato cadastrado com sucesso')

def sair_do_aplicativo():
    print("Fechando o aplicativo...")
    exit()

menu = {
    1: eleitor,
    2: adicionar_candidato,
    3: sair_do_aplicativo
}

while True:
    print("\nMenu Principal:")
    print("1. Votar")
    print("2. Adicionar candidato")
    print("3. Sair do aplicativo")
    try:
        opcao = int (input("Escolha uma opção (1/2/3): "))
        
    except ValueError:
        print("A opção deve ser um número inteiro.")
        continue

    if opcao in menu:
        menu[opcao]()
    else:
        print("Opção inválida. Por favor, escolha uma das opcoes.")