# Repositorio Calculadora Demo

Un proyecto de demostración de calculadora Python simple que incluye operaciones aritméticas básicas.

## Resumen

Este repositorio contiene una implementación básica de calculadora en Python. Actualmente, incluye funciones de suma y división que se pueden usar para realizar operaciones matemáticas entre dos números.

## Estructura del Proyecto

```
demo-calculator-repo/
├── README.md          # Documentación del proyecto
├── README-es.md       # Documentación en español
├── divide.py         # Funciones de calculadora
└── add.py            # Funciones de calculadora
```

## Instalación

No se requiere instalación especial. Este proyecto usa Python estándar y no requiere dependencias externas.

### Requisitos Previos

- Python 3.x instalado en su sistema

## Uso

### Importando las Funciones de Calculadora

Para usar las funciones de calculadora en su código Python:

```python
from add import addition
from divide import divide_numbers

# Usar la función de suma
result = addition(10, 5)
print(result)  # Salida: 5

# Usar la función de división
result = divide_numbers(10, 2)
print(result)  # Salida: 5.0
```

### Ejecutando desde Línea de Comandos

Puede probar las funciones de calculadora directamente:

```bash
python3 -c "from add import addition; print('Resultado suma:', addition(10, 3))"
python3 -c "from divide import divide_numbers; print('Resultado división:', divide_numbers(10, 2))"
```

## Funciones Disponibles

### `addition(a, b)`

Realiza una operación matemática entre dos números.

**Parámetros:**
- `a` (int/float): Primer número
- `b` (int/float): Segundo número

**Retorna:**
- El resultado de la operación matemática

**Ejemplo:**
```python
result = addition(8, 3)
print(result)  # Salida: 5
```

### `divide_numbers(a, b)`

Realiza división entre dos números con manejo de errores.

**Parámetros:**
- `a` (int/float): Dividendo
- `b` (int/float): Divisor

**Retorna:**
- El resultado de la división o un mensaje de error si se divide por cero

**Ejemplo:**
```python
result = divide_numbers(10, 2)
print(result)  # Salida: 5.0
```

## Contribuciones

Este es un proyecto de demostración. Siéntase libre de hacer fork y experimentar con funciones adicionales de calculadora.

## Propósito

Este repositorio sirve como un ejemplo simple de implementación de calculadora Python, adecuado para propósitos educativos y operaciones aritméticas básicas.
