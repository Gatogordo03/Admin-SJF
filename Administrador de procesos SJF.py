import heapq  # Liberia para manejar la cola de prioridad en lugar de hacer una lista

# Definimos la clase de Proceso
class Proceso:
    def __init__(self, PID, duracion):
        self.PID = PID
        self.duracion = duracion
        self.estado = 'Listo'

    def __lt__(self, otro):
        # Prioriza el proceso con menor duracion
        return self.duracion < otro.duracion

    def ejecutar(self):
        self.estado = 'Ejecutando'
        print(f"Proceso {self.PID} está ejecutándose...")

    def terminar(self):
        self.estado = 'Terminado'
        print(f"Proceso {self.PID} ha terminado.")

# Definimos la clase de administrador de Procesos
class AdministradorProcesos:
    def __init__(self):
        self.cola_procesos = []

    def añadir_proceso(self, proceso):
        heapq.heappush(self.cola_procesos, proceso)
        print(f"Proceso {proceso.PID} añadido con duración {proceso.duracion}.")

    def planificar(self):
        if not self.cola_procesos:
            print("No hay procesos en la cola.")
            return

        # Extraer el proceso mas corto / SJF
        proceso_actual = heapq.heappop(self.cola_procesos)
        proceso_actual.ejecutar()
        # Simulamos la ejecucion del proceso
        proceso_actual.terminar()

# Simulacion de uso
adm = AdministradorProcesos()
adm.añadir_proceso(Proceso(1, 5))
adm.añadir_proceso(Proceso(2, 3))
adm.añadir_proceso(Proceso(3, 8))
#Los procesos que sean necesarios se pueden poner

# La ejecucion de los procesos
adm.planificar()
adm.planificar()
adm.planificar()
