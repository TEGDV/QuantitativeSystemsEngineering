## CS:APP 2nd Edition - Assault Protocol

This book is the doctrinal backbone for Year 1 systems knowledge. It will be approached methodically, one chapter per month, to ensure deep mastery over superficial understanding.

### **Preliminary Mission: Chapter 1 - Reconnaissance**

Chapter 1, "A Tour of Computer Systems," is a high-level operational overview. **Read it once, quickly, for context.** Do not get bogged down in details. Its purpose is to give you a map of the territory you will explore in depth in the following chapters. You have already covered it in Week 1. Refer back to it only if you need to recall how the pieces fit together.

### **Month 1: Chapter 2 - Representing Information**

This is the true starting point. The objective is to master how data exists at the bit level. The chapter is divided into a four-week assault.

* **Week 1: Foundations of Representation**
    * **Monday:** Read pp. 29-46 (Section 2.1.1 to 2.1.4).
        * **Focus:** Hexadecimal notation, `word size`, and byte ordering (endianness).
    * **Wednesday:** Read pp. 46-56 (Section 2.1.5 to 2.1.10).
        * **Focus:** String representation, bit-level operations (`&`, `|`, `^`, `~`), and shift operations (`<<`, `>>`).

* **Week 2: Integer Representation**
    * **Monday:** Read pp. 56-69 (Section 2.2 to 2.2.4).
        * **Focus:** Unsigned integers and the logic of two's complement for signed integers.
    * **Wednesday:** Read pp. 69-79 (Section 2.2.5 to 2.2.8).
        * **Focus:** Conversions between signed/unsigned, sign extension, and the dangers of truncation.

* **Week 3: Integer Arithmetic**
    * **Monday:** Read pp. 79-88 (Section 2.3 to 2.3.3).
        * **Focus:** Two's complement addition, subtraction, and negation; overflow detection.
    * **Wednesday:** Read pp. 88-99 (Section 2.3.4 to 2.3.8).
        * **Focus:** Multiplication and the optimization of division by powers of two via shifts.

* **Week 4: Floating-Point Arithmetic**
    * **Monday:** Read pp. 99-110 (Section 2.4 to 2.4.3).
        * **Focus:** Fractional binary representation and the IEEE 754 standard (sign, exponent, fraction).
    * **Wednesday:** Read pp. 110-118 (Section 2.4.4 to 2.5).
        * **Focus:** Rounding modes, floating-point operations, and the nature of precision errors.

---
* Homework problems (pp. 119 - 134)
* Solutions (pp. 134 - 151)

### **Month 2: Chapter 3 - Machine-Level Program Representation**

This month, you move from *what* data is to *how* the machine acts upon it. The objective is to learn to read and understand x86-64 assembly language. This is not an academic exercise; it is the process of learning the machine's native tongue. The pace is aggressive. It requires absolute focus.

* **Week 5: Assembly Fundamentals**
    * **Monday:** Read pp. 156-177 (Sections 3.1 to 3.4).
        * **Focus:** Program encodings, data formats, accessing information, and the roles of the primary integer registers.
    * **Wednesday:** Read pp. 177-199 (Sections 3.5 to 3.6).
        * **Focus:** Arithmetic and logical operations (`leaq`, `add`, shifts) and the fundamentals of control flow (condition codes, jumps).

* **Week 6: Procedures and Arrays**
    * **Monday:** Read pp. 200-218 (Section 3.7).
        * **Focus:** The run-time stack, control transfer (`call`/`ret`), and register usage conventions for procedures.
    * **Wednesday:** Read pp. 219-240 (Section 3.8).
        * **Focus:** Array allocation, pointer arithmetic, and the layout of nested and variable-sized arrays in memory.

* **Week 7: Data Structures and Pointers**
    * **Monday:** Read pp. 241-253 (Section 3.9 to 3.10).
        * **Focus:** The memory layout of `structs` and `unions`, data alignment, and a consolidated understanding of pointers.
    * **Wednesday:** Read pp. 254-266 (Sections 3.11 to 3.12).
        * **Focus:** Practical use of the GDB debugger and the critical security implications of buffer overflow vulnerabilities.

* **Week 8: x86-64 and Floating Point**
    * **Monday:** Read pp. 267-280 (Section 3.13).
        * **Focus:** The extension to 64-bit, how information is accessed, and control flow in x86-64.
    * **Wednesday:** Read pp. 280-294 (Sections 3.13 to 3.15).
        * **Focus:** Data structures in x86-64, machine-level representation of floating-point programs, and the chapter summary.

---
* **Homework Problems:** (pp. 294 - 308)
* **Solutions to Practice Problems:** (pp. 308 - ...)
