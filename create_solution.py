import os
import argparse
import re

def create_solution_template(problem_name, difficulty, language="python"):
    # Clean problem name for folder creation
    clean_name = re.sub(r'[^\w\s-]', '', problem_name).strip().replace(' ', '_').lower()
    
    # Map difficulties to folders
    difficulty_map = {
        'e': 'Easy',
        'm': 'Medium',
        'h': 'Hard'
    }
    
    diff_folder = difficulty_map.get(difficulty.lower(), 'Uncategorized')
    
    # Create directory structure
    folder_path = os.path.join(diff_folder, clean_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # File extensions
    extensions = {
        'python': 'py',
        'java': 'java',
        'cpp': 'cpp',
        'js': 'js'
    }
    
    ext = extensions.get(language.lower(), 'txt')
    file_path = os.path.join(folder_path, f"solution.{ext}")
    
    # Boilerplate content
    content = ""
    if ext == 'py':
        content = f'"""\nProblem: {problem_name}\nDifficulty: {diff_folder}\n"""\n\nclass Solution:\n    def solve(self):\n        pass\n'
    elif ext == 'cpp':
        content = f'/*\nProblem: {problem_name}\nDifficulty: {diff_folder}\n*/\n\n#include <iostream>\n#include <vector>\nusing namespace std;\n\nclass Solution {{\npublic:\n    void solve() {{\n        \n    }}\n}};\n'
    elif ext == 'java':
        content = f'/*\nProblem: {problem_name}\nDifficulty: {diff_folder}\n*/\n\nclass Solution {{\n    public void solve() {{\n        \n    }}\n}}\n'
    elif ext == 'js':
        content = f'/**\n * Problem: {problem_name}\n * Difficulty: {diff_folder}\n */\n\nvar solve = function() {{\n    \n}};\n'
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"✅ Successfully created template at: {file_path}")
    else:
        print(f"⚠️ File already exists at: {file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a boilerplate folder and file for a LeetCode problem.")
    parser.add_argument("name", help="Name of the problem (e.g., 'Two Sum')")
    parser.add_argument("-d", "--difficulty", choices=['e', 'm', 'h'], required=True, help="Difficulty: e (Easy), m (Medium), h (Hard)")
    parser.add_argument("-l", "--language", default="python", choices=['python', 'java', 'cpp', 'js'], help="Programming language (default: python)")
    
    args = parser.parse_args()
    create_solution_template(args.name, args.difficulty, args.language)
