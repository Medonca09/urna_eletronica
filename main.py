from database import tabelas
from models import registrar_candidato, listar_candidatos, registrar_eleitor, verificar_eleitor, registrar_voto, contar_votos, buscar_candidato_por_numero

def menu():
    print("\nMenu Principal")
    print("1. Registrar candidatos")
    print("2. Iniciar votação")
    print("3. Contar votos e exibir resultados")
    print("4. Sair")

def registrar_candidatos_eletivos():
    while True:
        nome = input("Nome do candidato: ").strip()
        cargo = input("Cargo disputado: ").strip()
        try:
            numero = int(input("Número do candidato: "))
        except ValueError:
            print("Número inválido. Tente novamente.")
            continue

        registrar_candidato(nome, cargo, numero)
        print(f"Candidato {nome} ({cargo}) com número {numero} registrado com sucesso.")
        continuar = input("Deseja cadastrar outro candidato? (s/n): ").strip().lower()
        if continuar != 's':
            break

def votar():
    eleitor_id = input("Digite seu ID de eleitor: ").strip()

    if verificar_eleitor(eleitor_id):
        print("Você já votou. Acesso negado.")
        return

    candidatos = listar_candidatos()
    if not candidatos:
        print("Nenhum candidato registrado para votação.")
        return

    print("\nCandidatos disponíveis:")
    for candidato in candidatos:
        print(f"Número: {candidato[3]} - Nome: {candidato[1]} ({candidato[2]})")

    try:
        numero = int(input("Digite o número do candidato para votar: "))
        candidato_id = buscar_candidato_por_numero(numero)
        if candidato_id:
            registrar_voto(candidato_id)
            registrar_eleitor(eleitor_id)
            print("Voto registrado com sucesso!")
        else:
            print("Número inválido. Tente novamente.")
    except ValueError:
        print("Erro ao registrar o voto. Certifique-se de digitar um número válido.")

def exibir_resultados():
    resultados = contar_votos()
    if not resultados:
        print("Nenhum voto registrado ainda.")
        return

    print("\nResultados:")
    for resultado in resultados:
        print(f"Número: {resultado[1]} - Nome: {resultado[0]}: {resultado[2]} votos")

def main():
    tabelas()
    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == '1':
            registrar_candidatos_eletivos()
        elif opcao == '2':
            votar()
        elif opcao == '3':
            exibir_resultados()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
