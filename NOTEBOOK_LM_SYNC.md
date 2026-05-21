# 🧠 Syncing with Google NotebookLM & Study Routine Guide

This guide details how to connect this repository to Google NotebookLM for a seamless learning feedback loop, and how to optimize your **1 to 2 hours daily study routine** to maximize retention and progression.

---

## 🔄 NotebookLM Integration

Since Google NotebookLM does not natively integrate with Git repositories, we use a **single compiled master source file** approach. The repository is configured to automatically aggregate all scattered markdown notes, weekly planning files, and daily logs into a single structured file: `compiled_academic_notes.md`.

This file is automatically updated on GitHub every time you push changes to your `main` branch.

### How to Connect NotebookLM (Step-by-Step)

1. **Go to Google NotebookLM:**
   Open [NotebookLM](https://notebooklm.google/) and create a new notebook (e.g., "Quantitative Systems Engineering").
   
2. **Add the Source:**
   - Click **Add Source** (under the Sources panel).
   - Select **Link** / **Website**.
   - Paste the following **Public Raw GitHub URL** of your compiled notes file:
     ```text
     https://raw.githubusercontent.com/TEGDV/QuantitativeSystemsEngineering/main/compiled_academic_notes.md
     ```
   - Click **Add**. NotebookLM will fetch the entire document, parse the hierarchy, and index it.

3. **How to Sync New Notes (One-Click Refresh):**
   - Every time you finish a study session and push your new log or note to GitHub, the GitHub Action automatically runs `scripts/compile_notes.py` and pushes the updated `compiled_academic_notes.md` to GitHub.
   - Go to your NotebookLM notebook.
   - In the **Sources** panel, hover over the `compiled_academic_notes.md` source and click the **Refresh** icon (🔄).
   - NotebookLM will instantly pull the latest notes, updates, and daily logs into its active context!

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

This creates a file named `YYYY-MM-DD_log.md` (e.g. `2026-05-21_log.md`) in `year_01/quarter_01/notes/` containing:
- **Session Stats:** Date, Focus Area, Duration, and a Habit Checklist.
- **Theory & Reading:** Spaces for resources studied and key concepts.
- **Implementation & Practice:** Space for code snippets or commands run.
- **Questions & Next Focus:** Space for blockers and tomorrow's goals.

### 2. Compiling Notes Locally (`compile_notes.py`)

If you want to compile your notes locally to verify the structure or check the output before pushing:

```bash
python3 scripts/compile_notes.py
```
This traverses all folders in the repository, sorts all markdown files logically (by Year -> Quarter -> Category), shifts their headers to preserve hierarchy, and writes them into `compiled_academic_notes.md` in the root.

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
Once NotebookLM is loaded with your `compiled_academic_notes.md` context, use it to review and test yourself:
- **"Grill Me" Session:** Ask NotebookLM: *"Based on my study logs for the past week, quiz me on two's complement arithmetic and memory layout. Give me 3 exercises to solve."*
- **Explain the Gaps:** When you log a doubt under **Blockers/Doubts**, paste it to NotebookLM: *"Here is a blocker I logged today about epoll edge-triggered vs level-triggered behavior. Explain this using the context of my OSTEP notes."*
- **Concept Association:** Ask: *"How does the linear algebra concept I studied on Tuesday (nullspaces) relate to the systems programming topics I was working on last week?"*
- **Synthesized Study Guides:** Ask NotebookLM to generate a cheat-sheet or flashcards based on the notes you've taken so far.
