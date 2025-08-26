# Week 1: Protocol - Foundations of Representation

This is the operational mandate for the first seven days. The objective is singular: establish a rhythm of deep work in the two core pillars of this year—Computer Systems and Mathematics. Distractions are eliminated. The 2-4 hour block is a non-negotiable commitment.

Adherence to the schedule is the only metric for success this week. The work must be done.

---

### **Monday: Computer Science - The Language of Memory**
* **Objective:** Master hexadecimal notation, the concept of "word size," and the critical distinction between big-endian and little-endian byte ordering.
* **Block (2 Hours):** Read CS:APP, pp. 29-41 (Sección 2.1.1 a 2.1.4).
* **Execution:**
    1.  Escribe un programa en C que declare una variable `int x = 0x01234567;` y luego imprima sus bytes individuales para determinar el endianness de tu máquina.
    2.  Convierte a mano los números decimales 15, 16, 255, y 256 a binario y hexadecimal.
    3.  Explica en tus notas por qué el byte ordering es un problema fundamental en la programación de redes.

### **Tuesday: Mathematics - The Geometry of Equations**
* **Objective:** To visualize linear equations not as abstract algebra, but as geometric objects: lines, planes, and their intersections.
* **Block (2-3 Hours):** Watch MIT 18.06 Linear Algebra, Lecture 1 ("The Geometry of Linear Equations") and Lecture 2 ("Elimination with Matrices").
* **Execution:**
    1.  Take handwritten notes. The physical act of writing aids memory.
    2.  For a 2x2 system, draw the row picture (intersecting lines) and the column picture (vector addition). Do this for a system with one solution, no solution, and infinite solutions.
    3.  Perform Gaussian elimination on a 3x3 system by hand. Show your work.

### **Wednesday: Computer Science - Bit-Level Manipulation**
* **Objective:** Entender cómo se representan las cadenas de caracteres y el código, y dominar las operaciones a nivel de bit en C.
* **Block (2 Hours):** Read CS:APP, pp. 46-56 (Sección 2.1.5 a 2.1.10).
* **Execution:**
    1.  Escribe una función en C que use máscaras de bits (`&`) y desplazamientos (`>>`) para extraer el byte más significativo de un entero de 32 bits.
    2.  Implementa la operación XOR (`^`) usando solo las operaciones AND (`&`) y NOT (`~`).
    3.  Explica la diferencia fundamental entre el desplazamiento lógico a la derecha y el desplazamiento aritmético a la derecha.

### **Thursday: Mathematics - Elimination and Inverses**
* **Objective:** To master the mechanics of matrix operations, the core machinery of linear algebra.
* **Block (2-3 Hours):** Watch MIT 18.06, Lecture 3 ("Multiplication and Inverse Matrices") and Lecture 4 ("Factorization into A = LU").
* **Execution:**
    1.  Multiply two 3x3 matrices by hand.
    2.  Find the inverse of a 2x2 matrix using the formula.
    3.  Take a 3x3 matrix and perform LU decomposition on it by hand.

### **Friday: The Forge - Armory and First Contact**
* **Objective:** To prepare your development environment and make first contact with your primary language. A warrior's weapon must be sharp and ready.
* **Block (2-3 Hours):**
* **Execution:**
    1.  Install a C compiler (GCC via MinGW, macOS Command Line Tools, or `build-essential` on Linux).
    2.  Install Rust via `rustup`.
    3.  Write, compile, and run `hello, world` in C.
    4.  Write, compile, and run `hello, world` in Rust using `rustc` directly.
    5.  Create a new project using `cargo new hello_cargo`, build it, and run it. Read the output to understand what Cargo is doing for you.

### **Saturday: The Forge - Basic Training**
* **Objective:** To move from "hello, world" to programs that perform logic. Solidify basic syntax and concepts.
* **Block (3-4 Hours):** Work through Chapter 3 of *The Rust Programming Language* ("Common Programming Concepts").
* **Execution:**
    1.  For every concept (variables, data types, functions, control flow), write a small, separate program in a `practice` directory to test it.
    2.  Build the three programs requested in the book:
        * Temperature converter.
        * Fibonacci number generator.
        * "The Twelve Days of Christmas" lyrics generator.

### **Sunday: Review and Reload**
* **Objective:** To assess the week's progress, identify weak points, and prepare for the next operational cycle.
* **Block (2 Hours):**
* **Execution:**
    1.  Read through every single note you took this week.
    2.  Create a "Weak Points" list. Write down the 1-3 concepts that you feel least confident about.
    3.  Create the `week_02.md` file. The first task for next week will be to attack the items on your "Weak Points" list.
    4.  Outline the new topics for Week 2 in Year1.md

---

The plan is updated. The mission is unchanged.
