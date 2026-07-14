# Intérprete de Lógicas No Clásicas y Tablas de Verdad Plurivalentes

Una implementación en Python de un motor de evaluación y generador de tablas de verdad para sistemas lógicos no clásicos, enfocándose específicamente en **First-Degree Entailment (FDE)**, la **Lógica de la Paradoja (LP)** de Priest, y la **Lógica Triente Fuerte de Kleene (K3)**.

Este proyecto demuestra cómo las estructuras lógicas y algebraicas abstractas pueden modelarse en Python de forma limpia y modular, utilizando estándares modernos de programación como el tipado estático y funciones de orden superior.

## Contexto y Marco Lógico

La lógica clásica estándar opera bajo un marco bivalente estricto: las proposiciones son rotundamente Verdaderas o rotundamente Falsas. Sin embargo, la ciencia de la computación, la gestión de bases de datos y la filosofía a menudo se enfrentan a escenarios con **información incompleta** (lagunas/gaps) o **datos inconsistentes/contradictorios** (excesos/gluts).

Para modelar esto, implementamos **FDE (First-Degree Entailment)**, un sistema lógico de 4 valores. En lugar de utilizar primitivos booleanos simples, los valores de verdad se modelan mediante un enfoque de teoría de conjuntos (implementados como listas de Python):

* **`[1]` (Verdadero):** Estrictamente Verdadero.
* **`[0]` (Falso):** Estrictamente Falso.
* **`[1, 0]` (Ambos / Glut):** Información inconsistente (verdadero y falso simultáneamente, usado en Lógicas Paraconsistentes como **LP**).
* **`[]` (Ninguno / Gap):** Información faltante o indeterminada (usado en Lógicas Parciales como **K3**).

### Sistemas Modelados:
1.  **FDE:** Sistema central de 4 valores que contiene todos los subconjuntos de $\{0, 1\}$.
2.  **LP (Logic of Paradox):** Sistema paraconsistente de 3 valores (excluye el conjunto vacío `[]`).
3.  **K3 (Kleene's Strong Logic):** Sistema de 3 valores capaz de manejar entradas indefinidas (excluye el exceso `[1, 0]`).

---

## Características Clave y Arquitectura del Código

* **Diseño DRY (Don't Repeat Yourself):** Construido alrededor de una única y robusta función de orden superior (`print_binary_table`) que acepta cualquier dominio lógico y cualquier función de operador, eliminando la redundancia en el código.
* **Type Hinting (Pistas de Tipo):** Totalmente compatible con el módulo `typing` de Python (`Callable`, `List`), lo que garantiza una alta legibilidad, autocompletado en IDEs y preparación para análisis estático.
* **Operadores Exhaustivos:** Incluye conectivas lógicas estándar (Negación, Conjunción, Disyunción), múltiples modelos de Condicional (implicación material estándar vs. Condicional Estricto basado en identidad), Bicondicional y OR Exclusivo (XOR) extrapolados a un dominio de 4 valores.
* **Punto de Entrada Listo para Producción:** Estructurado utilizando el bloque estándar `if __name__ == "__main__":` para permitir una integración limpia como módulo de terceros sin efectos secundarios.

---

## Cómo Empezar

### Prerrequisitos
* Python 3.9 o superior.

### Instalación y Ejecución
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/non-classical-logic-interpreter.git](https://github.com/TU_USUARIO/non-classical-logic-interpreter.git)
   cd non-classical-logic-interpreter

2. Ejecuta el script generador de tablas de verdad: 
```Bash
python FDE_truth_tables.py
```

### Ejemplo de Salida
```Plaintext
--- Tabla: AND (FDE) ---
     A           B        A AND B   
------------------------------------
    [1]         [1]         [1]     
    [1]       [1, 0]      [1, 0]    
    [1]         []          []      
    [1]         [0]         [0]     
  [1, 0]        [1]       [1, 0]    
  [1, 0]      [1, 0]      [1, 0]    
  ...
```
## Licencia
Este proyecto es de código abierto y está disponible bajo la Licencia MIT.