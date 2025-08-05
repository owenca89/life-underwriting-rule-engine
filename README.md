# Life Underwriting Rule Engine

This Python-based simulator mimics simplified life insurance underwriting logic. It evaluates mock applicants using configurable rules stored in a JSON file and logs decisions to a CSV file.

## Features

- Interactive terminal input for age, BMI, smoking status, blood pressure, and medical history
- Business rules loaded dynamically from 'rules.json'
- Realistic underwriting conditions (e.g., decline under 18, refer for chronic illness)
- Decision results logged to 'results.csv'
- Error handling with optional logging to 'error_log.txt'

## Getting Started

1. Clone the repository:
   git clone https://github.com/owenca89/life-underwriting-rule-engine.git
   cd life-underwriting-rule-engine.git
2. Run the app:
   python underwriting_rules.py
3. Follow the terminal prompts: Age, Smoker (yes/no), BMI, Blood pressure, Medical history flags (chronic illness, heart disease, cancer)
4. Review output and see logged decisions in results.csv

