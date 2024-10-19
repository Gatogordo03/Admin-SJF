# Simulador de Administrador de Procesos en Python

Este proyecto es una simulación básica de un administrador de procesos en Python, utilizando el algoritmo **Shortest Job First (SJF)** para planificar los procesos. Los procesos se gestionan mediante una **cola de prioridad** utilizando la librería `heapq`.

Se podria gestionar desde una lista de procesos sin libreria pero esto facilita mas las cosas.

## Estructura del Proyecto

El proyecto está compuesto por dos clases principales:

1. **Clase `Proceso`:**
   Representa un proceso individual que será administrado por el simulador.

2. **Clase `AdministradorProcesos`:**
   Gestiona la cola de procesos y utiliza el algoritmo SJF para planificar cuál proceso debe ejecutarse primero.

### Clase `Proceso`

Esta clase contiene la representación básica de un proceso. Los atributos y métodos son los siguientes:

- **Atributos:**
  - `PID`: Identificador único del proceso (un número entero).
  - `duracion`: La duración del proceso en unidades de tiempo.
  - `estado`: El estado actual del proceso (`Listo`, `Ejecutando`, `Terminado`).

- **Métodos:**
  - `__init__(self, pid, duracion)`: Inicializa un nuevo proceso con su identificador y duración.
  - `__lt__(self, otro)`: Método que define la comparación entre procesos por duración, necesario para la cola de prioridad.
  - `ejecutar(self)`: Cambia el estado del proceso a `Ejecutando` e imprime un mensaje indicando su ejecución.
  - `terminar(self)`: Cambia el estado del proceso a `Terminado` e imprime un mensaje indicando su finalización.

### Clase `AdministradorProcesos`

Esta clase administra la cola de procesos y la ejecución de estos siguiendo el algoritmo SJF. 

- **Atributos:**
  - `cola_procesos`: Una lista que contiene los procesos organizados como un montículo (heap), permitiendo una rápida selección del proceso más corto.

- **Métodos:**
  - `__init__(self)`: Inicializa la cola de procesos vacía.
  - `añadir_proceso(self, proceso)`: Añade un nuevo proceso a la cola de procesos.
  - `planificar(self)`: Selecciona el proceso con la menor duración de la cola, lo ejecuta y lo marca como terminado.

### Diagrama de Flujo Simplificado

```plaintext
1. El usuario añade procesos a la cola.
2. El administrador de procesos selecciona el proceso con menor duración.
3. El proceso se ejecuta.
4. El proceso se marca como terminado.
5. Se repite hasta que no queden procesos en la cola.
```

## Uso del Proyecto

### Instalación

No se requieren dependencias adicionales. El proyecto utiliza solamente la biblioteca estándar de Python.

### Ejecución del Código

1. Clona el repositorio o descarga los archivos del proyecto.

2. Ejecuta el archivo principal(puedes modificar el nombre y ejecutarlo mas sencillo):

```bash
python Administrador\ de\ procesos\ SJF.py
```
### Ejemplo de Uso

```python
# Crear el administrador de procesos
adm = AdministradorProcesos()

# Añadir procesos con diferentes duraciones
adm.añadir_proceso(Proceso(1, 5))
adm.añadir_proceso(Proceso(2, 3))
adm.añadir_proceso(Proceso(3, 8))

# Planificar y ejecutar procesos
adm.planificar()  # Ejecutará el proceso con menor duración
adm.planificar()  # Ejecutará el siguiente proceso más corto
adm.planificar()  # Ejecutará el último proceso
```

### Salida Esperada

```
Proceso 2 está ejecutándose...
Proceso 2 ha terminado.
Proceso 1 está ejecutándose...
Proceso 1 ha terminado.
Proceso 3 está ejecutándose...
Proceso 3 ha terminado.
```

## Mejoras Futuras

- Implementación de otros algoritmos de planificación de procesos como Round Robin o First Come First Serve (FCFS).

- Mejorar la simulación agregando interrupciones o tiempos de espera.

- Añadir soporte para la visualización del estado de los procesos en tiempo real.
