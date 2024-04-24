class Paciente:
    def __init__(self, NombrePaciente, Edad, Condicion, Prioridad):
        self.NombrePaciente = NombrePaciente
        self.Edad = Edad
        self.Condicion = Condicion
        self.Prioridad = Prioridad
    
    def __str__(self):
        return f"--------------------\nPaciente: {self.NombrePaciente}.\nCondicion: {self.Condicion}.\nPrioridad: {self.Prioridad}\n"
    
class DNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    #Recorrer y mostrar
    def traverse(self):
        node = self.head
        while(node is not None):
            print(node.value)
            node = node.next

    #Agregar
    def append(self, value, node):
        if(self.head is None):
            self.head = DNode(value)
            self.size += 1
            return
        #Para que se agregen primero que el mismo prioridad <=
        #if(value.NombrePaciente < node.value.NombrePaciente): (Orden alfabetico)
        #if(value.Edad < node.value.Edad): (Edad)
        #if(value.Prioridad < node.value.Prioridad): (Prioridad)
        if(value.Prioridad < node.value.Prioridad):
            new_node = DNode(value)
            new_node.next = node
            new_node.prev = node.prev
            if(node.prev is not None):
                node.prev.next = new_node
            else:
                self.head = new_node
            node.prev = new_node
            self.size += 1
            return
        if(node.next is None):
            new_node = DNode(value)
            node.next = new_node
            new_node.prev = node
            self.size += 1
            return
        self.append(value, node.next)

    #Agregar al comienzo
    def preppend(self, value):
        new_node = DNode(value)
        self.head = new_node
        new_node.next = self.head
        self.size += 1

    #Eliminar por indice
    def delete_at_index(self, del_index, node, pos=0):
        if(del_index >= self.size): return
        if(del_index == 0):
            next = self.head.next
            self.head.next = None
            self.head = next
            self.head.prev = None
            self.size -= 1
            return
        if(pos == del_index):
            next = node.next
            prev = node.prev
            node.next.prev = prev
            node.prev.next = next
            self.size -= 1
            return
        self.delete_at_index(del_index, node.next, pos+1)

    #Eliminar primero
    def delete_atencion(self):
        if(self.size == 0):return
        if self.head is not None:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            self.size -= 1
        return
    
    #Mostrar siguiente atencion
    def mostrar_siguiente_atencion(self, node):
        if node is None:
            return
        print(f"Paciente: {node.value.NombrePaciente}")
        print(f"Condicion: {node.value.Condicion}")
        print(f"Prioridad: {node.value.Prioridad}")
        return

    #Borra el ultimo de la lista
    def delete(self, node):
        if(self.size == 0):return
        if(node.next == None):
            node.prev.next = None
            node.prev = None
            self.size -= 1
            return 
        self.delete(node.next)
    
    #Actualizar prioridad/lista
    def actualizar_prioridad(self, nombre_paciente, nueva_prioridad, node):
        if node is None:
            return
        
        if node.value.NombrePaciente == nombre_paciente:
            paciente_actualizado = Paciente(node.value.NombrePaciente, node.value.Edad, node.value.Condicion, nueva_prioridad)
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next
            if node.next is not None:
                node.next.prev = node.prev
            self.append(paciente_actualizado, self.head)
            return
        else:
            siguiente_node = node.next
            self.actualizar_prioridad(nombre_paciente, nueva_prioridad, siguiente_node)