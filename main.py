"""Course Schedule System - menu-driven driver program."""

from schedule import Schedule

CSV_FILE = "STEM - Summer 2022 Schedule of Classes as of 05-02-22.csv"


def show_menu() -> None:
    print("\n=== Course Schedule System ===")
    print("1. Display all courses")
    print("2. Search by subject")
    print("3. Search by subject and catalog number")
    print("4. Search by instructor last name")
    print("5. Quit")


def main() -> None:
    schedule = Schedule()
    try:
        schedule.load_from_csv(CSV_FILE)
    except FileNotFoundError:
        print(f"Error: could not find data file '{CSV_FILE}'.")
        return

    print(f"Loaded schedule from '{CSV_FILE}'.")

    while True:
        show_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            schedule.print()
        elif choice == "2":
            subject = input("Enter subject (e.g. BIO): ")
            schedule.print_results(schedule.find_by_subject(subject))
        elif choice == "3":
            subject = input("Enter subject (e.g. BIO): ")
            catalog = input("Enter catalog number (e.g. 141): ")
            schedule.print_results(schedule.find_by_subject_catalog(subject, catalog))
        elif choice == "4":
            last_name = input("Enter instructor last name: ")
            schedule.print_results(schedule.find_by_instructor_last_name(last_name))
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number 1-5.")


if __name__ == "__main__":
    main()
