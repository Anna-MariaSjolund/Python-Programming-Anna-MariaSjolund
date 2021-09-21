class Vector:
    '''A class to represent a euclidean vector with magnitude and direction.'''
    
    def __init__(self, *numbers:float) -> None: #We use star so that we can input different number of numbers (numbers is a tuple)
        #print(numbers)
        for number in numbers:
            if not isinstance(number, (float, int)): #We do not need a paranthesis if we only want to check for example float
                #However booleans will not raise an error since they are evaluated to 0 and 1
                raise TypeError(f"{number} is not a valid number. Number must be a float or int, not {type(number)}.")

        if len(numbers) <= 0: #We can use len because number is a tuple
            raise ValueError("Vectors can't be empty.")
        
        #self.numbers = (number for number in numbers) #this is a tuple comprehension, this will create a generator
        #We convert the number into a float so that True and False will also be numbers
        #Using _ here makes it private (we could also use a setter)
        self._numbers = tuple(float(number) for number in numbers) #We have to convert the generator to a tuple

    @property
    def numbers(self) -> tuple:
        return self._numbers

    #We us __add__ to overload addition
    #It's convention to use self, so that other developers see that it is a method (although Python does not require it)
    #We use other if we want another of the same type
    #The method should return a new Vector
    #(2, 3) + (1, 1, 1) Not okay, they have to be the same dimension
    #(2, 3) + (1, 1) = (3, 4) This is okay


    def __add__(self, other:"Vector") -> "Vector": #We have to use quotes becuase it is a custom type
        if self.validate_vectors(other): #The object itself will be sent it to the method, together with other that we specify
            #Other will now be a vector have the same dimension
            #We zip together self.numbers and other.numbers and unpack them in a and b, then add them together and store them in number
            numbers = (a+b for a, b in zip(self.numbers, other.numbers)) #numbers is now a generator
            #we have to unpack the generator object using *
            #If we have five numbers the numbers will be unpacked and each element will be sent to the Vector
            return Vector(*numbers) 

    #If we do not make this function we cannot runt len(v1) in the Jupyter notebook
    #We have done this by operation overload
    # len() function
    def __len__(self) -> int:
        '''Returns number of components in a Vector, not the Euclidean length.'''
        return len(self.numbers) #self.numbers is a tuple which we can run len on and get the number of elements

    def validate_vectors(self, other: "Vector") -> bool:
        '''Validate if two vectors have same dimension'''
        if not isinstance(other, Vector) or len(other) != len(self):
            raise TypeError("Both must be Vector and same length.")
        return len(self) == len(other)
    
    #If we only have the __repr__ method it will print this when printing the object
    def __repr__(self) -> str:
        return f"Vector{self.numbers}"
    
    #If we have a __str__ this will be printed, instead of what is in the __repr__ when printing the object
    def __str__(self) -> str:
        return f"{self.numbers}"

    # [] operator
    def __getitem__(self, item:int) -> float:
        return self.numbers[item] #This will enable us to reach an element in the list
#Both of these are valid vectors
#v1 = (1, 1)
#v2 = (1, 1, 14, 5, 2, 252, 56, 2, 7)
