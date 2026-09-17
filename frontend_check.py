# frontend_check.py

import time

print("======================================")
print("       FRONTEND MODULE CHECK")
print("======================================")

print("Checking student examination input...")

time.sleep(3)

total_marks = 100
marks_obtained = 85

print(f"Total Marks    : {total_marks}")
print(f"Marks Entered  : {marks_obtained}")

if total_marks <= 0:
    print("[FAIL] Total marks must be greater than zero.")
    raise SystemExit(1)

if marks_obtained < 0 or marks_obtained > total_marks:
    print("[FAIL] Invalid marks entered.")
    raise SystemExit(1)

print("[PASS] Marks are within the valid range.")
print("[PASS] Student examination input validated.")

print("======================================")
print("Frontend checks passed.")
print("======================================")
