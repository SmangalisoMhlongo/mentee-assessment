# Python TDD Assessment

Welcome to your Python Test-Driven Development (TDD) assessment!  
You’ve been learning Python for about 3 weeks, so this challenge is designed to help you prove what you’ve learned — and how you think.

## 🧭 Overview
You’ll complete small coding tasks across multiple files using **TDD** (Test-Driven Development).  
That means you’ll either:
1. **Write tests first**, then implement the code to make them pass, or
2. **Write code first**, then create the tests for it.

You’ll be using **unittest**, the standard Python testing framework.

---

## 🧩 Task 1: Math Utilities
**Files**:  
- `src/math_utils.py`  
- `tests/test_math_utils.py`

### What to do:
- Implement basic mathematical functions (addition, subtraction, multiplication, division).
- Follow the `# TODO:` notes in both files.
- Handle invalid input (e.g., division by zero).

**Goal:**  
All tests in `test_math_utils.py` should pass.

---

## 🧮 Task 2: Factorials
**Files**:  
- `src/factorial.py`  
- `tests/test_factorial.py`

### What to do:
- Implement `factorial(n)` recursively.
- Write tests that handle:
  - Normal inputs (e.g., 5 → 120)
  - Edge cases (0 → 1)
  - Invalid inputs (negative numbers → raise ValueError)

---

## 🧱 Task 3: Drawing Shapes
**Files**:  
- `src/shapes.py`  
- `tests/test_shapes.py`

### What to do:
- Implement simple ASCII shape drawing (square, triangle, rectangle).
- Each function should return a **string** (not print).
- Tests should check if shapes have the correct number of lines and characters.

---

## 🔤 Task 4: String Formatting
**Files**:  
- `src/string_utils.py`  
- `tests/test_string_utils.py`

### What to do:
- Implement `format_name(first, last)` → `"Last, First"`
- Implement `title_case(sentence)` → converts every word to title case.
- Tests should cover both normal and edge cases (empty strings, extra spaces).

---

## 🔢 Task 5: List Filtering
**Files**:  
- `src/list_utils.py`  
- `tests/test_list_utils.py`

### What to do:
- Implement `filter_even(numbers)` → returns list of even numbers.
- Implement `filter_positive(numbers)` → returns list of positive numbers.
- Tests should cover empty lists, mixed values, and all negative numbers.

---

## 🧠 How to Run Tests
In your terminal:

```bash
python -m unittest discover -s tests
```

You should see green ✅ when all tests pass.

Good luck and have fun building clean, test-driven Python code!
