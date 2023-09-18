from Persona import Persona # Importar Persona para la clase Alumno
# Clase autor que deriva de la clase Persona
class Autor(Persona):
    cod_autor = ''
    pais = ''
    editorial = ""

    def __init__(self, cod_persona, nombre, ap_paterno, ap_materno, fecha_nacimiento, cod_autor, pais, editorial):
        # Llama al constructor de la clase base (Persona)
        super().__init__(cod_persona, nombre, ap_paterno, ap_materno, fecha_nacimiento)
        self.cod_autor = cod_autor
        self.pais = pais
        self.editorial = editorial

    # Métodos getter y setter para los atributos adicionales de la clase Autor
    def get_cod_autor(self):
        return self.cod_autor
    
    def get_pais(self):
        return self.pais

    def get_editorial(self):
        return self.editorial
    #Setttttt
    def set_cod_autor(self, cod_autor):
        self.cod_autor = cod_autor

    def set_pais(self, pais):
        self.pais = pais

    def set_editorial(self, editorial):
        self.editorial = editorial

    # Método para imprimir información del autor
    def imprimir_autor(self):
        self.imprimir_persona()
        print(f"Código de Autor: {self.cod_autor}")
        print(f"País: {self.pais}")
        print(f"Editorial: {self.editorial}")