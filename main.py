class Paciente:
    def __init__(self, NombrePaciente, Edad, Condicion, Prioridad):
        self.NombrePaciente = NombrePaciente
        self.Edad = Edad
        self.Condicion = Condicion
        self.Prioridad = Prioridad

    def ObtenerPrioridad(self):
            return self.Prioridad
    
    