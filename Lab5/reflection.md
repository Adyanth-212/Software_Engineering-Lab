# Reflection

(The handout PDF did not list the questions, so these are the standard Lab 5 reflection questions.)

**1. Which issues were the easiest to fix, and which were the hardest?**
Style issues (Flake8 spacing and line length) and renames were mechanical. The hardest were the security ones, because they need a design choice: replacing `os.system` meant moving to an argument list and deciding how to treat the remaining low-severity Bandit warnings, and the hardcoded password meant deciding where the secret should live (an environment variable).

**2. Did the tools report any false positives?**
Partly. B311 (`random`) is arguably a false positive for picking a quiz question, and B404/B603/B607 remain after the `subprocess` fix even though the call is safe (fixed argv, no shell). I used `secrets.choice` for the first and documented `# nosec` suppressions with a reason for the others rather than ignoring them silently.

**3. How would you integrate static analysis into your development workflow?**
Run Flake8, Pylint and Bandit locally via pre-commit hooks and again in CI on every pull request, failing the build on Bandit High/Medium findings and on a Pylint score below a threshold (for example 9.5).

**4. What tangible improvements did you see in code quality, security and readability?**
Pylint went from 5.65 to 10.00, Bandit from 2 High and 2 Low issues to none, and Flake8 to clean. Concretely: command injection and weak hashing removed, a shared mutable default that leaked state between calls fixed, consistent naming, documentation on every function, and the module can now be imported without side effects.
