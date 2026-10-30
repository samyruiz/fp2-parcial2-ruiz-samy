from carro import Carro
from cliente import Cliente
from moto import Moto
from parqueo import Parqueo
from pickup import Pickup


def main():
  parqueo = Parqueo("El Obelisco", 6)

  while True:
    print("\n+++++ PARQUEO EL OBELISCO +++++")
    print("1. REGISTRAR ENTRADA")
    print("2. REGISTRAR SALIDA")
    print("3. VER VEHÍCULOS ESTACIONADOS")
    print("4. BUSCAR VEHÍCULO POR PLACAS")
    print("5. VER RESUMEN DEL DÍA")
    print("6. SALIR")
    opcion = input("BIENVENIDO ELIGE UNA OPCIÓN: ").strip()

    if opcion == "1":
      # Orden estricto: tipo -> placa -> color -> dato propio -> dueño -> teléfono -> hora entrada
      tipo = input("Tipo (M, C o P): ").strip().upper()
      if tipo not in ["M", "C", "P"]:
        print("Error: Tipo no válido. Debe ser M, C o P.")
        continue

      placa = input("Placa: ").strip()
      color = input("Color: ").strip()

      if tipo == "M":
        dato_str = input("Cilindrada: ").strip()
      elif tipo == "C":
        dato_str = input("Puertas: ").strip()
      else:
        dato_str = input("Carga (ton): ").strip()

      if not dato_str.isdigit():
        print("Error: El dato propio debe ser un número entero.")
        continue
      dato_propio = int(dato_str)

      nombre_dueno = input("Nombre del dueño: ").strip()
      telefono = input("Teléfono: ").strip()

      hora_str = input("Hora de entrada: ").strip()
      if not hora_str.isdigit():
        print("Error: La hora de entrada debe ser un número entero.")
        continue
      hora_entrada = int(hora_str)

      dueno = Cliente(nombre_dueno, telefono)
      if tipo == "M":
        vehiculo = Moto(placa, color, dueno, dato_propio)
      elif tipo == "C":
        vehiculo = Carro(placa, color, dueno, dato_propio)
      else:
        vehiculo = Pickup(placa, color, dueno, dato_propio)

      parqueo.registrar_entrada(vehiculo, hora_entrada)

    elif opcion == "2":
      placa = input("Placa: ").strip()
      hora_str = input("Hora de salida: ").strip()
      if not hora_str.isdigit():
        print("Error: La hora de salida debe ser un número entero.")
        continue
      hora_salida = int(hora_str)

      parqueo.registrar_salida(placa, hora_salida)

    elif opcion == "3":
      parqueo.listar()

    elif opcion == "4":
      placa = input("Placa: ").strip()
      vehiculo = parqueo.buscar(placa)
      if vehiculo is not None:
        print(vehiculo.describir())
      else:
        print(f"El vehículo con placa {placa.upper()} no está en el parqueo.")

    elif opcion == "5":
      print(f"Espacios libres: {parqueo.espacios_libres()}")
      print(f"Total recaudado: Q{parqueo.total_recaudado}")

    elif opcion == "6":
      print("Saliendo del programa. ¡Regrese pronto!")
      break

    else:
      print("Error: Opción no válida. Por favor elige entre 1 y 6.")


if __name__ == "__main__":
  main()