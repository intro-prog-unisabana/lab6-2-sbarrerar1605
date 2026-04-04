def employee_print(employee_info):
    name = employee_info.get("Name", "N/A")
    salary = employee_info.get("Salary", "N/A")
    role = employee_info.get("Role", "N/A")

    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Role: {role}")

    remaining = employee_info.copy()
    remaining.pop("Name", None)
    remaining.pop("Salary", None)
    remaining.pop("Role", None)

    if remaining:
        for key, value in remaining.items():
            print(f"{key}: {value}")
    else:
        print("No other info!")