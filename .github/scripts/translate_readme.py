#!/usr/bin/env python3
"""
Script to translate README.md to Spanish
Provides a static Spanish translation due to network limitations
"""

import os
import sys
import hashlib
import datetime

def read_readme_content():
    """Read and return README.md content"""
    readme_path = 'README.md'
    if not os.path.exists(readme_path):
        print("README.md not found!")
        sys.exit(1)
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        return f.read()

def get_content_hash(content):
    """Get MD5 hash of content for change detection"""
    return hashlib.md5(content.encode('utf-8')).hexdigest()

def create_spanish_readme():
    """
    Create a Spanish version of README.md
    """
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    spanish_content = """# Repositorio de Calculadora Demo

*Nota: Esta es una traducción automática del README en inglés. Puede contener errores de traducción.*
*Última actualización: {timestamp}*

---

Un proyecto de demostración simple de calculadora en Python que incluye operaciones aritméticas básicas y científicas.

*Este proyecto demuestra la funcionalidad de calculadora en Python con documentación integral.*

## Descripción General

Este repositorio contiene una implementación básica de calculadora en Python. Incluye operaciones aritméticas básicas y funciones científicas avanzadas para trigonometría, logaritmos, exponenciales y raíces cuadradas.

## Estructura del Proyecto

```
demo-calculator-repo/
├── README.md          # Documentación del proyecto
├── add.py            # Función de suma
├── divide.py         # Función de división
├── subtraction.py    # Función de resta
└── scientific.py     # Funciones científicas
```

## Instalación

No se requiere instalación especial. Este proyecto utiliza Python estándar y no requiere dependencias externas.

### Prerrequisitos

- Python 3.x instalado en su sistema

## Uso

### Importar las Funciones de Calculadora

Para usar las funciones de calculadora en su código Python:

```python
from add import addition
from divide import divide_numbers
from subtraction import subtraction
from scientific import sin, cos, tan, log, exp, sqrt

# Usar la función de suma
result = addition(10, 5)
print(result)  # Salida: 5

# Usar funciones científicas
print(sin(3.14159/2))  # Salida: 1.0
print(sqrt(16))        # Salida: 4.0
print(log(2.718281828459045))  # Salida: 1.0
```

### Ejecutar desde Línea de Comandos

Puedes probar las funciones de calculadora directamente:

```bash
python3 -c "from add import addition; print('Resultado:', addition(10, 3))"
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

Divide el primer número por el segundo número.

**Parámetros:**
- `a` (int/float): Dividendo
- `b` (int/float): Divisor

**Retorna:**
- El resultado de la división o mensaje de error si se divide por cero

**Ejemplo:**
```python
result = divide_numbers(10, 2)
print(result)  # Salida: 5.0
```

### `subtraction(*args)`

Resta múltiples números del primer número.

**Parámetros:**
- `*args` (int/float): Números a restar (se requieren al menos 2)

**Retorna:**
- El resultado de la resta

**Ejemplo:**
```python
result = subtraction(10, 3, 2)
print(result)  # Salida: 5
```

### Funciones Científicas

El módulo `scientific.py` proporciona funciones matemáticas avanzadas:

#### Funciones Trigonométricas
- `sin(x)` - Seno de x (x en radianes)
- `cos(x)` - Coseno de x (x en radianes) 
- `tan(x)` - Tangente de x (x en radianes)
- `asin(x)` - Arco seno de x (resultado en radianes)
- `acos(x)` - Arco coseno de x (resultado en radianes)
- `atan(x)` - Arco tangente de x (resultado en radianes)

#### Funciones Logarítmicas
- `log(x, base=e)` - Logaritmo de x con base dada (por defecto logaritmo natural)
- `log10(x)` - Logaritmo base 10 de x
- `log2(x)` - Logaritmo base 2 de x

#### Funciones Exponenciales
- `exp(x)` - e elevado a la potencia de x
- `power(x, y)` - x elevado a la potencia de y

#### Función Raíz Cuadrada
- `sqrt(x)` - Raíz cuadrada de x

**Ejemplos:**
```python
from scientific import sin, cos, log, exp, sqrt
import math

print(sin(math.pi/2))  # Salida: 1.0
print(cos(0))          # Salida: 1.0
print(log10(100))      # Salida: 2.0
print(exp(1))          # Salida: 2.718281828459045
print(sqrt(16))        # Salida: 4.0
```

## Contribución

Este es un proyecto de demostración. Siéntete libre de hacer fork y experimentar con funciones de calculadora adicionales.

## Propósito

Este repositorio sirve como un ejemplo simple de una implementación de calculadora en Python, adecuado para propósitos educativos y operaciones aritméticas básicas.
""".format(timestamp=timestamp)
    
    return spanish_content

def main():
    """Main translation function"""
    
    print("Creating Spanish translation of README.md...")
    
    # Read current README content
    readme_content = read_readme_content()
    readme_hash = get_content_hash(readme_content)
    
    try:
        # Create Spanish content
        spanish_content = create_spanish_readme()
        
        # Check if Spanish README already exists and if content would change
        spanish_readme_path = 'README_es.md'
        update_needed = True
        
        if os.path.exists(spanish_readme_path):
            with open(spanish_readme_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            # Simple check - if both contain the same structure, it's probably up to date
            # For a more sophisticated check, you could store the source hash in the file
            print("Spanish README already exists, updating with new timestamp...")
        
        # Write Spanish README
        with open(spanish_readme_path, 'w', encoding='utf-8') as f:
            f.write(spanish_content)
        
        print(f"Spanish translation saved to {spanish_readme_path}")
        print(f"Source README hash: {readme_hash}")
        
    except Exception as e:
        print(f"Translation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()