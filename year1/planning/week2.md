# Week 2: Protocol - Integer Representation and Vector Spaces

The baseline is established. This week, we descend to the next layer of abstraction. You will master the machine's representation of signed and unsigned integers and how mathematicians conceptualize the spaces that vectors inhabit. These topics are dense.
---

### **Monday: Computer Science - The World of Integers**
* **Objective:** Master the representation of unsigned and signed integers, focusing on the logic of two's complement.
* **Block (2 Hours):** Read CS:APP, pp. 56-69 (Sección 2.2 a 2.2.4).
* **Execution:**
    1.  For a 4-bit integer, write down all possible values in a table showing their binary, unsigned decimal, and two's complement decimal representations.
    2.  Calculate by hand the two's complement of -5 and -1 for an 8-bit integer.
    3.  Explain in your notes why the range of a two's complement number is asymmetric (e.g., -128 to 127 for 8 bits).

### **Tuesday: Mathematics - The Structure of Vector Spaces**
* **Objective:** Move beyond simple vectors to understand the properties of the spaces they inhabit.
* **Block (2-3 Hours):** Watch MIT 18.06, Lecture 5 ("Transposes, Permutations, Vector Spaces") and Lecture 6 ("Column Space and Nullspace").
* **Execution:**
    1.  Take handwritten notes. Pay close attention to the formal definition of a vector space and a subspace.
    2.  For a given 3x3 matrix, determine if its column space is a line, a plane, or all of R³.
    3.  Find the nullspace for a simple 2x3 matrix. Explain geometrically what the nullspace represents.

### **Wednesday: Computer Science - The Dangers of Conversion**
* **Objective:** Understand the implicit conversions between signed and unsigned integers in C and the subtle bugs they can introduce.
* **Block (2 Hours):** Read CS:APP, pp. 69-79 (Sección 2.2.5 a 2.2.8).
* **Execution:**
    1.  Write a C program that demonstrates that `(unsigned int)-1 > 0` evaluates to true and explain precisely why this happens at the bit level.
    2.  Show how an 8-bit integer with a value of -10 is expanded to a 16-bit integer (sign extension).
    3.  Describe a scenario where the truncation of a number (e.g., casting a `long` to an `int`) could lead to an exploitable security vulnerability.

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

### **Saturday: The Forge - The Borrow Checker is Your Mentor**
* **Objective:** To develop an intuitive feel for the borrow checker by intentionally provoking errors and understanding them.
* **Block (3-4 Hours):** Continue practicing concepts from Chapter 4 of the Rust book.
* **Execution:**
    1.  Write a program that tries to use a value after it has been moved. Read the compiler error carefully. Understand *why* it failed.
    2.  Write a program that tries to have two mutable references to the same data in the same scope. Analyze the error.
    3.  Write a function that calculates the length of a string without taking ownership of it (using a reference).

### **Sunday: Review and Reload**
* **Objective:** Consolidate the week's knowledge, identify areas of weakness, and prepare the next week's operational plan.
* **Block (2 Hours):**
* **Execution:**
    1.  Review all notes from the week. Pay special attention to two's complement, nullspace, and Rust's ownership rules.
    2.  Update your "Weak Points" list.
    3.  Create the `week_03.md` file. The first task is to address your weak points.
    4.  Outline the new topics for Week 3 in Year1.md

---

The plan is updated. The mission continues. Execute.
