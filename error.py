class DimensionError(Exception):
    def __init__(self, messages, dimensions, max):
        super().__init__(messages)
        self.dimensions = dimensions
        self.max = max
        
        
    def __str__(self):
        if self.dimensions < 1:
            return f'La dimensión {self.dimensions} esta bajo lo permitido'
        else:
            return f'La dimensión {self.dimensions} no puede ser mayor al máximo {self.max}'