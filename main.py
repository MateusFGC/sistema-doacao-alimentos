from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Literal
from tinydb import TinyDB, Query


@dataclass
class Todo:
    task: str   
    owner: str
    status: Literal['done', 'todo'] = 'todo'

    def as_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data):
        return Todo(**data)

#Dados do BD
t1 = Todo('buy coffee', 'Mateus', 'todo')    
t2 = Todo('Walk the dog', 'Mateus')    

#Criação e execução do BD
db_path = Path(__file__).parent / 'db.json'
db = TinyDB(db_path, indent=4)

#Limpa a base de dados repetidas
db.truncate()

#Inserir os dados por empacotamento
index_1, index2 = db.insert_multiple(
    [t1.as_dict(), t2.as_dict()])

#Remover dados por index
db.remove(doc_ids=[])

#atualizar qualquer dados dentro do BD, neste caso altero a tarefa task
db.update(
    {'task': 'Buy more coffe'},
          #obs: como eu estou mandando no plural  doc_ids  preciso enviar mais que um indice oc_ids=1, 2, 3 no caso que irei mandar 1 só, mandei um interavel em colchetes []
          doc_ids=[1])

#Pegar os dados
TodoQuery = Query()
print(
    db.search(
        #Filtre e busque informação a partir dos nomes dos dados
        #No .owner. pode alterar pelo nome do dados como task ou status
        #No search() basta apenas colocar qual dados vc procura e ele retornarar o dicionario inteiro
        #Forma 2 .owner == 'Mateus'
        TodoQuery.owner.search("Mateus")
    )
)