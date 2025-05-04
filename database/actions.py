from datetime import datetime
import database

def doar_alimento():
    print("\n--- Doar Alimento ---")
    donor_name = input("Seu nome: ")
    food_type = input("Tipo de alimento: ")
    quantity = input("Quantidade (ex: 1kg, 5 unidades): ")
    expiry_date = input("Data de validade (ou 'N/A'): ")

    donation_id = database.add_donation(donor_name, food_type, quantity, expiry_date)
    print(f"\nDoação registrada com sucesso! ID: {donation_id}")

def ver_estoque():
    print("\n--- Estoque Disponível ---")
    available = database.get_available_donations()
    if not available:
        print("Nenhum item disponível no momento.")
        return False # Indica que não há estoque

    print("ID | Alimento       | Quantidade    | Validade      | Doador")
    print("---|----------------|---------------|---------------|---------------")
    for item in available:
        print(f"{item['id']:<3}| {item['food_type']:<14} | {item['quantity']:<13} | {item['expiry_date']:<13} | {item['donor_name']}")
    print("-" * 65)
    return True # Indica que há estoque

def solicitar_alimento():
    print("\n--- Solicitar Alimento ---")
    if not ver_estoque(): # Mostra o estoque antes de pedir ID
        return # Sai se não houver estoque

    try:
        donation_id_str = input("Digite o ID do alimento que deseja solicitar: ")
        donation_id = int(donation_id_str)
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return

    # Verifica se o ID é válido e disponível ANTES de pedir dados do solicitante
    donation = database.get_donation_by_id(donation_id)
    if not donation or donation['status'] != 'available':
        print(f"Erro: Doação com ID {donation_id} não encontrada ou não está disponível.")
        return

    # Se chegou aqui, o ID é válido, então pede os dados do solicitante
    print(f"\nSolicitando: {donation['food_type']} (Qtd: {donation['quantity']})")
    requester_name = input("Seu nome: ")
    requester_contact = input("Seu telefone/contato: ")
    requester_reason = input("Motivo da solicitação: ")

    success = database.register_donation_claim(donation_id, requester_name, requester_contact, requester_reason)

    if success:
        print("\nSolicitação registrada e alimento baixado do estoque com sucesso!")
    else:
        # Esta mensagem não deveria aparecer por causa da checagem prévia, mas é bom ter
        print("\nErro ao registrar a solicitação. O item pode ter sido pego por outra pessoa.")


def ver_historico():
    print("\n--- Histórico de Doações Concluídas ---")
    transactions = database.get_all_transactions()
    if not transactions:
        print("Nenhuma doação concluída registrada.")
        return

    print("ID | Alimento       | Qtd           | Doador        | Solicitante   | Contato       | Motivo                                 | Data")
    print("---|----------------|---------------|---------------|---------------|---------------|----------------------------------------|--------------------------")
    for t in transactions:
        # Limita o tamanho do motivo para não quebrar a tabela
        reason_short = (t['requester_reason'][:35] + '...') if len(t['requester_reason']) > 38 else t['requester_reason']
        # Formata data para melhor leitura
        try:
            completion_date_fmt = datetime.fromisoformat(t['completion_date']).strftime('%d/%m/%Y %H:%M')
        except:
            completion_date_fmt = t['completion_date'] # Se der erro, mostra como está

        print(f"{t['id']:<3}| {t['food_type']:<14} | {t['quantity']:<13} | {t['donor_name']:<13} | {t['requester_name']:<13} | {t['requester_contact']:<13} | {reason_short:<38} | {completion_date_fmt}")
    print("-" * 150) # Ajustar conforme a largura da linha formatada