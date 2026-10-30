from vehiculo import Vehiculo


class Parqueo:

  def __init__(self, nombre: str, capacidad: int):
    self.nombre = nombre
    self.capacidad = capacidad
    self.estacionados: list[Vehiculo] = []
    self.total_recaudado: int = 0

  def espacios_libres(self) -> int:
    return self.capacidad - len(self.estacionados)

  def buscar(self, placa: str) -> Vehiculo | None:
    placa_buscada = placa.strip().upper()
    for vehiculo in self.estacionados:
      if vehiculo.placa == placa_buscada:
        return vehiculo
    return None

  def registrar_entrada(self, vehiculo: Vehiculo, hora: int) -> bool:
    # Art. 1 · Capacidad
    if len(self.estacionados) >= self.capacidad:
      print(
          "Art. 1 (Capacidad): El parqueo está lleno. No se admite ningún"
          " vehículo más."
      )
      return False

    # Art. 2 · Horario
    if hora < 6 or hora > 22:
      print(
          f"Art. 2 (Horario): La hora {hora} está fuera de horario (6 a 22"
          " hrs). Entrada rechazada."
      )
      return False

    # Art. 3 · Placa única
    if self.buscar(vehiculo.placa) is not None:
      print(
          f"Art. 3 (Placa única): El vehículo con placa {vehiculo.placa} ya"
          " está adentro. Entrada rechazada."
      )
      return False

    # Si pasa todas las validaciones
    vehiculo.hora_entrada = hora
    self.estacionados.append(vehiculo)
    print(
        f"Entrada registrada: {vehiculo.describir()} | Hora:"
        f" {hora}:00 hrs."
    )
    return True

  def registrar_salida(self, placa: str, hora: int) -> int:
    vehiculo = self.buscar(placa)
    if vehiculo is None:
      print(
          "Error: No se encontró ningún vehículo con placa"
          f" {placa.strip().upper()} en el parqueo."
      )
      return 0

    # Art. 2 · Horario
    if hora < 6 or hora > 22:
      print(
          f"Art. 2 (Horario): La hora {hora} está fuera de horario (6 a 22"
          " hrs). Salida rechazada."
      )
      return 0

    # Art. 4 · Salida
    if hora < vehiculo.hora_entrada:
      print(
          "Art. 4 (Salida): Nadie sale antes de la hora en que entró"
          f" (Entrada: {vehiculo.hora_entrada} hrs, Salida intentada: {hora}"
          " hrs)."
      )
      return 0

    # Si sale en la misma hora, se cobra mínimo 1 hora
    horas_estadia = hora - vehiculo.hora_entrada
    if horas_estadia == 0:
      horas_estadia = 1

    monto = vehiculo.calcular_tarifa(horas_estadia)
    self.total_recaudado += monto
    self.estacionados.remove(vehiculo)

    print(
        f"Salida registrada: {vehiculo.placa} | Horas cobradas:"
        f" {horas_estadia} | Monto a cobrar: Q{monto}"
    )
    return monto

  def listar(self):
    if not self.estacionados:
      print("No hay ningún vehículo estacionado.")
      return
    print(
        f"--- Vehículos estacionados en {self.nombre}"
        f" ({len(self.estacionados)}/{self.capacidad}) ---"
    )
    for vehiculo in self.estacionados:
      print(
          f"- {vehiculo.describir()} | Hora de entrada:"
          f" {vehiculo.hora_entrada}:00 hrs"
      )