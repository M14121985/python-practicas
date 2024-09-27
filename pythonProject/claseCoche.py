class Coche:
    """
    Representa un coche genérico.

    Atributos:
        marca (str): La marca del coche.
        modelo (str): El modelo del coche.
        color (str): El color del coche.
        año (int): El año de fabricación del coche.
    """

    def __init__(self, marca, modelo, color, año):
        """
        Inicializa un objeto Coche.

        Args:
            marca (str): La marca del coche.
            modelo (str): El modelo del coche.
            color (str): El color del coche.
            año (int): El año de fabricación del coche.
        """
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._año = año

    @property
    def marca(self):
        """Obtiene la marca del coche."""
        return self._marca

    @property
    def modelo(self):
        """Obtiene el modelo del coche."""
        return self._modelo

    @property
    def color(self):
        """Obtiene el color del coche."""
        return self._color

    @color.setter
    def color(self, nuevo_color):
        """
        Cambia el color del coche.


        Args:
            nuevo_color (str): El nuevo color del coche.
        """
        self._color = nuevo_color

    @property
    def año(self):
        """Obtiene el año de fabricación del coche."""
        return self._año

    @año.setter
    def año(self, nuevo_año):
        """
        Cambia el año de fabricación del coche.

        Args:
            nuevo_año (int): El nuevo año de fabricación del coche.
        """
        self._año = nuevo_año


# Clases que heredan de Coche
class CocheDeportivo(Coche):
    """
    Representa un coche deportivo, derivado de Coche.

    Atributos adicionales:
        caballos_fuerza (int): La potencia del coche en caballos de fuerza.
    """

    def __init__(self, marca, modelo, color, año, caballos_fuerza):
        """
        Inicializa un objeto CocheDeportivo.

        Args:
            marca (str): La marca del coche.
            modelo (str): El modelo del coche.
            color (str): El color del coche.
            año (int): El año de fabricación del coche.
            caballos_fuerza (int): La potencia del coche en caballos de fuerza.
        """
        super().__init__(marca, modelo, color, año)
        self._caballos_fuerza = caballos_fuerza

    @property
    def caballos_fuerza(self):
        """Obtiene la potencia del coche en caballos de fuerza."""
        return self._caballos_fuerza


class CocheElectrico(Coche):
    """
    Representa un coche eléctrico, derivado de Coche.

    Atributos adicionales:
        autonomia (int): La autonomía del coche en kilómetros.
    """

    def __init__(self, marca, modelo, color, año, autonomia):
        """
        Inicializa un objeto CocheElectrico.

        Args:
            marca (str): La marca del coche.
            modelo (str): El modelo del coche.
            color (str): El color del coche.
            año (int): El año de fabricación del coche.
            autonomia (int): La autonomía del coche en kilómetros.
        """
        super().__init__(marca, modelo, color, año)
        self._autonomia = autonomia

    @property
    def autonomia(self):
        """Obtiene la autonomía del coche en kilómetros."""
        return self._autonomia


# Ejemplo de uso
mi_coche = Coche("Toyota", "Corolla", "Azul", 2022)

# Acceder a los docstrings
print(Coche.__doc__)             # Docstring de la clase Coche
print(mi_coche.marca.__doc__)    # Docstring de la propiedad marca
print(mi_coche.color.__doc__)    # Docstring de la propiedad color (getter)
print(Coche.color.fset.__doc__)  # Docstring de la propiedad color (setter)

