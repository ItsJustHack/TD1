class Polynomial: 
    def __init__(self, coeffs): 
        """Initialize a polynomial"""
        # 3X^2 + 2X + 1 is represented by [3, 2, 1]
        self.coeffs = coeffs

    def __str__(self): 
        
        if self.coeffs == []:
            raise "No polynom" 

        s = "("
        length = len(self.coeffs)
        for (i, coeff) in enumerate(self.coeffs):
            s +="X**" + str(coeff)

        





