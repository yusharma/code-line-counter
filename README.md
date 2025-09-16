# Code Line Counter

## 📌 Overview
Code Line Counter is a small utility that analyzes source code files and gives you statistics about:  
- **Blank lines**  
- **Comment lines**  
- **Code lines**  

It can work on a **single file** or scan through an **entire directory** of supported files.

### ✅ Current Features
- Supports **Python** and **Java** files.  
- Can analyze **one file** or **multiple files in a directory**.  
- Distinguishes between:
  - Blank lines  
  - Comment lines (only single-line comments supported for now)  
  - Code lines  
- Includes unit tests for:
  - Single Python/Java file  
  - Unsupported files (e.g., JavaScript)  
  - Multiple supported files in a directory  

---

## 🛠️ Adding Support for a New Language
To add another programming language:  
1. Create a **Line Classifier** inside the `classifiers/` directory.  
   - Example: `classifiers/python_line_classifier.py`  
   - This should define how to recognize comments, blank, and code lines.  
2. Create a **Language Analyzer** inside the `analyzers/` directory.  
   - Example: `analyzers/python_analyzer.py`  
   - This should register the line classifier and define supported file extensions.  

---

## 🚀 Example Usage
```python
from app import App

counter = App()
stats = counter.count_file_lines("test/sample_files/test_data2.py")

print(stats)
# Example output:
# {
#   "blank": 2,
#   "comments": 3,
#   "code": 10
# }
```

---

## 🧪 Running Unit Tests

Run app tests:
``` bash
python -m unittest test.test_app
```

---

## 📂 Project Structure
```
.
├── app.py                # Main entry point
├── analyzers/            # Language analyzers
├── classifiers/          # Line classifiers
├── factory/              # Factory methods
├── models/               # Data models
├── test/                 # Unit tests
│   ├── test_app.py
│   └── sample_files/
│       ├── test_data1.java
│       ├── test_data2.py
│       └── test_data1.js
```
