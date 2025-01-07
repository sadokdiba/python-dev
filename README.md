# 100 Days of Code: Python Journey 🚀🐍

Welcome to my **100 Days of Code** challenge repository! 🎉 This is my commitment to coding daily for 100 days, primarily focusing on **Python** as a server-side language. Follow along as I document my growth, tackle new challenges, and refine my skills through consistent practice and learning.

---

## 📂 Project Structure

Each day's progress is stored in its respective folder inside the `projects` folder from the main directory (`day_XX_"project_description"`), where:
- **`day_XX/`** contains the code and notes for that day's projects and features.
- A **`"day"`** could span over several day depending on the difficulty as the idea is to code every single day.
- Updates to previous days' code are also committed as I iterate and improve on earlier solutions or add new features.
  
### Example:
```plaintext
projects/
├── day_01_treasure_island/
│   ├── main.py
│   └── README.md
├── day_02_hangman/
│   ├── script.py
│   ├── tests/
│   └── README.md
├── ...
└── README.md
```

### Commit Message Conventions

This repository follows the **Conventional Commits** specification to maintain a consistent commit history. Below are the prefixes used and their purposes:

### Standard Commit Prefixes

| **Prefix**   | **Description**                                                                                 | **Example**                                         |
|--------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------|
| `feat:`      | Adds a new feature or functionality.                                                            | `feat: add user login feature`                    |
| `fix:`       | Fixes a bug or issue in the code.                                                               | `fix: resolve null pointer exception`             |
| `docs:`      | Updates or adds documentation (e.g., README, code comments).                                    | `docs: update API usage examples in README`       |
| `style:`     | Changes that do not affect the code's functionality (e.g., formatting, whitespace).              | `style: reformat code according to style guide`   |
| `refactor:`  | Refactors code without changing functionality or fixing bugs.                                   | `refactor: optimize authentication logic`         |
| `test:`      | Adds or updates tests.                                                                          | `test: add unit tests for payment module`         |
| `chore:`     | Updates build tools, dependencies, or other non-functional tasks.                               | `chore: update Node.js to latest LTS version`     |
| `perf:`      | Improves performance (e.g., optimizing algorithms, reducing load times).                        | `perf: improve query performance for reports`     |
| `ci:`        | Updates CI/CD configuration files or scripts.                                                   | `ci: add GitHub Actions for automated testing`    |
| `build:`     | Changes build system or external dependencies.                                                  | `build: upgrade webpack to version 5`            |
| `revert:`    | Reverts a previous commit.                                                                      | `revert: undo feat: add user login feature`       |

---

### Additional or Custom Prefixes

| **Prefix**         | **Description**                                                                          | **Example**                                       |
|---------------------|------------------------------------------------------------------------------------------|-------------------------------------------------|
| `hotfix:`          | A critical fix that needs immediate deployment.                                         | `hotfix: resolve production crash in login`    |
| `deps:`            | Updates dependencies specifically (similar to `build`).                                 | `deps: update lodash to 4.17.21`               |
| `wip:`             | Work in progress (commits that are incomplete but pushed for collaboration).            | `wip: implement basic dashboard layout`        |
| `security:`        | Security fixes or updates.                                                              | `security: fix XSS vulnerability in comments`  |
| `localization:`    | Updates related to translations or internationalization.                                | `localization: update French translations`     |
| `design:`          | Updates or changes related to UI/UX design.                                             | `design: adjust spacing in navbar`             |

---

### Breaking Changes
If a commit introduces a **breaking change** (something that is not backward compatible), include a `!` after the prefix. Add details about the breaking change in the commit body.

Example:
```text
feat!: update authentication API to use OAuth 2.0
BREAKING CHANGE: The `login` API endpoint has been removed. Use the `oauth/token` endpoint instead.
```

### Branch Naming Conventions
- `feat/<feature-name>`: New features
- `fix/<bug-name>`: Bug fixes
- `chore/<task-name>`: Maintenance tasks
