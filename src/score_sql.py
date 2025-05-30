def score_sql(code):
    score = 0
    if "SELECT *" in code.upper():
        score += 4
    if "DELETE" in code.upper() and "WHERE" not in code.upper():
        score += 5
    if "EXECUTE" in code.upper():
        score += 6
    if "?" in code or "%s" in code:
        score -= 2  # Parameterized = safer
    return max(score, 0)