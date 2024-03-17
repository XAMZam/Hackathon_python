def main():
    try:
        age = int(input("Enter your Age: "))

        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please input a valid age.")

if __name__ == "__main__":
    main()