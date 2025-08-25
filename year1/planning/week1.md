# Week 1: Protocol - Zeroing the Sights

This is the operational mandate for the first seven days. The objective is singular: establish a rhythm of deep work in the two core pillars of this year—Computer Systems and Mathematics. Distractions are eliminated. The 2-4 hour block is a non-negotiable commitment.

Adherence to the schedule is the only metric for success this week. The work must be done.

---

### **Monday: Computer Science - The Life of a Program**
* **Objective:** To trace a program from a human-readable file to executable machine code. You must understand the full journey.
* **Block (2-4 Hours):** Read *Computer Systems: A Programmer's Perspective* (CS:APP), Chapter 1: "A Tour of Computer Systems."
* **Execution:**
    1.  Read the chapter actively, with a notebook.
    2.  Type, compile, and run the `hello.c` program yourself. Use `gcc -o hello hello.c`.
    3.  Use the commands shown (`cpp`, `cc1`, `as`, `ld`) to see the intermediate files. Do not skip this step. It is critical.
    4.  Write a one-page summary explaining the roles of the preprocessor, compiler, assembler, and linker. If you cannot explain it simply, read the chapter again.

### **Tuesday: Mathematics - The Geometry of Equations**
* **Objective:** To visualize linear equations not as abstract algebra, but as geometric objects: lines, planes, and their intersections.
* **Block (2-3 Hours):** Watch MIT 18.06 Linear Algebra, Lecture 1 ("The Geometry of Linear Equations") and Lecture 2 ("Elimination with Matrices").
* **Execution:**
    1.  Take handwritten notes. The physical act of writing aids memory.
    2.  For a 2x2 system, draw the row picture (intersecting lines) and the column picture (vector addition). Do this for a system with one solution, no solution, and infinite solutions.
    3.  Perform Gaussian elimination on a 3x3 system by hand. Show your work.

### **Wednesday: Computer Science - Bits, Bytes, and Integers**
* **Objective:** To understand how information is represented at the lowest level.
* **Block (2-3 Hours):** Read CS:APP, Chapter 2, Sections 2.1-2.3 ("Information is Bits + Context", "Integral Representations").
* **Execution:**
    1.  Work through the conversions between binary, decimal, and hexadecimal by hand.
    2.  Explain the difference between signed (two's complement) and unsigned integers.
    3.  Write down the range of values that can be represented by an 8-bit and a 32-bit signed integer.

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
    6.  Organize your project directory structure as defined in the Year 1 `README.md`.

### **Saturday: The Forge - Basic Training**
* **Objective:** To move from "hello, world" to programs that perform logic. Solidify basic syntax and concepts.
* **Block (3-4 Hours):** Work through Chapter 3 of *The Rust Programming Language* ("Common Programming Concepts").
* **Execution:**
    1.  For every concept (variables, data types, functions, control flow), write a small, separate program in a `practice` directory to test it.
    2.  Build the three programs requested in the book:
        * Temperature converter.
        * Fibonacci number generator.
        * "The Twelve Days of Christmas" lyrics generator.
    3.  Attempt to write the temperature converter in C. Note the differences in syntax, type safety, and boilerplate. This contrast is important.

### **Sunday: Review and Reload**
* **Objective:** To assess the week's progress, identify weak points, and prepare for the next operational cycle.
* **Block (2 Hours):**
* **Execution:**
    1.  Read through every single note you took this week.
    2.  Create a "Weak Points" list. Write down the 1-3 concepts that you feel least confident about.
    3.  Create the `week_02.md` file. The first task for next week will be to attack the items on your "Weak Points" list before moving on to new material.
    4.  Outline the new topics for Week 2: CS:APP Ch. 2 (Floating Point), Math Lectures 5-6.

---

This is the standard. There is no deviation.
