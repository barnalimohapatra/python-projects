# Python E-Commerce Projects

This repository contains advanced Python projects, currently featuring a high-performance asynchronous e-commerce catalog service built with FastAPI.

## Project Overview: E-Commerce Catalog Service

The **python-ecommerce** project is a FastAPI-based microservice that provides efficient product catalog management and retrieval capabilities. It features:

- 🚀 Asynchronous request handling with FastAPI
- 📦 CSV-based product data loading
- 🔍 Product search and batch retrieval
- ⚡ Optimized data structures for quick lookups
- 🔧 Utility decorators and generators for data processing

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Navigate to the project directory:
```bash
cd python-ecommerce
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

The main dependencies include:
- **FastAPI** - Modern web framework for building APIs
- **Uvicorn** - ASGI web server for running FastAPI applications
- **Pydantic** - Data validation and settings management
- **Python-dotenv** - Environment variable management

## Project Structure

```
python-ecommerce/
├── requirements.txt              # Project dependencies
├── async_service/
│   ├── main.py                  # FastAPI application and main endpoints
│   ├── data/
│   │   └── products.csv         # Product catalog data
│   ├── loaders/
│   │   └── product_loader.py    # CSV data loading functions
│   └── utils/
│       ├── decorators.py        # Custom decorators for functions
│       └── generators.py        # Generator utilities for data processing
```

### File Descriptions

- **main.py** - Contains the FastAPI application setup and all API route handlers
- **product_loader.py** - Handles loading product data from CSV files into memory
- **decorators.py** - Custom decorators for enhanced function behavior
- **generators.py** - Utility generators (e.g., batch_generator for chunking data)
- **products.csv** - Contains the product catalog with product IDs and attributes

## Execution Instructions

### Running the Application

Start the development server with auto-reload enabled:

```bash
uvicorn async_service.main:app --reload --port 8001
```

**Parameters:**
- `async_service.main:app` - Location of the FastAPI application instance
- `--reload` - Automatically restart server on code changes (development mode)
- `--port 8001` - Server runs on `http://localhost:8001`

### Production Deployment

For production, run without the reload flag:

```bash
uvicorn async_service.main:app --port 8001
```

## Git Repository

To clone this repository:

```bash
git clone <repository-url>
cd python-projects
cd python-ecommerce
```

To pull latest changes:

```bash
git pull origin main
```
