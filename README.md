# Quantitative Systems Engineering: A 7-Year Academic Mandate for Mastery

Este repositorio documenta mi campaña de autoestudio estructurada de **7 años** para adquirir un nivel de maestría y rigor equivalente a un Ph.D. en Ingeniería de Sistemas Cuantitativos (*Quantitative Systems Engineering*). Esta misión busca consolidar tres disciplinas en un solo perfil técnico y científico de élite: la rigurosidad abstracta de un matemático, el control físico del hardware de un programador de sistemas y el instinto empírico de un operador de mercado (*trader*).

Mi grado académico será este repositorio. Mi portafolio de investigación consistirá en la réplica de modelos y la creación de infraestructura crítica y de ultra-baja latencia documentada en este espacio.

---

## 📜 Filosofía de Estudio y Estructuración Plana

El aprendizaje a nivel doctoral de manera autodidacta requiere eliminar la fricción de navegación. Para evitar la sobrecarga cognitiva de sistemas de notas "atómicos" con directorios profundamente anidados, este repositorio adopta una **filosofía de organización plana**:

1. **Centralización Cuatrimestral**: En lugar de archivos semanales dispersos, la planeación y las notas se centralizan en documentos maestros de LaTeX por cada cuatrimestre académico.
2. **Jerarquía Simétrica**: El cuaderno de notas del cuatrimestre replica de forma exacta la jerarquía del planeador del trimestre correspondiente, permitiendo una correlación inmediata de la teoría y la práctica.
3. **Registro Práctico Directo**: Todos los desarrollos de software y proyectos de ingeniería se almacenan directamente en la raíz de la carpeta de ejercicios, organizados por proyectos específicos.

---

## 📅 Estructura de Tiempo No Negociable

El programa está diseñado con base en un presupuesto de **8.5 horas semanales** de enfoque absoluto y sin distracciones:

*   **Lunes a Viernes**: **1 hora diaria** dedicada a la asimilación de conceptos teóricos fundamentales y lecturas rápidas de pocket books (5 horas totales).
*   **Sábado**: **3 horas consecutivas** de desarrollo práctico y codificación deliberada en *La Forja* (capstones y proyectos de código).
*   **Domingo**: **30 minutos** reservados exclusivamente para la revisión de la semana finalizada, planeación detallada del próximo ciclo cuatrimestral y ajustes organizativos en LaTeX.

---

## 🗺️ La Estructura de Carpetas del Repositorio

El espacio de trabajo se organiza formalmente en únicamente **4 directorios** en la raíz del repositorio:

```text
QuantitativeSystemsEngineering/
├── Documentos/    # Manuales, plantillas base y libros de referencia en PDF.
├── Ejercicios/    # Carpetas de proyectos de código y exámenes/cuestionarios .tex.
├── Notas/         # Cuadernos de apuntes teóricos en LaTeX (.tex) y bitácoras cuatrimestrales.
└── Planeacion/    # Planes maestros y planificadores cuatrimestrales en LaTeX.
```

---

## 🏷️ Convenciones de Nomenclatura de Archivos y Carpetas

Para asegurar la legibilidad por agentes de Inteligencia Artificial y la consistencia editorial, se aplican estrictamente los siguientes patrones de nomenclatura:

### 1. Proyectos de Código y Prácticas (`Ejercicios/`)
*   **Carpetas de Ejercicios**: `Y{Año}Q{Cuatrimestre}_E{Número}_{nombre_descriptivo_con_guiones_bajos}`
    *   *Ejemplo*: `Ejercicios/Y1Q1_E02_detector_endianness/`
*   **Exámenes y Cuestionarios**: `Y{Año}Q{Cuatrimestre}_EXAMEN_{minor_o_materia}.tex` dentro de la subcarpeta del ejercicio correspondiente.
    *   *Ejemplo*: `Ejercicios/Y1Q1_E07_evaluaciones/Y1Q1_EXAMEN_ingles.tex`

### 2. Documentos Académicos y Libros (`Documentos/`)
*   **Libros y Manuales PDF**: `NOMBRE_DEL_LIBRO_EN_MAYUSCULAS_SIN_ESPACIOS.pdf`
    *   *Ejemplo*: `Documentos/Books/COMPUTERSYSTEMS_PROGRAMMER_PERSPECTIVE_3ED.pdf`
