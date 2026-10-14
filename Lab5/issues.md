# Issues found and fixed

Baseline: Pylint 5.65/10, Bandit 4 issues (2 High, 2 Low), Flake8 4 issues.
Final: Pylint 10.00/10, Bandit 0 issues, Flake8 0 issues.
Reports: `reports/*_before.txt` and `reports/*_after.txt` (the top-level `*_report.txt` files are the final ones).

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| `os.system` with string concatenation (B605) | Security (High) | 56 | `labPc` is concatenated into a shell command, so a crafted host name allows command injection | `subprocess.run(["ssh", "--", lab_pc, "lock-screen"], check=True)`: no shell, `--` stops option injection |
| Weak MD5 hash (B324) | Security (High) | 16 | MD5 is broken and flagged for security use | Switched to `hashlib.sha256` |
| Hardcoded password (B105) | Security (Low) | 11 | `PROCTOR_PASSWORD = "proctor-demo"` committed to source | Read from the `PROCTOR_PASSWORD` environment variable |
| `random` for selection (B311) | Security (Low) | 20 | Non-cryptographic PRNG flagged | Use `secrets.choice` |
| Mutable default argument (W0102) | Bug | 23 | `penalties={}` is shared across every call, so penalties leak between students and calls | Default to `None`, create a new dict inside the function |
| `range(len())` loop (C0200) | Style / quality | 25 | Index loop over `QUESTIONS` | `for i, question in enumerate(QUESTIONS)` |
| Unnecessary `elif` after `return` (R1705) | Quality | 37-42 | Redundant branching | Plain `if` / final `return` |
| camelCase names (C0103) | Style | 15, 19, 23, 35, 45, 54 | Functions and args not snake_case | Renamed (`hash_answer`, `pick_bonus_question`, `grade_student`, `student_name`, `get_grade`, `class_average`, `lock_screen`, `lab_pc`) |
| Missing docstrings (C0114/C0116) | Documentation | module + all functions | No docs | Added module and function docstrings |
| `main()` runs on import | Design | 73 | Importing the module runs the demo | Added `if __name__ == "__main__":` guard |
| E302 | Style (Flake8) | 54 | One blank line before `lockScreen` | Two blank lines |
| E225 | Style (Flake8) | 67 | `average=classAverage()` | Spaces around `=` |
| E261 | Style (Flake8) | 69 | Inline comment needs two spaces | Fixed spacing |
| E501 | Style (Flake8) | 70 | Line 93 chars > 79 | Wrapped the `print` call |

Bandit suppressions: `# nosec B404` on `import subprocess` and `# nosec B603 B607` on the `ssh` call. The argument list is fixed and passed without a shell, so the only remaining risk is the PATH lookup of `ssh`, which is acceptable for this helper.

Behaviour check: the demo prints exactly the same output as before (the bonus question is random).
