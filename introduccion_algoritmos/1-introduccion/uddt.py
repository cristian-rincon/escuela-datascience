"""
User Defined Data Type
"""
from dataclasses import dataclass


@dataclass
class Client:

    name: str
    id: str
    credit: float
    address: str


def main():

    user1 = Client("Cristian", "00001", 4400000, "Cr 1 nro 1 01")

    print(f'The client name is: {user1.name}')
    print(f'The client id is: {user1.id}')
    print(f'The client credit is: {user1.credit}')
    print(f'The client address is: {user1.address}')

    print(type(Client))


if __name__ == "__main__":
    main()
