import actions

def main_menu():
    """Exibe o menu principal e retorna a escolha do usuário."""
    print("\n===== Sistema de Doação de Alimentos v0.1 =====")
    print("1. Doar Alimentos")
    print("2. Ver Estoque Disponível")
    print("3. Solicitar Alimentos do Estoque")
    print("4. Ver Histórico de Doações Concluídas")
    print("0. Sair")
    choice = input("Escolha uma opção: ")
    return choice

if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == '1':
            actions.doar_alimento()
        elif choice == '2':
            actions.ver_estoque()
        elif choice == '3':
            actions.solicitar_alimento()
        elif choice == '4':
            actions.ver_historico()
        elif choice == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar...") # Pausa para o usuário ler a saída