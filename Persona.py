class Persona:
    # Atributos de la clase Persona 
    cod_persona = "" # Por ahora no se usa
    nombre = ""
    ap_paterno = ""
    ap_materno = ""
    fecha_nacimiento = ""

    # Constructor de la clase Persona
    def __init__(self, cod_persona, nombre, ap_paterno, ap_materno, fecha_nacimiento):
        self.cod_persona = cod_persona
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.fecha_nacimiento = fecha_nacimiento

    # Métodos getter
    def get_cod_persona(self):
        return self.cod_persona

    def get_nombre(self):
        return self.nombre

    def get_ap_paterno(self):
        return self.ap_paterno

    def get_ap_materno(self):
        return self.ap_materno

    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento

    # Métodos setter
    def set_cod_persona(self, cod_persona):
        self.cod_persona = cod_persona

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_ap_paterno(self, ap_paterno):
        self.ap_paterno = ap_paterno

    def set_ap_materno(self, ap_materno):
        self.ap_materno = ap_materno

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    # Método para imprimir información de la persona
    def imprimir_persona(self):
        print(f"Codigo de Persona: {self.cod_persona}")
        print(f"Nombre: {self.nombre} {self.ap_paterno} {self.ap_materno}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")

