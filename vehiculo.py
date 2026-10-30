from abc import ABC, abstractmethod
from cliente import Cliente


class Vehiculo(ABC):

  def __init__(self, placa: str, color: str, dueno: Cliente):
    self.placa = placa.strip().upper()  # Art. 3: placas siempre en mayúsculas
    self.color = color.strip()
    self.dueno = dueno
    self.hora_entrada = None  # Se asigna hasta que Parqueo confirme la entrada

  @abstractmethod
  def calcular_tarifa(self, horas: int) -> int:
    """Método abstracto obligatorio para todas las subclases."""
    pass

  def describir(self) -> str:
    return f"{self.placa}, color {self.color}, dueño: {self.dueno.describir()}"