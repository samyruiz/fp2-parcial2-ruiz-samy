class Cliente:

  def __init__(self, nombre: str, telefono: str):
    self.nombre = nombre
    self.telefono = telefono

  def describir(self) -> str:
    return f"{self.nombre} ({self.telefono})"