*   **Plantillas Base LaTeX**: `PLANTILLA_GENERAL_CON_EJEMPLOS.tex`, `TEMPLATE_CUADERNO_NOTAS.tex`, `TEMPLATE_PLANNER_CUATRIMESTRAL.tex`.

### 3. Notas Teóricas y Bitácoras (`Notas/`)
*   **Cuadernos de Notas Cuatrimestrales**: `CUADERNO_NOTAS_Y{Año}Q{Cuatrimestre}.tex`
    *   *Ejemplo*: `Notas/CUADERNO_NOTAS_Y1Q1.tex`
*   **PDFs Compilados**: Se almacenan en la misma carpeta junto a su fuente `.tex` correspondiente.

### 4. Planificadores y Currículum
*   **Currículum Maestro**: Ubicado en la raíz del repositorio como [CURRICULUM.md](file:///home/templance1/QuantitativeSystemsEngineering/CURRICULUM.md).
*   **Planificadores Cuatrimestrales**: `PLANNER_CUATRIMESTRAL_Y{Año}Q{Cuatrimestre}.tex` dentro de `Planeacion/`.
    *   *Ejemplo*: `Planeacion/PLANNER_CUATRIMESTRAL_Y1Q1.tex`

---

## 🛠️ Herramientas Tecnológicas y Requerimientos de Software

El desarrollo práctico de esta campaña requiere un entorno Linux configurado para el desarrollo de sistemas de baja latencia y maquetación científica:

### 1. Entorno de Desarrollo y Edición
*   **Neovim (v0.9+)**: Configurado con Lua como editor principal.
*   **Vimtex**: Plugin de integración para Neovim que permite la compilación bajo demanda, resaltado y sincronización directa con el visor de PDF (desactivando la autocompilación y archivos synctex según directiva de optimización).
*   **LSPs (Language Server Protocol)**: Configuración de `rust-analyzer` (Rust), `clangd` (C/C++), `pyright` (Python) y `texlab` (LaTeX).

### 2. Compiladores y Runtimes
*   **LaTeX (Tectonic Engine)**: Compilador moderno y autocontenido de LaTeX que descarga dependencias y paquetes dinámicamente, asegurando consistencia entre entornos.
*   **C y C++ Compiler (GCC / Clang)**: Soporte completo para estándares modernos (C11, C++20) y depuración nativa con `gdb` o `lldb`.
*   **Rust (Rustup / Cargo)**: Cadena de herramientas nativa de Rust en versión estable para desarrollo concurrente y asíncrono.
*   **Python (v3.10+)**: Utilización del gestor de paquetes de alto rendimiento `uv` o `pip` para análisis matemático mediante `pandas` / `polars`.
*   **Lua (v5.1+)**: Motor de scripting ligero utilizado para la configuración avanzada de buffers en Neovim.

### 3. Utilidades de Sistema y Control
*   **Git**: Control de versiones estricto de todos los desarrollos teóricos y prácticos.
*   **GNU Coreutils**: Herramientas estándar de terminal Linux para manipulación e inspección de datos.
*   **poppler-utils**: Para herramientas como `pdftoppm` utilizadas para verificar layouts compilados.

---

## 📚 El Arsenal de Recursos: Ediciones Críticas y Pocket Guides

Para optimizar la hora diaria de estudio teórico, se complementan los textos principales con guías de bolsillo (*Pocket Guides*) de lectura rápida para asimilar la intuición conceptual antes de abordar el rigor formal:

### 1. Computación y Sistemas
*   **Textos Principales**:
    *   *Computer Systems: A Programmer's Perspective (CS:APP)*, 3rd Edition (Bryant \& O'Hallaron) – Enfocado exclusivamente en x86-64.
    *   *Operating Systems: Three Easy Pieces (OSTEP)*, Versión 1.10 (Arpaci-Dusseau) – Virtualización, concurrencia y persistencia.
    *   *The C++ Programming Language*, 4th Edition (Bjarne Stroustrup) – El manual de referencia definitivo de C++ moderno.
