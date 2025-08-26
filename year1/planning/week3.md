# Week 3: Protocol - Integer Arithmetic and The Complete Solution

This week, we move from how numbers are stored to how they are manipulated. You will implement the logic of integer arithmetic at the bit level. In parallel, you will master the complete algorithm for solving any system of linear equations, the computational core of countless scientific problems. The work requires precision.

---

### **Monday: Computer Science - The Logic of Addition**
* **Objective:** Understand addition, subtraction, and negation in complement a dos, including the critical concept of desbordamiento (overflow).
* **Block (2 Hours):** Read CS:APP, pp. 79-88 (Sección 2.3 a 2.3.3).
* **Execution:**
    1.  Realiza a mano la suma de 5 + 3 y 5 + 5 en complemento a dos de 4 bits, mostrando si ocurre desbordamiento y por qué.
    2.  Realiza a mano la resta 5 - 3 (calculada como 5 + (-3)) en complemento a dos de 4 bits.
    3.  Demuestra que negar el número más negativo en complemento a dos (ej. -8 en 4 bits) resulta en el mismo número, y explica la implicación de este caso límite.

### **Tuesday: Mathematics - Solving Ax = b**
* **Objective:** Master the complete algorithm for solving systems of linear equations, including cases with no solution or infinite solutions.
* **Block (2-3 Hours):** Watch MIT 18.06, Lecture 7 ("Solving Ax = 0: Pivot Variables, Special Solutions") and Lecture 8 ("Solving Ax = b: Row Reduced Form R").
* **Execution:**
    1.  Toma una matriz 3x4 `A` y encuentra la solución completa para `Ax = 0`. Esto implica encontrar las variables pivote y libres, y construir las soluciones especiales que forman el nullspace.
    2.  Usando la misma matriz `A` y un vector `b`, encuentra la solución completa para `Ax = b`.
    3.  Explica con tus propias palabras la relación entre la solución particular (una solución a Ax=b) y el nullspace (todas las soluciones a Ax=0).

### **Wednesday: Computer Science - Multiplication by Machine**
* **Objective:** Entender la multiplicación y la división por potencias de dos usando desplazamientos de bits, una optimización fundamental.
* **Block (2 Hours):** Read CS:APP, pp. 88-99 (Sección 2.3.4 a 2.3.8).
* **Execution:**
    1.  Multiplica 6 * 3 en binario sin signo de 4 bits, mostrando el resultado completo de 8 bits.
    2.  Escribe una función en C que multiplique un entero por 17 usando solo desplazamientos (`<<`) y sumas (`+`).
    3.  Explica cómo la división de un número negativo por una potencia de dos usando desplazamiento aritmético a la derecha (`>>`) difiere de la división matemática tradicional y cómo se puede corregir este sesgo.

### **Thursday: Mathematics - Independence, Basis, and Dimension**
* **Objective:** Solidify your understanding of linear independence, spanning, basis, and dimension—the core concepts describing the "size" y la estructura de un espacio vectorial.
* **Block (2-3 Hours):** Watch MIT 1.06, Lecture 9 ("Linear Independence, Basis, and Dimension"). Dedica la sesión a resolver problemas del problem set asociado.
* **Execution:**
    1.  Dado un conjunto de 3 vectores en R³, determina si son linealmente independientes.
    2.  Encuentra una base para el column space y una base para el nullspace de una matriz 3x4.
    3.  Para una matriz `m x n` de rango `r`, escribe las dimensiones de sus cuatro subespacios fundamentales (column space, nullspace, row space, left nullspace).

### **Friday: The Forge - Structuring Data**
* **Objective:** Learn how to create complex data types using structs in Rust. This is the foundation for building any non-trivial application.
* **Block (2-3 Hours):** Read and work through Chapter 5 of *The Rust Programming Language* ("Using Structs to Structure Related Data").
* **Execution:**
    1.  Define a `User` struct with fields like `username`, `email`, y `active`.
    2.  Write functions that toman una instancia del `User` struct como argumento.
    3.  Implementa métodos en el `User` struct usando un bloque `impl`. Crea un método que devuelva la información del usuario como un string formateado.

### **Saturday: The Forge - Structs in Action**
* **Objective:** Apply your knowledge of structs to a practical problem and explore more advanced features like tuple structs and debug printing.
* **Block (3-4 Hours):** Continue practicing concepts from Chapter 5 of the Rust book.
* **Execution:**
    1.  Crea un programa que calcule el área de un rectángulo, primero usando variables separadas, y luego refactorízalo para usar un `Rectangle` struct.
    2.  Refactoriza el programa de nuevo para usar métodos en el `Rectangle` struct, como `area()` y `can_hold()`.
    3.  Añade la anotación `#[derive(Debug)]` a tus structs y experimenta imprimiéndolos usando los especificadores de formato `{:?}` y `{:#?}`.

### **Sunday: Review and Reload**
* **Objective:** Consolidate the week's knowledge, identify areas of weakness, and prepare the next week's operational plan.
* **Block (2 Hours):**
* **Execution:**
    1.  Review all notes. Focus on integer overflow, the process of finding the complete solution to `Ax = b`, y la sintaxis de los métodos `impl` en Rust.
    2.  Update your "Weak Points" list.
    3.  Create the `week_04.md` file. The first task is to address your weak points.
    4.  Outline the new topics for Week 4 in Year1.md

---

The pace is deliberate. The standard is absolute. Execute.
