# Python Projects Repository

This repository contains a collection of advanced Python projects demonstrating modern software engineering practices, async programming, API design, and data processing techniques.

## Overview

Each project in this repository is designed to showcase best practices for building production-ready Python applications with proper architecture, testing, and documentation.

## Projects

### 1. [E-Commerce Catalog Service](./python-ecommerce)

A high-performance asynchronous e-commerce catalog microservice built with FastAPI.

**Key Features:**
- 🚀 Asynchronous request handling
- 📦 Efficient CSV-based product data loading
- 🔍 Product search and batch retrieval capabilities
- ⚡ Optimized data structures for quick lookups
- ✅ Comprehensive test suite

**Tech Stack:**
- FastAPI
- Python 3.8+
- Uvicorn ASGI server
- Pytest for testing

**Getting Started:**
```bash
cd python-ecommerce
pip install -r requirements.txt
PYTHONPATH=. pytest tests/
uvicorn async_service.main:app --reload --port 8001
```

For detailed documentation, see [python-ecommerce README](./python-ecommerce/README.md)

## Repository Structure

```
python-projects/
├── README.md                     # This file
├── python-ecommerce/             # E-Commerce Catalog Service
│   ├── README.md
│   ├── requirements.txt
│   └── async_service/
```

## General Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- git

### Quick Start for Any Project

1. Clone the repository:
```bash
git clone <repository-url>
cd python-projects
```

2. Navigate to the project directory:
```bash
cd <project-directory>
```

3. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

4. Install dependencies and run tests:
```bash
pip install -r requirements.txt
PYTHONPATH=. pytest tests/
```

5. Follow project-specific instructions in each project's README

## Git Workflow

Use the commands below for standard change review and commit flow:

```bash
git add .
git diff
git commit -m "<your message>"
git push origin HEAD
git status
```

> Replace `<your message>` with a short description of the changes.

## Contributing

When adding new projects to this repository:

1. Create a new project directory with descriptive name
2. Include a comprehensive README.md with:
   - Project overview
   - Setup instructions
   - Execution/deployment instructions
   - Test instructions
   - Key features and technology stack
3. Include a `requirements.txt` with all dependencies
4. Include unit tests in a `tests/` directory
5. Update this main README with project information

## Best Practices Demonstrated

- ✅ Async/await patterns in Python
- ✅ RESTful API design with FastAPI
- ✅ Data loading and processing
- ✅ Unit testing with pytest
- ✅ Virtual environment management
- ✅ Project documentation
- ✅ Git workflow

## License

[Add your license information here]

## Contact

[Add contact information here]
