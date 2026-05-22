#!/usr/bin/env python3
import os
import re
import subprocess
from datetime import datetime

# Configuration
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_TEX = os.path.join(REPO_ROOT, "compiled_academic_notes.tex")

# Folders/files to ignore during compilation
IGNORE_DIRS = {".git", ".github", "scripts", "node_modules", "venv", ".venv"}
IGNORE_FILES = {"compiled_academic_notes.tex"}

PREAMBLE = r"""\documentclass[11pt,a4paper]{report}
\usepackage[utf8]{inputenc}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{xcolor}
\usepackage{listings}
\usepackage{textcomp}
\usepackage{graphicx}
\usepackage{hyperref}

\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    urlcolor=cyan,
    pdftitle={Quantitative Systems Engineering: Compiled Notes and Logs},
    pdfauthor={Jair Aguilar Peña}
}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}
\definecolor{backcolour}{rgb}{0.95,0.95,0.92}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{backcolour},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    captionpos=b,                    
    keepspaces=true,                 
    numbers=left,                    
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=4
}

\lstset{style=mystyle}

\title{Quantitative Systems Engineering\\ \large Compiled Study Notes \& Logs}
\author{Jair Aguilar Peña}
\date{\today}

\begin{document}
\maketitle
\tableofcontents
\newpage
"""

def clean_relative_path(path):
    return os.path.relpath(path, REPO_ROOT)

def get_tex_files():
    """Traverses the repository and collects all latex fragment files under year directories, sorted logically."""
    tex_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        # Prune ignored directories in place
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        
        rel_root = os.path.relpath(root, REPO_ROOT)
        if rel_root == ".":
            continue
            
        parts = rel_root.split(os.sep)
        if not parts[0].startswith("year"):
            continue
            
        for file in files:
            if file.endswith(".tex") and file not in IGNORE_FILES:
                full_path = os.path.join(root, file)
                rel_path = clean_relative_path(full_path)
                tex_files.append((rel_path, full_path))
    
    # Sort files logically:
    # 1. By year directory (e.g., year1, year_01, year2)
    # 2. By subdirectories (quarter_01, planning, notes)
    # 3. By filename (e.g., YYYY-MM-DD_log.tex or alphabetical)
    def sorting_key(file_tuple):
        rel_path = file_tuple[0]
        parts = rel_path.split(os.sep)
        
        # Build a list of tuples for comparison: (has_numeric, numeric_value, original_string)
        # Folders with numbers will sort first (0), sorted by that number, then by string name.
        key_parts = []
        for part in parts:
            numbers = re.findall(r'\d+', part)
            if numbers:
                key_parts.append((0, int(numbers[0]), part))
            else:
                key_parts.append((1, 0, part))
        return (key_parts, rel_path)

    tex_files.sort(key=sorting_key)
    return tex_files

def insert_source_link(content, rel_path):
    github_url = f"https://github.com/TEGDV/QuantitativeSystemsEngineering/blob/main/{rel_path}"
    escaped_path = rel_path.replace('_', '\\_')
    link_tex = f"\n\\noindent\\textit{{Source Path: \\href{{{github_url}}}{{{escaped_path}}}}}\\\\\n"
    
    # Try to find the first \section
    m = re.search(r'(\\section\{.*?\})', content)
    if m:
        pos = m.end()
        return content[:pos] + link_tex + content[pos:]
    else:
        return link_tex + content

def compile_notes():
    tex_files = get_tex_files()
    if not tex_files:
        print("No latex fragment files found to compile.")
        return
    
    print(f"Found {len(tex_files)} LaTeX files. Compiling master document...")
    
    compiled_content = [PREAMBLE]
    
    current_breadcrumbs = None
    
    for rel_path, full_path in tex_files:
        print(f"Processing: {rel_path}")
        
        # Read the file
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue
        
        # Track breadcrumbs/chapters
        parts = rel_path.split(os.sep)
        breadcrumbs = parts[:-1]
        # Human readable and escaped for LaTeX
        breadcrumbs_str = " $\\rightarrow$ ".join([p.replace('_', ' ').title() for p in breadcrumbs])
        # Escape any special characters that title() might leave behind, though replace already handles _
        
        if breadcrumbs_str != current_breadcrumbs:
            current_breadcrumbs = breadcrumbs_str
            compiled_content.append(f"\n\\chapter{{{breadcrumbs_str}}}\n")
            
        # Insert Source Link
        processed_content = insert_source_link(content, rel_path)
        
        compiled_content.append(processed_content)
        compiled_content.append("\n\\newpage\n")
    
    compiled_content.append("\n\\end{document}\n")
    
    # Write to master file
    try:
        with open(OUTPUT_TEX, 'w', encoding='utf-8') as f:
            f.write("".join(compiled_content))
        print(f"Successfully compiled {len(tex_files)} fragment files into {OUTPUT_TEX}.")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        return

    # Attempt to compile to PDF
    print("Attempting to compile to PDF...")
    compiled = False
    for engine in [["tectonic", "compiled_academic_notes.tex"], ["pdflatex", "-interaction=nonstopmode", "compiled_academic_notes.tex"]]:
        try:
            print(f"Running {' '.join(engine)}...")
            res = subprocess.run(engine, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=REPO_ROOT)
            print("PDF compilation successful!")
            compiled = True
            break
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            continue
    if not compiled:
        print("Could not compile to PDF. Please ensure tectonic or pdflatex is installed.")

if __name__ == "__main__":
    compile_notes()
