# Post-generator using Gen-AI

This project is a LinkedIn Post Generator that leverages the power of LLaMA 3.1 through the Groq API, LangChain for orchestration, and a user-friendly Streamlit interface. It allows users to generate tailored, high-quality LinkedIn posts based on their role, tone, intent, and keywords.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)


---

## Features

- Uses the LLaMA 3.1 model via Groq API for fast and accurate post generation.
- Modular codebase using LangChain for prompt management and chaining.
- Streamlit-based frontend for ease of use and deployment.
- Few-shot prompting technique to enhance generation quality.
- Support for custom user input: role, tone, goal, and keywords.

---

## Tech Stack

- Python 3.12
- Streamlit
- LangChain
- Groq API (OpenAI-compatible)
- `dotenv` for managing environment variables
- JSON for input/output management

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- A valid Groq API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/project-genai-post-generator.git
cd project-genai-post-generator

python -m venv venv
venv\Scripts\activate  # For Windows
# or
source venv/bin/activate  # For macOS/Linux

pip install -r requirements.txt

### Running

streamlit run main.py

### Project Structure

project-genai-post-generator/
│
├── main.py                  # Streamlit frontend logic
├── llm_helper.py            # Manages LLM interactions
├── post_generator.py        # Constructs post text based on input
├── few_shot.py              # Few-shot examples for better generation
├── preprocess.py            # Preprocessing for raw data
│
├── requirements.txt         # Python dependencies
├── generated_image.png      # Optional output image
│
└── data/
    ├── .env                 # API keys and config
    ├── raw_posts.json       # Sample input data
    └── processed_posts.json # Generated posts
