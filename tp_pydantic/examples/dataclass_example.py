from dataclasses import dataclass

@dataclass
class PersonDC:
    name: str
    age: int
p = PersonDC("amin", "22")
print(p)
