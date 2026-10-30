from cliente import Cliente
from vehiculo import Vehiculo


class Moto(Vehiculo):

  def __init__(
      self, placa: str, color: str, dueno: Cliente, cilindrada: int
  ):
    super().__init__(placa, color, dueno)
    self.cilindrada = cilindrada

  def calcular_tarifa(self, horas: int) -> int:
    return 5 * horas  # Art. 5: Q5 por hora sin tope

  def describir(self) -> str:
    return f"Moto | {super().describir()} | {self.cilindrada} cc"