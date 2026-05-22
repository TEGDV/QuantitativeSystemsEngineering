#!/usr/bin/env python3
import os
import re

def escape_latex(text):
    # Replace backslash first to avoid double escaping
    text = text.replace('\\', '\\textbackslash{}')
    for char in ['&', '%', '$', '#', '_', '{', '}']:
        text = text.replace(char, '\\' + char)
    text = text.replace('~', '\\textasciitilde{}')
    text = text.replace('^', '\\textasciicircum{}')
    text = text.replace('<', '\\textless{}')
    text = text.replace('>', '\\textgreater{}')
    return text

def format_markdown_text(text):
    # Split by backticks to extract inline code
    parts = text.split('`')
    new_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Inline code: escape LaTeX and wrap in \texttt
            new_parts.append(f"\\texttt{{{escape_latex(part)}}}")
        else:
            # Apply bold and italic formatting using regexes
            s = part
            s = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', s)
            s = re.sub(r'__(.*?)__', r'\\textbf{\1}', s)
            s = re.sub(r'\*(.*?)\*', r'\\textit{\1}', s)
            s = re.sub(r'_(.*?)_', r'\\textit{\1}', s)
            
            # Tokenize by LaTeX commands to escape the rest
            tokens = re.split(r'(\\[a-zA-Z]+\{|})', s)
            for j in range(len(tokens)):
                if j % 2 == 0:
                    tokens[j] = escape_latex(tokens[j])
            new_parts.append("".join(tokens))
            
    res = "".join(new_parts)
    # Unicode replacements
    res = res.replace('→', '$\\rightarrow$').replace('›', '$\\rangle$')
    return res

def convert_md_content_to_tex(content):
    lines = content.split('\n')
    output = []
    
    in_list = False
    list_type = None # 'itemize' or 'enumerate'
    in_code = False
    
    for line in lines:
        # Check for code blocks (indented or not)
        m_code = re.match(r'^\s*```(\w+)?', line)
        if m_code:
            if not in_code:
                in_code = True
                if in_list:
                    output.append(f"\\end{{{list_type}}}")
                    in_list = False
                    list_type = None
                
                lang = m_code.group(1) or ""
                lang_map = {
                    "rust": "Rust",
                    "c": "C",
                    "cpp": "C++",
                    "python": "Python",
                    "bash": "bash",
                    "sh": "bash",
                    "yaml": "XML",
                    "json": "XML"
                }
                tex_lang = lang_map.get(lang.lower(), "")
                if tex_lang:
                    output.append(f"\\begin{{lstlisting}}[language={tex_lang}]")
                else:
                    output.append("\\begin{lstlisting}")
            else:
                in_code = False
                output.append("\\end{lstlisting}")
            continue
            
        if in_code:
            # Write verbatim inside code block
            output.append(line)
            continue
            
        # Horizontal rules
        if line.strip() == "---":
            if in_list:
                output.append(f"\\end{{{list_type}}}")
                in_list = False
                list_type = None
            output.append("\\noindent\\rule{\\textwidth}{0.4pt}")
            continue
            
        # Headers
        m_h = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m_h:
            if in_list:
                output.append(f"\\end{{{list_type}}}")
                in_list = False
                list_type = None
            
            level = len(m_h.group(1))
            title = m_h.group(2).strip()
            
            # Format title (handling markdown bold/italics/inline code inside titles)
            formatted_title = format_markdown_text(title)
            
            if level == 1:
                output.append(f"\\section{{{formatted_title}}}")
            elif level == 2:
                output.append(f"\\subsection{{{formatted_title}}}")
            elif level == 3:
                output.append(f"\\subsubsection{{{formatted_title}}}")
            else:
                output.append(f"\\paragraph{{{formatted_title}}}")
            continue
            
        # Lists
        m_item = re.match(r'^(\s*)[-\*]\s+(.*)$', line)
        m_enum = re.match(r'^(\s*)\d+\.\s+(.*)$', line)
        
        if m_item:
            item_text = m_item.group(2).strip()
            
            # Handle checkboxes:
            is_checkbox = False
            is_checked = False
            if item_text.startswith('[ ]'):
                is_checkbox = True
                item_text = item_text[3:].strip()
            elif item_text.startswith('[x]'):
                is_checkbox = True
                is_checked = True
                item_text = item_text[3:].strip()
                
            formatted_item = format_markdown_text(item_text)
            if is_checkbox:
                prefix = '{[x]} ' if is_checked else '{[ ]} '
                formatted_item = prefix + formatted_item
            
            if not in_list or list_type != 'itemize':
                if in_list:
                    output.append(f"\\end{{{list_type}}}")
                in_list = True
                list_type = 'itemize'
                output.append("\\begin{itemize}")
            output.append(f"  \\item {formatted_item}")
            continue
        elif m_enum:
            enum_text = m_enum.group(2).strip()
            formatted_enum = format_markdown_text(enum_text)
            
            if not in_list or list_type != 'enumerate':
                if in_list:
                    output.append(f"\\end{{{list_type}}}")
                in_list = True
                list_type = 'enumerate'
                output.append("\\begin{enumerate}")
            output.append(f"  \\item {formatted_enum}")
            continue
            
        # Empty lines
        if line.strip() == "":
            output.append(line)
            continue
            
        # Regular text
        if in_list:
            output.append(f"\\end{{{list_type}}}")
            in_list = False
            list_type = None
            
        output.append(format_markdown_text(line))
        
    if in_list:
        output.append(f"\\end{{{list_type}}}")
        
    return "\n".join(output)

def migrate_files():
    targets = [
        "year_01/quarter_01/notes/2026-05-21_log.md",
        "year_01/quarter_01/notes/systems/chapter1_cssapp.md",
        "year_01/quarter_01/notes/systems/history_of_C_lang.md",
        "year_01/quarter_01/planning/week1.md",
        "year_01/quarter_01/planning/week2.md",
        "year_01/quarter_01/planning/week3.md"
    ]
    
    for md_path in targets:
        if not os.path.exists(md_path):
            print(f"File not found: {md_path}")
            continue
            
        tex_path = os.path.splitext(md_path)[0] + ".tex"
        print(f"Migrating {md_path} -> {tex_path}")
        
        with open(md_path, 'r', encoding='utf-8') as f:
            md_content = f.read()
            
        tex_content = convert_md_content_to_tex(md_content)
        
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(tex_content)
            
        # Delete original markdown file
        os.remove(md_path)
        print(f"Deleted original {md_path}")

if __name__ == "__main__":
    migrate_files()
