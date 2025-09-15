import re

CRS_PATTERN = re.compile(r"^C\.R\.S\. § \d{1,2}-\d{1,2}-\d{1,3}(\.\d+)*$")
RULE_PATTERN = re.compile(r"^Colo\. R\. Civ\. P\. \d+(\([a-z0-9]\))*$")

def validate_citation(text):
    if CRS_PATTERN.match(text):
        return {"valid": True, "message": f"Valid Colorado statute: {text}"}
    if RULE_PATTERN.match(text):
        return {"valid": True, "message": f"Valid Colorado rule: {text}"}
    return {"valid": False, "message": f"Invalid or unrecognized citation: {text}"}

