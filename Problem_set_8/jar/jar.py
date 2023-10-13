import sys

class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")
        self._size = 0

    # __str__ returns cookie emojis
    def __str__(self):
        return f"{'🍪'*self._size}"

    # deposit command adds n cookies to the jar
    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        self._size += n

    # withdraw command removes n cookies from the jar
    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies")
        else:
            self._size -= n

    # property setters & getters
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    # get and perform user command
    @classmethod
    def get_command(cls):
        command = input("Choose your command: (J)ar  (D)eposit / (W)ithdraw / (C)apacity / (S)ize) / (E)xit! ")
        return command


def main():

    jar = Jar()

    while(True):
        command = jar.get_command()
        match command:
            # Jar
            case "J":
                print(jar)
            # Deposit
            case "D":
                jar.deposit(int(input("Amount of cookies to deposit: ")))
            # Withdraw
            case "W":
                jar.withdraw(int(input("Amount of cookies to withdraw: ")))
            # Capacity returns the jar's capacity
            case "C":
                print(jar.capacity)
            # Size returns the number of cookies actually in the jar
            case "S":
                print(jar.size)
            # Exit the program
            case "E":
                sys.exit()
            case other:
                print("Invalid command")


if __name__ == "__main__":
    main()
