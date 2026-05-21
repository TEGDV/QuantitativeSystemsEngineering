#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Configuration
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(REPO_ROOT, "compiled_academic_notes.md")

# Folders to ignore during compilation
IGNORE_DIRS = {".git", ".github", "scripts", "node_modules", "venv", ".venv"}
IGNORE_FILES = {"README.md", "compiled_academic_notes.md"}

def clean_relative_path(path):
    return os.path.relpath(path, REPO_ROOT)

def get_markdown_files():
    """Traverses the repository and collects all markdown files under year directories, sorted logically."""
    md_files = []
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
            if file.endswith(".md") and file not in IGNORE_FILES:
                full_path = os.path.join(root, file)
                rel_path = clean_relative_path(full_path)
                md_files.append((rel_path, full_path))
    
    # Sort files logically:
    # 1. By year directory (e.g., year1, year_01, year2)
    # 2. By subdirectories (quarter_01, planning, notes)
    # 3. By filename (e.g., YYYY-MM-DD_log.md or alphabetical)
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

    md_files.sort(key=sorting_key)
    return md_files

def shift_headers(content, shift_amount):
    """Shifts all markdown headers in the content by the specified shift_amount."""
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        # Match standard ATX headers (e.g., # Header, ## Subheader)
        # We only match if it starts with # and has a space after the last #
        m = re.match(r'^(#+)(?:\s+(.*))?$', line)
        if m:
            header_symbols = m.group(1)
            header_text = m.group(2) or ""
            current_level = len(header_symbols)
            new_level = min(current_level + shift_amount, 6) # Max H6 in markdown
            new_lines.append(f"{'#' * new_level} {header_text}")
        else:
            new_lines.append(line)
    return '\n'.join(new_lines)

def count_words(text):
    """Rough estimation of word count."""
    return len(re.findall(r'\w+', text))

def compile_notes():
    md_files = get_markdown_files()
    if not md_files:
        print("No markdown files found to compile.")
        return
    
    print(f"Found {len(md_files)} markdown files. Compiling...")
    
    compiled_content = []
    
    # Write Master Header
    compiled_content.append("# Quantitative Systems Engineering: Compiled Notes & Logs")
    compiled_content.append(f"*Last compiled: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    compiled_content.append("")
    compiled_content.append("This file contains the unified learning notes, plans, and daily logs compiled from the repository. ")
    compiled_content.append("It is automatically updated on every push to the repository to keep the NotebookLM context synchronized.")
    compiled_content.append("")
    compiled_content.append("## 📁 Compiled Sources")
    
    for rel_path, _ in md_files:
        compiled_content.append(f"- [{rel_path}](https://github.com/TEGDV/QuantitativeSystemsEngineering/blob/main/{rel_path})")
    
    compiled_content.append("")
    compiled_content.append("---")
    compiled_content.append("")
    
    for rel_path, full_path in md_files:
        print(f"Processing: {rel_path}")
        
        # Read the file
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")
            continue
        
        # Determine the logical hierarchy depth of the file based on directory structure
        # e.g., year1/notes/systems/chapter1.md -> parts: ["year1", "notes", "systems", "chapter1.md"]
        # We will treat each level as an H2, H3, H4 context, and shift the file's internal headers accordingly.
        parts = rel_path.split(os.sep)
        
        # Remove extension from the file name
        file_display_name = os.path.splitext(parts[-1])[0].replace('_', ' ').title()
        
        # Construct the context breadcrumbs
        breadcrumbs = " › ".join([p.replace('_', ' ').title() for p in parts[:-1]])
        
        # Append Section Divider
        compiled_content.append(f"## 📄 Source: {breadcrumbs} › {file_display_name}")
        compiled_content.append(f"*Path: [{rel_path}](https://github.com/TEGDV/QuantitativeSystemsEngineering/blob/main/{rel_path})*")
        compiled_content.append("")
        
        # Shift headers in the file by 2 levels (since the source header is H2)
        # So H1 inside the file becomes H3, H2 becomes H4, etc.
        shifted_content = shift_headers(content, shift_amount=2)
        
        compiled_content.append(shifted_content)
        compiled_content.append("")
        compiled_content.append("---")
        compiled_content.append("")
    
    # Write to master file
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write("\n".join(compiled_content))
        
        total_words = count_words("\n".join(compiled_content))
        print(f"Successfully compiled {len(md_files)} files into {OUTPUT_FILE}.")
        print(f"Total Word Count: {total_words} words.")
    except Exception as e:
        print(f"Error writing to output file: {e}")

if __name__ == "__main__":
    compile_notes()
