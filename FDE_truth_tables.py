"""
FDE_truth_tables.py

Este módulo implementa y genera tablas de verdad para lógicas no clásicas 
plurivalentes: First-Degree Entailment (FDE), Logic of Paradox (LP) y 
Kleene's Strong Logic (K3).
"""

from typing import Callable, List

# Definición de los valores de verdad utilizando el enfoque de conjuntos (listas)
T: List[int] = [1]      # Solo Verdadero
F: List[int] = [0]      # Solo Falso
B: List[int] = [1, 0]   # Ambos (Both)
N: List[int] = []       # Ninguno (Neither)

# Dominios (Sistemas Lógicos)
FDE: List[List[int]] = [T, B, N, F]
LP: List[List[int]] = [T, B, F]
K3: List[List[int]] = [T, N, F]

CELL_WIDTH = 12

# ==========================================
# 1. OPERADORES LÓGICOS
# ==========================================

def four_valued_not(a: List[int]) -> List[int]:
    # Calcula la negación en FDE intercambiando 1 por 0 y viceversa.
    result = []
    if 0 in a:
        result.append(1)
    if 1 in a:
        result.append(0)
    return sorted(result, reverse=True)  # Mantiene consistencia visual [1, 0]


def four_valued_and(a: List[int], b: List[int]) -> List[int]:
    # Calcula la conjunción evaluando condiciones de verdad y falsedad.
    result = []
    # Verdadero si ambos componentes contienen la verdad (1)
    if 1 in a and 1 in b:
        result.append(1)
    # Falso si al menos uno contiene la falsedad (0)
    if 0 in a or 0 in b:
        result.append(0)
    return sorted(result, reverse=True)


def four_valued_or(a: List[int], b: List[int]) -> List[int]:
    # Calcula la disyunción en FDE.
    result = []
    if 1 in a or 1 in b:
        result.append(1)
    if 0 in a and 0 in b:
        result.append(0)
    return sorted(result, reverse=True)


def four_valued_condicional(a: List[int], b: List[int]) -> List[int]:
    # Condicional material estándar mapeado a 4 valores (~A OR B).
    result = []
    if 0 in a or 1 in b:
        result.append(1)
    if 1 in a and 0 in b:
        result.append(0)
    return sorted(result, reverse=True)


def four_valued_condicionalf(a: List[int], b: List[int]) -> List[int]:
    # Condicional implícito estricto basado en la identidad de conjuntos.
    # Las condiciones originales simplificadas y estructuradas de forma limpia
    es_verdadero = (a == b) or (1 not in a and 0 not in b) or (1 in b and 0 in a)
    
    result = []
    if es_verdadero:
        result.append(1)
    else:
        result.append(0)
    return result


def four_valued_bicondicional(a: List[int], b: List[int]) -> List[int]:
    # Bicondicional evaluado como (A -> B) AND (B -> A).
    cond1 = four_valued_condicional(a, b)
    cond2 = four_valued_condicional(b, a)
    return four_valued_and(cond1, cond2)


def four_valued_xor(a: List[int], b: List[int]) -> List[int]:
    # Disyunción exclusiva definida como (A OR B) AND NOT (A AND B).
    or_res = four_valued_or(a, b)
    and_res = four_valued_and(a, b)
    not_and_res = four_valued_not(and_res)
    return four_valued_and(or_res, not_and_res)


# ==========================================
# 2. MOTOR GENÉRICO DE TABLAS DE VERDAD
# ==========================================

def print_binary_table(logic_name: str, domain: List[List[int]], operator_symbol: str, 
                       operator_func: Callable[[List[int], List[int]], List[int]]) -> None:
    """
    Genera de forma genérica el formato impreso de cualquier tabla bivalente 
    para un dominio (sistema lógico) específico.
    """
    print(f"\n--- Tabla: {operator_symbol} ({logic_name}) ---")
    header = f"A".center(CELL_WIDTH) + "B".center(CELL_WIDTH) + f"A {operator_symbol} B".center(CELL_WIDTH)
    print(header)
    print("-" * len(header))
    
    for p in domain:
        for q in domain:
            result = operator_func(p, q)
            print(str(p).center(CELL_WIDTH) + str(q).center(CELL_WIDTH) + str(result).center(CELL_WIDTH))


# ==========================================
# 3. BLOQUE DE EJECUCIÓN PRINCIPAL
# ==========================================

if __name__ == "__main__":
    print("==================================================")
    # Ejemplo de operación unaria (Negación en FDE)
    print("Negación FDE:")
    print("A".center(CELL_WIDTH) + "NOT A".center(CELL_WIDTH))
    print("-" * (CELL_WIDTH * 2))
    for val in FDE:
        print(str(val).center(CELL_WIDTH) + str(four_valued_not(val)).center(CELL_WIDTH))
    
    # Pruebas de Operadores Binarios cruzando diferentes lógicas
    # Conjunción
    print_binary_table("FDE", FDE, "AND", four_valued_and)
    print_binary_table("LP", LP, "AND", four_valued_and)
    print_binary_table("K3", K3, "AND", four_valued_and)
    
    # Disyunción
    print_binary_table("FDE", FDE, "OR", four_valued_or)
    
    # Condicionales
    print_binary_table("FDE", FDE, "Condicional (->)", four_valued_condicional)
    print_binary_table("LP", LP, "Condicional (->)", four_valued_condicional)
    print_binary_table("K3", K3, "Condicional (->)", four_valued_condicional)
    print_binary_table("FDE", FDE, "Condicional F (->F)", four_valued_condicionalf)
    
    # Bicondicional y XOR
    print_binary_table("FDE", FDE, "Bicondicional (<->)", four_valued_bicondicional)
    print_binary_table("FDE", FDE, "Disyunción exclusiva (XOR)", four_valued_xor)
    print("\n==================================================")