# Preparing input

input_file = open("input.txt")

reports = []

for line in input_file.readlines():
    report = list(map (int, line.split(" ")))
    reports.append(report)

# Part 1

def is_safe(report):
    increasing_order = report[0] < report[1]
    safe = True
    if not (sorted(report) == report or sorted(report, reverse=True) == report):
        safe = False
    for i in range(len(report) - 1):
        if abs(report[i] - report[i+1]) not in {1, 2, 3}:
            safe = False
    return safe

safe_reports = 0

for report in reports:
    if is_safe(report):
        safe_reports += 1

print(safe_reports)

# Part 2

def is_safe_with_problem_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        m_report = report.copy()
        del m_report[i]
        if is_safe(m_report):
            return True
    return False

safe_reports_with_problem_dampener = 0

for report in reports:
    if is_safe_with_problem_dampener(report):
        safe_reports_with_problem_dampener += 1

print(safe_reports_with_problem_dampener)
