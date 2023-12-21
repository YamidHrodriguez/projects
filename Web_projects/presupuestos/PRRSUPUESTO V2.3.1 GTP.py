from datetime import datetime

# Rutas de los archivos
total_file_path = "./db/TOTAL.txt"
registro_file_path = "./db/Registro.txt"
ingresos_file_path = "./db/Ingresos.txt"
egresos_file_path = "./db/Egresos.txt"
total_egresos_file_path = "./db/Total_eg.txt"
total_ingresos_file_path = "./db/Total_ing.txt"

# CLASE PADRE
class Total:
    def __init__(self, id, amount=0):
        self.id = id
        self.amount = amount

    def actualizar_total(self, opc, monto):
        # Actualizar el total general
        with open(total_file_path, "r+") as file:
            total_general = float(file.read().strip() or 0)
            if opc.lower() == "ingreso":
                total_general += monto
            elif opc.lower() == "egreso":
                total_general -= monto
            file.seek(0)
            file.write(str(total_general))
            file.truncate()

        # Actualizar el total de ingresos o egresos
        if opc.lower() == "ingreso":
            with open(total_ingresos_file_path, "r+") as total_ing:
                total_ingresos = float(total_ing.read().strip() or 0)
                total_ingresos += monto
                total_ing.seek(0)
                total_ing.write(str(total_ingresos))
                total_ing.truncate()
            with open(ingresos_file_path, "w+") as ing:
                ing.write(f'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@          
            •  INGRESÓ 
             •  DESCRIPCIÓN: {obj.name}
             •  CANTIDAD: ${obj.amount}
             •  FECHA Y HORA: {obj.fecha_hora}
______________________________________________                
            TOTAL INGRESOS: ${total_ingresos}
''')
        elif opc.lower() == "egreso":
            with open(total_egresos_file_path, "r+") as total_eg:
                total_egresos = float(total_eg.read().strip() or 0)
                total_egresos += monto
                total_eg.seek(0)
                total_eg.write(str(total_egresos))
                total_eg.truncate()
            with open(egresos_file_path, "w+") as egr:
                egr.write(f'''
            •  EGRESÓ 
             •  DESCRIPCIÓN: {obj.name}
             •  CANTIDAD: ${obj.amount}
             •  FECHA Y HORA: {obj.fecha_hora}
______________________________________________                
            TOTAL EGRESOS: ${total_egresos}
''')

        # Registrar el movimiento en el archivo de registro general
        with open(registro_file_path, "w") as txt:
            txt.write(f'''
INGRESOS-EGRESOS 
********************* TOTAL: ${total_general}
''')

        return total_general


# CLASE HIJA
class Movement(Total):
    def __init__(self, id, tip, name, fecha_hora, amount):
        super().__init__(id, amount)
        self.tip = tip
        self.name = name
        self.fecha_hora = fecha_hora


# ALGORITMO PRINCIPAL
while True:
    opc = int(input('''
                APP DE FINANZAS PERSONALES
    °°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
                1) REGISTRAR INGRESO DE DINERO
                2) REGISTRAR EGRESO DE DINERO
                3) IMPRIMIR INFORMACIÓN
                4) FORMATEAR REGISTROS
                5) SALIR
    '''))

    if opc == 5:
        break

    if opc == 1:
        opc = "ingreso"
        name = input("Nombre del ingreso: ")
        amount = float(input("Cantidad de dinero ingresado: "))
        fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M %p")
        obj = Movement(1, opc, name, fecha_hora, amount)
        monto = obj.amount
        cont = obj.actualizar_total(opc, monto)

    elif opc == 2:
        opc = "egreso"
        name = input("Nombre del egreso: ")
        amount = float(input("Cantidad de dinero a sacar: "))
        fecha_hora = datetime.now().strftime("%d/%m/%Y %I:%M %p")
        obj = Movement(2, opc, name, fecha_hora, amount)
        monto = obj.amount
        cont = obj.actualizar_total(opc, monto)

    elif opc == 3:
        with open(ingresos_file_path, "r") as txt1, open(egresos_file_path, "r") as txt2, open(registro_file_path, "r") as txt:
            doc1 = txt1.readlines()
            doc2 = txt2.readlines()
            doc = txt.readlines()
            for line in doc1:
                print(line)
            print(f"{'@'*45}")
            for line in doc2:
                print(line)
            print(f"{'@'*45}")
            for line in doc:
                print(line)

    elif opc == 4:
        with open(total_file_path, "w"), open(registro_file_path, "w"), open(ingresos_file_path, "w"), \
                open(egresos_file_path, "w"), open(total_egresos_file_path, "w"), open(total_ingresos_file_path, "w"):
            print("FORMATEO EXITOSO")

print("Cierre de archivos exitoso")