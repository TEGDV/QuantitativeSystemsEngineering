# 🧠 Syncing with Google NotebookLM & Study Routine Guide

This guide details how to connect this repository to Google NotebookLM for a seamless learning feedback loop, and how to optimize your **1 to 2 hours daily study routine** to maximize retention and progression.

---

## 🔄 NotebookLM Integration

Since Google NotebookLM does not natively integrate with Git repositories, we compile our notes into a **unified professional PDF** (`compiled_academic_notes.pdf`). The repository is configured to automatically aggregate all scattered LaTeX fragment notes, weekly planning files, and daily logs, wrap them in a master academic template, and compile them to a PDF.

This PDF file is automatically updated on GitHub every time you push changes to your `main` branch.

### How to Connect NotebookLM (Step-by-Step)

1. **Go to Google NotebookLM:**
   Open [NotebookLM](https://notebooklm.google/) and create a new notebook (e.g., "Quantitative Systems Engineering").
   
2. **Add the Source:**
   - Click **Add Source** (under the Sources panel).
   - Select **Link** / **Website**.
   - Paste the following **Public Raw GitHub URL** of your compiled PDF file:
     ```text
     https://raw.githubusercontent.com/TEGDV/QuantitativeSystemsEngineering/main/compiled_academic_notes.pdf
     ```
   - Click **Add**. NotebookLM will fetch the PDF, parse the mathematical formulas and code blocks beautifully, and index it.
   - *Alternative:* You can also download `compiled_academic_notes.pdf` from your repository and upload it directly to NotebookLM as a PDF file, or upload it to Google Drive and connect it.

3. **How to Sync New Notes (One-Click Refresh):**
   - Every time you finish a study session and push your new log or note to GitHub, the GitHub Action automatically runs `scripts/compile_notes.py` using **Tectonic** to compile the LaTeX into `compiled_academic_notes.pdf` and pushes it back to GitHub.
   - Go to your NotebookLM notebook.
   - In the **Sources** panel, hover over the `compiled_academic_notes.pdf` source and click the **Refresh** icon (🔄).
   - NotebookLM will instantly pull the latest PDF, updating its context with your new math practice, notes, and study logs!

---

## 🛠️ Local Tools Guide

We have created two helper scripts in the `scripts/` directory to manage your studies locally.

### 1. Generating a Daily Study Log (`new_log.py`)

Create a pre-formatted study template for today to structure your study session and logs:

```bash
# Create a log for the latest active year/quarter notes directory
python3 scripts/new_log.py

# Create a log for a specific year (e.g., Year 1)
python3 scripts/new_log.py 1

# Create a log for a specific year and quarter (e.g., Year 1, Quarter 1)
python3 scripts/new_log.py 1 1
```

This creates a file named `YYYY-MM-DD_log.tex` (e.g. `2026-05-21_log.tex`) in `year_01/quarter_01/notes/` containing a pre-formatted LaTeX fragment with daily metrics, check lists, and a Rust listing block.

### 2. Compiling Notes Locally (`compile_notes.py`)

If you want to compile your notes locally to verify the structure or check the output before pushing:

```bash
python3 scripts/compile_notes.py
```
This traverses all folders in the repository, sorts all LaTeX fragment files logically (by Year -> Quarter -> Category), groups them into chapters by path, wraps them in a master document preamble (with code highlight styles, link colors, and document geometry), and outputs `compiled_academic_notes.tex` (and compiles to `compiled_academic_notes.pdf` if local LaTeX compilers like `tectonic` or `pdflatex` are installed).

---

## ⏱️ Optimizing the 1-2 Hour Daily Study Routine

As a self-taught engineer building high-performance quantitative systems, consistency and structure are more important than long, unstructured study sessions. Here is how to make the most of 1 to 2 hours daily:

### 1. The 90-Minute Focus Block (Ideal Routine)
Divide your daily block into three phases:
- **Phase 1: Theory (30 Mins):**
  - Read OSTEP, CS:APP, or work through Gilbert Strang's Linear Algebra.
  - Jot down core concepts directly in a note file (e.g. `year1/notes/systems/...`).
- **Phase 2: The Forge / Implementation (50 Mins):**
  - Do not just read. Write code.
  - Implement a matching engine in C/Rust, run network socket benchmarks, or solve matrix elimination problems by hand.
  - If a concept is unclear, write a small code script in a projects directory to test it.
- **Phase 3: Log & Summarize (10 Mins):**
  - Run `python scripts/new_log.py 1` (if in Year 1).
  - Fill out the stats, copy-paste any relevant terminal output or code snippets, and record blockers.
  - Commit and push to GitHub.

### 2. Leverage NotebookLM as an Active Mentor
Once NotebookLM is loaded with your `compiled_academic_notes.pdf` context, use it to review and test yourself:
- **"Grill Me" Session:** Ask NotebookLM: *"Based on my study logs for the past week, quiz me on two's complement arithmetic and memory layout. Give me 3 exercises to solve."*
- **Explain the Gaps:** When you log a doubt under **Blockers/Doubts**, paste it to NotebookLM: *"Here is a blocker I logged today about epoll edge-triggered vs level-triggered behavior. Explain this using the context of my OSTEP notes."*
- **Concept Association:** Ask: *"How does the linear algebra concept I studied on Tuesday (nullspaces) relate to the systems programming topics I was working on last week?"*
- **Synthesized Study Guides:** Ask NotebookLM to generate a cheat-sheet or flashcards based on the notes you've taken so far.
