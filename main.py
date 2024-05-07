from Logic import *

def showMenu():
    print("----------------------------------")
    print("   Sistema Gestion de Pacientes   ")
    print("----------------------------------")
    print("Bienvenido al sistema de gestion de pacientes, por favor seleccione una opción")
    print("1. Mostrar cola")
    print("2. Ingresar paciente")
    print("3. Actualizar prioridad")
    print("4. Extraer/Atencion paciente")
    print("5. Actualizar cola por urgencia")
    print("6. Salir")

def showOption_1(Cola):
    return Cola.traverse()

def showOption_2(Cola):
    print("----------------------------------")
    print("         Ingresar paciente        ")
    print("----------------------------------")
    NombrePaciente = input("Nombre del paciente: ")
    Edad = int(input("Edad: "))
    Condicion = input("Descripcion de la condicion: ")
    Prioridad = int(input("Prioridad: "))

    Obj_Paciente = Paciente(NombrePaciente, Edad, Condicion, Prioridad)

    Cola.append(Obj_Paciente, Cola.head)

    return Cola

def showOption_3(Cola):
    print("----------------------------------")
    print("       Actualizar prioridad       ")
    print("----------------------------------")
    NombrePaciente = input("Nombre del paciente: ")
    NuevaPrioridad = int(input("Nueva prioridad: "))

    Cola.actualizar_prioridad_nombre(NombrePaciente, NuevaPrioridad, Cola.head)

    return Cola

def showOption_4(Cola):
    print("----------------------------------")
    print("              Atencion            ")
    print("----------------------------------")
    Cola.delete_atencion()
    print("Paciente atendido")
    print("----------------------------------")
    print("El siguiente paciente es:")
    Cola.mostrar_siguiente_atencion(Cola.head)
    return Cola

def showOption_5(Cola):
    Cola.urgente()

def main():

    Cola_Pacientes = DLinkedList()

    while True:

        showMenu()

        selection = int(input("Por favor, selecciona una opción: "))

        if selection == 1:
            showOption_1(Cola_Pacientes)
        elif selection == 2:
            showOption_2(Cola_Pacientes)
        elif selection == 3:
            showOption_3(Cola_Pacientes)
        elif selection == 4:
            showOption_4(Cola_Pacientes)
        elif selection == 5:
            showOption_5(Cola_Pacientes)
        elif selection == 6:
            print("Usted ha salido del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()