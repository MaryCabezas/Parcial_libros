class Categoria:
    cod_categoria = ""
    categoria = ""
    
    def __init__(self, cod_categoria, categoria):
        self.cod_categoria = cod_categoria
        self.categoria = categoria

    def get_cod_categoria(self):
        return self.cod_categoria

    def set_cod_categoria(self, cod_categoria):
        self.cod_categoria = cod_categoria

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

    def imprimir_categoria(self):
        print(f"Código de Categoría: {self.cod_categoria}")
        print(f"Categoría: {self.categoria}")