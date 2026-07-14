# Non-Classical Logics & Many-Valued Truth Tables Interpreter

A Python implementation of an evaluation engine and truth table generator for non-classical systems, specifically focusing on **First-Degree Entailment (FDE)**, Priest's **Logic of Paradox (LP)**, and Kleene's **Strong Three-Valued Logic (K3)**.

This project demonstrates how abstract algebraic and logical structures can be modeled in clean, modular Python using modern programming standards like static typing and high-order functions.

## Background & Logical Framework

Standard classical logic operates on a strict bivalent framework: propositions are either strictly True or strictly False. However, computer science, database management, and philosophy often encounter scenarios involving **incomplete information** (gaps) or **inconsistent/contradictory data** (gluts).

To model this, we implement **FDE (First-Degree Entailment)**, a 4-valued logic system. Instead of single boolean primitives, truth values are modeled using set-theoretical approaches (implemented as Python lists):

* **`[1]` (True):** Strictly True.
* **`[0]` (False):** Strictly False.
* **`[1, 0]` (Both / Glut):** Inconsistent information (true and false simultaneously, used in Paraconsistent Logics like **LP**).
* **`[]` (Neither / Gap):** Missing or indeterminate information (used in Partial Logics like **K3**).

### Modeled Systems:
1.  **FDE:** Core 4-valued system containing all subsets of $\{0, 1\}$.
2.  **LP (Logic of Paradox):** 3-valued paraconsistent system (excludes the empty set `[]`).
3.  **K3 (Kleene's Strong Logic):** 3-valued system capable of handling undefined inputs (excludes the glut `[1, 0]`).

---

## Key Features & Code Architecture

* **DRY (Don't Repeat Yourself) Design:** Built around a single, robust higher-order function (`print_binary_table`) that accepts any logical domain and any operator function, removing codebase redundancy.
* **Type Hinting:** Fully compliant with Python's `typing` module (`Callable`, `List`) ensuring high readability, IDE auto-completion, and static analysis readiness.
* **Comprehensive Operators:** Includes standard logical connectives (Negation, Conjunction, Disjunction), multiple Conditional models (Material implication vs. Identity-based Strict Conditional), Biconditional, and Exclusive OR (XOR) extrapolated to a 4-valued domain.
* **Production-Ready Entry Point:** Structured using the standard `if __name__ == "__main__":` block to allow clean integration as a third-party module without side effects.

---

## Getting Started

### Prerequisites
* Python 3.9 or higher.

### Installation & Execution
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/non-classical-logic-interpreter.git](https://github.com/YOUR_USERNAME/non-classical-logic-interpreter.git)
   cd non-classical-logic-interpreter
   
2. Run the truth table generator script:

```Bash
python FDE_truth_tables.py
```

### Example Output Sample
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

## License
This project is open-source and available under the MIT License.