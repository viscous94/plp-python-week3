# Conditions and Loops

## File Overview

* **`grade_reporter.py`**: Processes a list of test scores to assign letter grades, count passing and failing students, and compute the class average score rounded to one decimal place.
* **`bug_hunt.py`**: Demonstrates debugging techniques by identifying and resolving three distinct errors (a syntax error, a type error, and a logic error) in a `while` loop counter program.

## Reflections on Debugging

The hardest bug to find in `bug_hunt.py` was the logic error (`count < 5`), as it allowed the code to execute successfully without throwing a runtime error. Even though no red error message appeared, I knew something was wrong because the final printed sum was `10` instead of the expected target of `15`. To diagnose it, I traced the loop's execution manually and realized that the loop condition terminated before adding the final number, `5`, requiring the condition to be updated to `count <= 5`.