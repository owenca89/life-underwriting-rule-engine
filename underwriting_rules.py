import json
import csv
import os
import logging

logging.basicConfig(
    filename='error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Applicant:
    def __init__(self, age, smoker, bmi, bp, medical_flags=None):
        self.age = age
        self.smoker = smoker
        self.bmi = bmi
        self.bp = bp  # 'Normal' or 'High'
        self.medical_flags = medical_flags if medical_flags else []

class RuleEngine:
    def __init__(self):
        self.rules = []

    def load_rules(self, file_path="rules.json"):
        with open(file_path, "r") as f:
            raw_rules = json.load(f)
        self.rules = []
        for rule in raw_rules:
            self.rules.append({
                "id": rule["id"],
                "description": rule["description"],
                "decision": rule["decision"],
                "condition": eval(f"lambda app: {rule['condition']}")
            })

    def evaluate(self, applicant):
        for rule in self.rules:
            if rule["condition"](applicant):
                return {
                    "decision": rule["decision"],
                    "triggered_rule": rule["id"],
                    "description": rule["description"]
                }

def log_result(applicant, result, log_file="results.csv"):
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Age", "Smoker", "BMI", "Blood Pressure",
                "Medical Flags", "Decision", "Triggered Rule", "Rule Description"
            ])

        writer.writerow([
            applicant.age,
            applicant.smoker,
            applicant.bmi,
            applicant.bp,
            ", ".join(applicant.medical_flags),
            result["decision"],
            result["triggered_rule"],
            result["description"]
        ])


def main():
    print("=== Life Insurance Rule Engine ===")

    try:
        age = int(input("Enter age: "))
        smoker_input = input("Smoker? (yes/no): ").strip().lower()
        smoker = smoker_input == 'yes'
        bmi = float(input("Enter BMI: "))
        bp = input("Enter blood pressure (Normal/High): ").strip().capitalize()
        flags = []

        chronic = input("Do you have a chronic illness? (yes/no): ").strip().lower()
        if chronic == 'yes':
            flags.append("chronic_illness")
        heart = input("History of heart disease? (yes/no): ").strip().lower()
        if heart == 'yes':
            flags.append("heart_disease")
        cancer = input("Have you had cancer? (yes/no): ").strip().lower()
        if cancer == 'yes':
            flags.append("cancer")

        applicant = Applicant(age=age, smoker=smoker, bmi=bmi, bp=bp, medical_flags=flags)

        engine = RuleEngine()
        engine.load_rules("rules.json")

        result = engine.evaluate(applicant)

        print("\n--- Evaluation Result ---")
        print("Decision:", result["decision"])
        print("Triggered Rule:", result["triggered_rule"])
        print("Rule Description:", result["description"])

        log_result(applicant, result)

    except Exception as e:
        logging.error("Unexpected error occurred", exc_info=True)
        print("An unexpected error occurred. Please check error_log.txt.")


if __name__ == "__main__":
    main()
