# Year 1: The Foundation

## Mission Dossier

This year is not about building complex systems. It is about forging the steel from which those systems will be built. The mission for Year 1 is to achieve an uncompromising mastery of the absolute fundamentals. You will deconstruct the machine to its essential components—bits, memory addresses, and logic gates—and rebuild your understanding from first principles. You will internalize the mathematics of structure and the language of the machine.

This is the most important year. A weak foundation guarantees the collapse of any structure built upon it. There are no shortcuts here. The work is non-negotiable. Humility, discipline, and relentless execution are the only requirements.

---

## Core Objectives

By the end of this year, you will have demonstrated mastery in the following areas:

* **Computer Architecture & Systems:** You will understand how a program is compiled, linked, loaded, and executed by the hardware. You will be able to explain the memory hierarchy, process management, and system calls from a programmer's perspective.
* **Manual Memory Management (C):** You will write, debug, and manage non-trivial applications in C. You will master pointers, memory allocation (`malloc`/`free`), and the construction of fundamental data structures from scratch. This is not for production use; it is a tool to force a deep understanding of memory.
* **Linear Algebra:** You will not just "know" linear algebra. You will think in terms of vector spaces, matrix transformations, and eigenvalues. You will be able to solve systems and analyze their properties by hand and with code.
* **Foundational Rust:** You will achieve proficiency in Rust's core concepts: ownership, the borrow checker, structs, enums, and traits. You will understand *why* these concepts exist by contrasting them with the manual dangers of C.

---

## The Forge: Capstone Project

The culmination of Year 1 is the construction of a **Limit Order Book (LOB) Matching Engine.**

* **Phase 1: C Implementation.** You will first build the engine in C. This will force you to confront the raw challenges of performance, data structure design, and manual memory management in a high-stakes context.
* **Phase 2: Rust Implementation.** You will then rewrite the engine idiomatically in Rust. This exercise will cement the value of Rust's safety guarantees and modern abstractions, demonstrating how they prevent the classes of bugs you undoubtedly introduced in the C version.

This project was chosen because it is a microcosm of a trading system. It requires efficient data structures (for storing orders), algorithmic logic (for matching), and a focus on correctness. It is the perfect crucible to test this year's foundational skills.

---

## Directory Mandates

This directory is your operational base for the year. Its structure is not a suggestion.

* `./planning/`: Weekly execution protocols. Each file (`week_01.md`, `week_02.md`, etc.) will detail the specific reading, lectures, and coding tasks for that week. This is where strategy meets the calendar.
* `./notes/`: Your digital brain trust. All notes from books, lectures, and papers will be stored here, organized by subject. They must be clear, concise, and written in your own words.
* `./projects/`: The proof of work. This contains all code, from small practice programs to the final capstone project. Each sub-directory must have its own `README.md` explaining its purpose and how to build/run it.
* `./resources/`: A curated list of links, papers, and supplementary materials acquired throughout the year.

---

> "We are what we repeatedly do. Excellence, then, is not an act, but a habit."
>
> \- Aristotle

Discipline is a habit. Forge it here.
