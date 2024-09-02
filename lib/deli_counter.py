def line(katz_deli):
    if not katz_deli:  # Check if the list is empty
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        line_status += " ".join([f"{i+1}. {name}" for i, name in enumerate(katz_deli)])
        print(line_status)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    if not katz_deli:  # Check if the list is empty
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli.pop(0)}.")

# Example usage
if __name__ == "__main__":
    katz_deli = []

    take_a_number(katz_deli, "Ada")
    take_a_number(katz_deli, "Grace")
    take_a_number(katz_deli, "Kent")

    line(katz_deli)  # => "The line is currently: 1. Ada 2. Grace 3. Kent"

    now_serving(katz_deli)  # => "Currently serving Ada."

    line(katz_deli)  # => "The line is currently: 1. Grace 2. Kent"

    take_a_number(katz_deli, "Matz")

    line(katz_deli)  # => "The line is currently: 1. Grace 2. Kent 3. Matz"

    now_serving(katz_deli)  # => "Currently serving Grace."

    line(katz_deli)  # => "The line is currently: 1. Kent 2. Matz"
