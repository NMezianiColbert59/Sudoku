class Case:
    
    def __init__(self, pos, value = None):
        """
            Constructeur par défaut
            Arguments :
                - pos   : position (0--80)
                - value : valeur (1--9)
            Tests :
            >>> Case(0).position, Case(80).position, Case(25).position
            (0, 80, 25)
            >>> Case(13).value, Case(13, 3).value
            (None, 3)
            >>> Case(0).row, Case(80).row, Case(25).row
            (0, 8, 7)
            >>> Case(0).line, Case(80).line, Case(25).line
            (0, 8, 2)
            >>> Case(0).region, Case(80).region, Case(25).region
            (1, 9, 3)
        """
        self.position = pos
        self.value = value
        self.row = pos%9
        self.line = pos//9
        self.region = pos//9+1
         
    def setValue(self, value):
        """
            Mutateur de l'attribut value
            
            Tests :
            >>> c = Case(13, 2)
            >>> c.setValue(8)
            >>> c.value == 4
            False
            >>> c.value == 5
            False
        """
        self.value = value
        
if __name__ == '__main__':
    import doctest
    doctest.testmod()