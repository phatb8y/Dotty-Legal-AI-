def generate_disclaimer(jurisdiction="CO"):
    if jurisdiction.upper() == "CO":
        return "This document complies with ADA and Colorado court accessibility guidelines."
    return "This document complies with ADA accessibility guidelines."
