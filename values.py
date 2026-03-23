from dataclasses import dataclass

@dataclass
class number:
    value: float

    def __repr__(self):
        return f"{self.value}"
    
