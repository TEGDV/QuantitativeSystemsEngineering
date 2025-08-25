High level c -> `program.c`
low level C -> any binary file compiled

to compile a 
low level C - any binary file compiled

to compile a `.c` file into binary we use `gcc`.
common compile command.

`gcc -o <bin_name> <c_file>` example `gcc -o hello hello.c`

the `gcc` command its an interface to run linked commands:

1. preprocersor `cpp` (converts `.c` files into a modified source program `.i`) modifies directives like #include <stdio.h> reads the his content and insert that content directly in the `.i` resulting file.
2. A compiler `cc1` turns the text modified program into assembly program Text. Converts the `.i` into a text Assembly code litterallly the byte code represented on the numerial bit representation as Text.
3. An Assembler `as` tool turns assembly text file (`.s`) into a relocable object program ( `.o` binary) instead of characters character representation the Assembler stores these bytes in a space memory to write the real Assembly Instructions.
4. A linker `ld` that turn the re-locable program into an executable binary file. i.e `hello` binary file no-extention.


# 1.4 Processors Reand And interpret instructions stored memory


Buses. The electrical connection around a computer where the bytes are carried between components. Buses are desingned to transfer fixed size chinks of bytes known as *words*. Most machines today uses either 4 bytes (32bits) or 8 bytes (64 bits).

I/O devices. Systems connection to the external world. keyobard, mouse, a display , a disk drive, etc.

Main memory. is a temporary storage. Memory is organized as a linear array f bytes. each with its own unique adress (array index) starting at 0.

CPU. central progracessing unit, is the engine that interprets or executes instructions stored in main memory.
  - At is core is a word sized storae device or register called *program counter*.
  - PC points at some chenie language intruction in main memory.
  - 

ALU. Aritmetic/Logic unit.

Common Processing Unit instructions:
- load: copu a byte or a word from main memory into a register, overwriting the previous contents of the register.
- Store: Copy a bute ot a word from a register to a location in main moemory, overwriting the previous contents of the register.
- Operate: Copyu the contents of two register to the ALU, perform an arthmetic operation the two words. and store the result in a register, overwriting the previous contents of that register.
- Jump: Extract a word from the instruction itself and copy that word in the program counter (PC), overwriting the previous value of the PC.


Save temporary files of compilation for C programs:

`gcc -save-temps <input> -o <ouput_bin>`

## Summary
---
`preprocersor` its the responsible of remove coments and ingest built-in code like stdio.h types and functions.

`compiler` its the responsible of optimize the code by re arraging instructions to result into an assembly code, also checks for errors before this previous step and generate the corresponding AS code for the target Architecture (i.e ARM, x86-64).

`Assembler` Transform the `.s` assembly code file into machine code that its a collections of 1 and 0.

`Linker` this is one of the most powerful stages. Since modern compiler don't write all the code into binaries to don't repeat instruction the linker bind some known utilities directly from the System ROM or Drivers and instead of write a new block of code in the binary the binary writes a instruction to execute the already existing instruction.


