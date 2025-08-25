# Week 2: Protocol - Machine Code and Vector Spaces

The baseline is established. This week, we descend to the next layer of abstraction. You will confront how the machine truly sees programs and how mathematicians conceptualize sets of vectors. These topics are denser. Se requiere un enfoque más profundo. No hay margen para la distracción.

---

### **Monday: Computer Science - The Deception of Floating Point**
* **Objective:** Master the IEEE 754 standard for floating-point representation. Understand its limitations and the nature of precision errors.
* **Block (2-4 Hours):** Read CS:APP, Chapter 2, Section 2.4 ("Floating-Point Representations").
* **Execution:**
    1.  Read the section twice. The first time for a general overview, the second time working through the examples with a calculator.
    2.  Take a simple decimal number like `0.75` and convert it to its 32-bit single-precision binary representation by hand. Show the sign bit, the exponent, and the fraction.
    3.  Write a paragraph explaining what a "denormalized" value is and why it's necessary.
    4.  Explain `rounding` in the context of floating point. This is critical for any form of quantitative work.

### **Tuesday: Mathematics - The Structure of Vector Spaces**
* **Objective:** Move beyond simple vectors to understand the properties of spaces they inhabit.
* **Block (2-3 Hours):** Watch MIT 18.06, Lecture 5 ("Transposes, Permutations, Vector Spaces") and Lecture 6 ("Column Space and Nullspace").
* **Execution:**
    1.  Take handwritten notes. Pay close attention to the definition of a vector space and a subspace.
    2.  For a given 3x3 matrix, determine if its column space is a line, a plane, or all of R³.
    3.  Find the nullspace for a simple 2x3 matrix. Explain geometrically what the nullspace represents.

### **Wednesday: Computer Science - First Contact with Assembly**
* **Objective:** To begin reading and understanding x86-64 assembly language. You will connect C code to the machine instructions it generates.
* **Block (2-3 Hours):** Read CS:APP, Chapter 3, Sections 3.1-3.4 ("A Little History", "Program Encodings", "Data Formats", "Accessing Information").
* **Execution:**
    1.  Compile a simple C function using `gcc -S`. Look at the `.s` file. Don't try to understand everything, but identify the function name, instructions (`mov`, `add`, etc.), and registers (`%rax`, `%rdi`, etc.).
    2.  Memorize the primary purpose of the key x86-64 registers: `%rax`, `%rbx`, `%rcx`, `%rdx`, `%rsi`, `%rdi`, `%rbp`, `%rsp`.
    3.  Write down the different addressing modes presented in Section 3.4. Create an example for each one.

### **Thursday: Mathematics - Reinforcement: The Four Subspaces**
* **Objective:** Solidify your understanding of the column space and nullspace, which are fundamental to all of linear algebra.
* **Block (2-3 Hours):** Re-watch Lecture 6. Dedicate the entire session to solving problems from the associated problem set.
* **Execution:**
    1.  For at least three different matrices, find a basis for their column space and their nullspace.
    2.  Create a matrix `A` where the vector `(1, 2, 3)` is in its column space.
    3.  Create a matrix `B` where the vector `(1, 1, 1)` is in its nullspace. Explain your reasoning.

### **Friday: The Forge - The Soul of Rust: Ownership**
* **Objective:** To understand Rust's core principle of ownership. This is the single most important concept to master.
* **Block (2-4 Hours):** Read and work through Chapter 4 of *The Rust Programming Language* ("Understanding Ownership").
* **Execution:**
    1.  Read the chapter without distraction. Type out every single code example and run it.
    2.  Draw diagrams showing how ownership is transferred when a variable is passed to a function.
    3.  Create examples that show the difference between a `move` and a `clone`.
    4.  Write a function that takes ownership of a string and another that "borrows" it via a reference.

### **Saturday: The Forge - The Borrow Checker is Your Mentor**
* **Objective:** To develop an intuitive feel for the borrow checker by intentionally provoking errors and understanding them.
* **Block (3-4 Hours):** Continue practicing concepts from Chapter 4 of the Rust book.
* **Execution:**
    1.  Write a program that tries to use a value after it has been moved. Read the compiler error carefully. Understand *why* it failed.
    2.  Write a program that tries to have two mutable references to the same data in the same scope. Analyze the error.
    3.  Write a function that calculates the length of a string without taking ownership of it.
    4.  Work with string slices. Write a function that takes a string and returns the first word.

### **Sunday: Review and Reload**
* **Objective:** Consolidate the week's knowledge, identify areas of weakness, and prepare the next week's operational plan.
* **Block (2 Hours):**
* **Execution:**
    1.  Review all notes from the week. Pay special attention to floating-point representation, nullspace, and Rust's ownership rules.
    2.  Update your "Weak Points" list.
    3.  Create the `week_03.md` file. The first task is to address your weak points.
    4.  Outline the new topics for Week 3: CS:APP Ch. 3 (Arithmetic & Control), Math Lectures 7-8.

---

The complexity will continue to increase. Your discipline must increase to meet it.
