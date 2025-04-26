from dataclasses import dataclass
from typing import Literal


@dataclass
class Todo:
    task: str   
    owner: str
    status: Literal['done', 'todo'] = 'todo'

t1 = Todo()    