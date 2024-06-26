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
        #Para que se agregen primero que el mismo prioridad <=
        #if(value.NombrePaciente < node.value.NombrePaciente): (Orden alfabetico)
        #if(value.Edad < node.value.Edad): (Edad)
        #if(value.Prioridad < node.value.Prioridad): (Prioridad)
        
    def append(self, value, node):
        if(self.head is None):
            self.head = DNode(value)
            self.size += 1
            return
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
            """prioridad = value.Prioridad
            if self.cuento(prioridad) > 1:
                self.actualizar_prioridad(self.head, prioridad)"""
            return
        if(node.next is None):
            new_node = DNode(value)
            node.next = new_node
            new_node.prev = node
            self.size += 1
            """prioridad = value.Prioridad
            if self.cuento(prioridad) > 1:
                self.actualizar_prioridad(self.head, prioridad)"""
            return
        self.append(value, node.next)
    
    def cuento(self, prioridad):
        contador = 0
        node = self.head
        while node is not None:
            if node.value.Prioridad == prioridad:
                contador += 1
            node = node.next
        return contador

    def actualizar_prioridad(self, node, prioridad):
        while node is not None:
            if node.value.Prioridad == prioridad:
                paciente_actualizado = Paciente(node.value.NombrePaciente, node.value.Edad, node.value.Condicion, node.value.Prioridad + 1)
                node.value = paciente_actualizado
            node = node.next

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
    
    #Actualizar prioridad/lista
    def actualizar_prioridad_nombre(self, nombre_paciente, nueva_prioridad, node):
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
            self.actualizar_prioridad_nombre(nombre_paciente, nueva_prioridad, siguiente_node)
    
    def urgente(self):
        
        nodo_y = self.prioridad(self.head)
        nodo_x = self.primer_nodo(self.head)
        
        aux1 = nodo_y.prev
        aux2 = nodo_y.next
        
        nodo_y.prev = nodo_x.prev
        nodo_y.next = nodo_x
        
        if(aux2 is None):
            aux1.next = None
        else:
            aux1.next = aux2            
            aux2.prev = aux1
        
        nodo_x.prev.next = nodo_y
        nodo_x.prev = nodo_y
            
    def primer_nodo(self, node):
        while node is not None:
            if node.value.Prioridad == (self.prioridad(self.head).value.Prioridad):
                return node
            node = node.next
            
            
    def prioridad(self, node):
        palabra = "urgente"
        while node is not None:
            if palabra in node.value.Condicion:
                return node
            node = node.next