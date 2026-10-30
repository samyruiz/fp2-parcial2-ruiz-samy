from cliente import Cliente
from vehiculo import Vehiculo


class Pickup(Vehiculo):

  def __init__(self, placa: str, color: str, dueno: Cliente, carga_ton: int):
    super().__init__(placa, color, dueno)
    self.carga_ton = carga_ton

  def calcular_tarifa(self, horas: int) -> int:
    return 15 * horas + 10  # Art. 5: Q15 por hora más Q10 de manejo

  def describir(self) -> str:
    return f"Pickup | {super().describir()} | {self.carga_ton} toneladas"