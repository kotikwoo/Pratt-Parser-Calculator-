from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    number = 0
    plus = 1
    minus = 2
    multiply = 3
    divide = 4
    lparen = 5
    rparen = 6


@dataclass
class Token:
     type: TokenType
     value: any = None

     def __repr__(self):
          return self.type.name + (f":{self.value}" if self.value != None else "")

