from cliente import Cliente
from vehiculo import Vehiculo


class Carro(Vehiculo):

  def __init__(self, placa: str, color: str, dueno: Cliente, puertas: int):
    super().__init__(placa, color, dueno)
    self.puertas = puertas

  def calcular_tarifa(self, horas: int) -> int:
    return min(10 * horas, 60)  # Art. 5: Q10 por hora, tope máximo Q60

  def describir(self) -> str:
    return f"Carro | {super().describir()} | {self.puertas} puertas"