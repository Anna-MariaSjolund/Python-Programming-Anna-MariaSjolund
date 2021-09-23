class OldCoinStash:
    def __init__(self, owner:str) -> None: #type hinting, it returns None (only for documentation, good practice, if we hoover over the __init__ we will see the type that it returns)
        #These attributes are public
        self.owner = owner

        #Private - by convention use underscore prefix (prefix before the word, postfix after the word) (we can also use name mangling)
        self._riksdaler = 0
        self._skilling = 0

    def deposit(self, riksdaler: float = 0, skilling: float = 0) -> None: #"riksdaler: float" is also type hinting, we expect to receive a float. We can also use | for or "float|int" for the latest version of Python.
        if riksdaler < 0 or skilling < 0:
            raise ValueError(f"Stop depositing negative values. {riksdaler} riksdaler or {skilling} skilling not okay.")
        
        self._riksdaler += riksdaler #We use _riksdaler because we want to get to the private variable and change it
        self._skilling += skilling
    
    def withdraw(self, riksdaler: float, skilling: float) -> None:
        if riksdaler > self._riksdaler or skilling > self._skilling:
            raise ValueError("You cannot withdraw more coins than you have.")
        if riksdaler < 0 or skilling < 0:
            raise ValueError("You cannot withdraw negative numbers.")
        
        self._riksdaler -= riksdaler
        self._skilling -= skilling
    
    def check_balance(self) -> str:
        return f"Coins in stash: {self._riksdaler} riksdaler and {self._skilling} skillingar."
    
    def __repr__(self) -> str: #Type hinting, it will return a String
        return f"OldCoinStash(owner='{self.owner})'."