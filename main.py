from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Literal
from tinydb import TinyDB


@dataclass
class Todo:
    task: str   
    owner: str
    status: Literal['done', 'todo'] = 'todo'

    def as_dict(self):
        return asdict(self)

#Dados do BD
t1 = Todo('buy coffee', 'Mateus', 'todo')    
t2 = Todo('Walk the dog', 'Mateus')    

#Criação e execução do BD
db_path = Path(__file__).parent / 'db.json'
db = TinyDB(db_path, indent=4)

#Limpa os dados repetidos
db.truncate()

#2 formas diferentes de inserir o dados do t1 e t2
index_1 = db.insert(t1.as_dict())
#forma 2 por empacotamento
index_2, index3 = db.insert_multiple(
    [t1.as_dict(), t2.as_dict()])

#Remover dados por index
db.remove(doc_ids=[2])

print(index_1)