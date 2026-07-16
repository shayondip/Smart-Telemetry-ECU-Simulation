# test_fault_report.py

from reports.fault_report import generate_fault_report


faults = generate_fault_report()


print("\n========== FAULT REPORT ==========\n")

for fault in faults:
    print(f"- {fault}")

print("\n==================================\n")