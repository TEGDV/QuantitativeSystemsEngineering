#!/usr/bin/env python3
import os
import sys
import re
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_latest_year_dir():
    """Finds the latest year directory in the repo (e.g., year_01, year2, etc.)."""
    pattern = re.compile(r'^year[_]?(\d+)$')
    years = []
    for d in os.listdir(REPO_ROOT):
        if os.path.isdir(os.path.join(REPO_ROOT, d)):
            match = pattern.match(d)
            if match:
                years.append((int(match.group(1)), d))
    
    if not years:
        return None
    
    # Sort by the numerical value of the year
    years.sort()
    return years[-1][1]

def get_latest_quarter_dir(year_dir):
    """Finds the latest quarter directory inside the year directory if it exists."""
    year_path = os.path.join(REPO_ROOT, year_dir)
    if not os.path.exists(year_path):
        return None
    pattern = re.compile(r'^quarter[_]?(\d+)$')
    quarters = []
    for d in os.listdir(year_path):
        if os.path.isdir(os.path.join(year_path, d)):
            match = pattern.match(d)
            if match:
                quarters.append((int(match.group(1)), d))
    
    if not quarters:
        return None
    
    quarters.sort()
    return quarters[-1][1]

def resolve_year_dir(year_input):
    """Resolves inputs like 1, '01', 'year1', 'year_01' to the matching repo folder."""
    if not year_input:
        return None
    digits = re.findall(r'\d+', str(year_input))
    if digits:
        year_num = int(digits[0])
    else:
        return None
        
    pattern = re.compile(rf'^year[_]?0*{year_num}$')
    for d in os.listdir(REPO_ROOT):
        if os.path.isdir(os.path.join(REPO_ROOT, d)):
            if pattern.match(d):
                return d
    return f"year_{year_num:02d}"

def resolve_quarter_dir(year_dir, quarter_input):
    """Resolves inputs like 1, '01', 'quarter1', 'quarter_01' inside year_dir."""
    if not quarter_input or not year_dir:
        return None
    digits = re.findall(r'\d+', str(quarter_input))
    if digits:
        quarter_num = int(digits[0])
    else:
        return None
        
    year_path = os.path.join(REPO_ROOT, year_dir)
    if not os.path.exists(year_path):
        return f"quarter_{quarter_num:02d}"
        
    pattern = re.compile(rf'^quarter[_]?0*{quarter_num}$')
    for d in os.listdir(year_path):
        if os.path.isdir(os.path.join(year_path, d)):
            if pattern.match(d):
                return d
    return f"quarter_{quarter_num:02d}"

def get_target_notes_dir():
    """Determines the target notes directory based on CLI args or existing folders."""
    year_arg = None
    quarter_arg = None
    
    # Parse positional arguments
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    if len(args) >= 1:
        year_arg = args[0]
    if len(args) >= 2:
        quarter_arg = args[1]
        
    if year_arg:
        target_year = resolve_year_dir(year_arg)
        print(f"Targeting Year: {target_year} (from argument '{year_arg}')")
    else:
        target_year = get_latest_year_dir()
        if not target_year:
            target_year = "year_01"
        print(f"Targeting Latest Year: {target_year} (pass argument to override, e.g., `python scripts/new_log.py 1`)")
            
    year_path = os.path.join(REPO_ROOT, target_year)
    
    if quarter_arg:
        target_quarter = resolve_quarter_dir(target_year, quarter_arg)
        print(f"Targeting Quarter: {target_quarter} (from argument '{quarter_arg}')")
    else:
        target_quarter = get_latest_quarter_dir(target_year)
        if target_quarter:
            print(f"Found Latest Quarter: {target_quarter}")
        
    if target_quarter:
        quarter_notes_path = os.path.join(year_path, target_quarter, "notes")
        if os.path.exists(quarter_notes_path):
            return quarter_notes_path
        # If notes dir doesn't exist but planning/projects does, let's create and use notes
        os.makedirs(quarter_notes_path, exist_ok=True)
        return quarter_notes_path
        
    year_notes_path = os.path.join(year_path, "notes")
    os.makedirs(year_notes_path, exist_ok=True)
    return year_notes_path

def create_daily_log():
    target_dir = get_target_notes_dir()
    today_str = datetime.now().strftime("%Y-%m-%d")
    log_filename = f"{today_str}_log.tex"
    log_filepath = os.path.join(target_dir, log_filename)
    
    rel_path = os.path.relpath(log_filepath, REPO_ROOT)
    
    if os.path.exists(log_filepath):
        print(f"Log file already exists: {rel_path}")
        print("Will not overwrite. Open it directly to make edits.")
        return
    
    # Create the directory structure if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    
    # Template contents
    template = f"""\\section{{Daily Study Log: {today_str}}}

\\subsection{{📊 Session Stats}}
\\begin{{itemize}}
  \\item \\textbf{{Date:}} {today_str}
  \\item \\textbf{{Focus Area:}} [e.g., Systems Programming / Linear Algebra / Rust]
  \\item \\textbf{{Time Invested:}} [e.g., 1 hour 45 minutes]
  \\item \\textbf{{Habit Checklist:}}
  \\item {{[ ]}} 📖 Reading \\& Theory Study
  \\item {{[ ]}} 🛠️ Hands-on coding/math problem solving
  \\item {{[ ]}} ✍️ Notes documented \\& compiled to NotebookLM
\\end{{itemize}}

\\noindent\\rule{{\\textwidth}}{{0.4pt}}

\\subsection{{📖 Theory \\& Reading Summary}}
\\textit{{What theoretical concepts did I cover today? Include book name/chapter and core notes.}}

\\begin{{itemize}}
  \\item \\textbf{{Topic/Resource:}} [e.g., CS:APP Chapter 2 - Representing and Manipulating Information]
  \\item \\textbf{{Key Concepts learned:}}
  \\item 
  \\item 
\\end{{itemize}}

\\noindent\\rule{{\\textwidth}}{{0.4pt}}

\\subsection{{🛠️ Implementation \\& Practice}}
\\textit{{What did I build, compile, profile, or debug today? Show code snippets, command lines, or math solutions.}}

\\begin{{itemize}}
  \\item \\textbf{{Task/Project:}} [e.g., Floating point conversions or Rust memory ownership exercise]
  \\item \\textbf{{Key Code/Output:}}
\\end{{itemize}}
\\begin{{lstlisting}}[language=Rust]
// Insert code snippets or terminal logs
\\end{{lstlisting}}
\\begin{{itemize}}
  \\item \\textbf{{What worked/What failed:}}
  \\item 
\\end{{itemize}}

\\noindent\\rule{{\\textwidth}}{{0.4pt}}

\\subsection{{🧠 Questions \\& Next Focus}}
\\textit{{What was difficult or needs further clarification? What is the goal for tomorrow's study session?}}

\\begin{{itemize}}
  \\item \\textbf{{Blockers/Doubts:}}
  \\item 
  \\item \\textbf{{Tomorrow's Goal:}}
  \\item 
\\end{{itemize}}
"""
    
    try:
        with open(log_filepath, 'w', encoding='utf-8') as f:
            f.write(template)
        print(f"Successfully created daily log template at:")
        print(f"  {rel_path}")
        print(f"\nHappy studying! Remember to run `python scripts/compile_notes.py` (or let the GitHub Action do it) when you're done.")
    except Exception as e:
        print(f"Error creating log file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    create_daily_log()
