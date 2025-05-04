from tinydb import TinyDB, Query, where
from datetime import datetime
import os

# Garante que a pasta db exista
if not os.path.exists('db'):
    os.makedirs('db')

db = TinyDB('db/food_data.json', indent=4) # indent=4 para facilitar leitura do JSON
donations_table = db.table('donations')
transactions_table = db.table('transactions')

def get_next_id(table):
    """Gera um ID simples incremental."""
    return len(table) + 1

def add_donation(donor_name, food_type, quantity, expiry_date):
    """Adiciona uma nova doação disponível."""
    donation_id = get_next_id(donations_table)
    donations_table.insert({
        'id': donation_id,
        'donor_name': donor_name,
        'food_type': food_type,
        'quantity': quantity,
        'expiry_date': expiry_date,
        'donation_date': datetime.now().isoformat(),
        'status': 'available'
    })
    return donation_id

def get_available_donations():
    """Retorna todas as doações com status 'available'."""
    Donation = Query()
    return donations_table.search(Donation.status == 'available')

def get_donation_by_id(donation_id):
    """Busca uma doação pelo seu ID."""
    Donation = Query()
    result = donations_table.search(Donation.id == donation_id)
    return result[0] if result else None

def update_donation_status(donation_doc_id, new_status):
    """Atualiza o status de uma doação pelo seu doc_id interno."""
    donations_table.update({'status': new_status}, doc_ids=[donation_doc_id])

def register_donation_claim(donation_id, requester_name, requester_contact, requester_reason):
    """Registra a transação e atualiza o status da doação."""
    donation = get_donation_by_id(donation_id)
    if donation and donation['status'] == 'available':
        # Loga a transação
        transaction_id = get_next_id(transactions_table)
        transactions_table.insert({
            'id': transaction_id,
            'donation_id': donation['id'],
            'food_type': donation['food_type'],
            'quantity': donation['quantity'],
            'donor_name': donation['donor_name'],
            'requester_name': requester_name,
            'requester_contact': requester_contact,
            'requester_reason': requester_reason,
            'completion_date': datetime.now().isoformat()
        })

        # Atualiza o status da doação original para 'donated'
        # TinyDB usa doc_id interno para updates
        donation_doc_id = donations_table.get(Query().id == donation_id).doc_id
        update_donation_status(donation_doc_id, 'donated')
        return True # Sucesso
    return False # Falha (não encontrado ou não disponível)


def get_all_transactions():
    """Retorna todo o histórico de transações."""
    return transactions_table.all()