*   **Pocket Guides \& Recursos de Concepto Rápido**:
    *   *Linux Pocket Guide*, 4th Edition (Daniel J. Barrett) – Referencia rápida de comandos y administración de sistemas.
    *   *C Pocket Reference* (Peter Prinz) – Lógica y sintaxis de C al instante.
    *   *C++ Pocket Reference* (Kyle Loudon) – Estructura de C++ moderno.

### 2. Matemáticas y Algoritmos
*   **Textos Principales**:
    *   *Introduction to Linear Algebra*, 6th Edition (Gilbert Strang, 2023) – Integración de optimización y deep learning.
    *   *Introduction to Algorithms (CLRS)*, 4th Edition (Cormen, Leiserson, Rivest, Stein, 2022) – Estructuras y análisis de complejidad.
*   **Pocket Guides \& Recursos de Concepto Rápido**:
    *   *Linear Algebra Done Right*, 4th Edition (Sheldon Axler, 2024) – Enfoque conceptual y teórico de espacios vectoriales sin determinantes iniciales.
    *   *Grokking Algorithms*, 2nd Edition (Aditya Bhargava, 2024) – Explicación visual y de alta velocidad de estructuras de datos básicas.

### 3. Sistemas de Sistemas, Lenguajes y Maquetación
*   **Textos Principales**:
    *   *The Rust Programming Language*, 2nd Edition (Klabnik \& Nichols).
    *   *Rust for Rustaceans*, 1st Edition (Jon Gjengset) – Conceptos avanzados de Rust (lifetimes, unsafe, macros, async).
    *   *Rust Atomics and Locks*, 1st Edition (Mara Bos) – Modelos de memoria concurrentes y primitivas de sincronización.
    *   *Asynchronous Programming in Rust (Async Rust)* (Official Working Group) – Desarrollo concurrente asíncrono.
    *   *The LaTeX Companion: Parts I \& II*, 3rd Edition (Mittelbach \& Fischer, 2023) – La biblia definitiva de maquetación en LaTeX.
    *   *Unix Network Programming, Vol. 1*, 3rd Edition (W. Richard Stevens) – APIs de Sockets.
    *   *Designing Data-Intensive Applications*, 1st Edition (Martin Kleppmann).
*   **Pocket Guides \& Recursos de Concepto Rápido**:
    *   *Command-Line Rust* (Ken Youens-Clark) – Diseño y desarrollo práctico de herramientas CLI robustas en Rust.
    *   *Effective Rust: 35 Specific Ways to Improve Your Rust Code* (Alastair Reid) – Guía práctica de mejores prácticas en Rust.
    *   *Rust Cheat Sheet* (rust-cheatsheet.ch) – Referencia de memoria y borrow checker.

### 4. Microestructura Financiera y Machine Learning
*   **Textos Principales**:
    *   *Trading and Exchanges: Market Microstructure for Practitioners*, 1st Edition (Larry Harris) – Dinámica de órdenes y liquidez.
    *   *Advances in Financial Machine Learning*, 1st Edition (Marcos López de Prado) – Modelos financieros avanzados.
    *   *Causality and Factor Investing: A Primer* (Marcos López de Prado, 2023) – Modelado causal de factores de inversión.
*   **Pocket Guides \& Recursos de Concepto Rápido**:
    *   *Machine Learning for Asset Managers* (Marcos López de Prado, 2020) – Versión conceptual y concisa de aplicación.

---

## 🏛️ Los Minors (Estudios Especializados Opcionales)

A la par de la línea de investigación principal (*Major*), cursaré **Minors** específicos diseñados para optimizar mi arsenal operativo:

1.  **Edición y Mantenimiento de Documentos con Neovim + LaTeX**: Dominio de Neovim y atajos de teclado para eliminar la fricción entre el pensamiento y el registro escrito técnico.
2.  **Inglés Técnico Avanzado**: Desarrollo de la fluidez y redacción académica para la lectura fluida de papers científicos y aportaciones en la comunidad global de desarrollo.

---

## 📞 Datos de Contacto y Operación

*   **Autor**: Jair Aguilar Peña
*   **Email**: apjair97@gmail.com
*   **Sitio Web**: jap_kode.pro (WIP)
*   **Herramienta de Registro**: NotebookLM sincronizado de manera automatizada con el archivo unificado de notas cuatrimestrales compilado en PDF.
