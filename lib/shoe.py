class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size   # This will now pass through the setter

    @property
    def size(self):
        """Return the size property"""
        return self._size
    
    @size.setter
    def size(self, value):
        """Set the size property"""
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
    
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
