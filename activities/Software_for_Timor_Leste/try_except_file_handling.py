import csv

# File handling: reading and writing text files
def read_write_text_file():
    try:
        # Writing to a text file
        with open("example.txt", "w") as file:
            file.write("Hello, world!\n")
            file.write("This is an example of writing to a text file.")

        # Reading from a text file
        with open("example.txt", "r") as file:
            content = file.read()
            print("Content of example.txt:")
            print(content)

    except IOError:
        print("An error occurred while reading/writing the file.")

    finally:
        print("File handling complete.")

# CSV file handling
def read_write_csv_file():
    try:
        # Writing to a CSV file
        with open("example.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "City"])
            writer.writerow(["John", "25", "New York"])
            writer.writerow(["Alice", "30", "London"])

        # Reading from a CSV file
        with open("example.csv", "r") as file:
            reader = csv.reader(file)
            print("Content of example.csv:")
            for row in reader:
                print(row)

    except IOError:
        print("An error occurred while reading/writing the CSV file.")

    finally:
        print("CSV file handling complete.")

# Exception handling: try, except, finally
def exception_handling():
    try:
        # Dividing by zero (will raise an exception)
        result = 10 / 0
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero!")

    finally:
        print("Exception handling complete.")

# Adding data from a list comprehension to a file
def list_comprehension_to_file():
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [x**2 for x in numbers]

    try:
        with open("squared_numbers.txt", "w") as file:
            for number in squared_numbers:
                file.write(str(number) + "\n")

        print("Squared numbers written to file.")

    except IOError:
        print("An error occurred while writing to the file.")

# Cool tricks with files
def file_tricks():
    # Counting the number of lines in a file
    with open("example.txt", "r") as file:
        line_count = sum(1 for line in file)
        print("Number of lines in example.txt:", line_count)

    # Reading a file in reverse order
    with open("example.txt", "r") as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())

# Main function
def main():
    read_write_text_file()
    print()

    read_write_csv_file()
    print()

    exception_handling()
    print()

    list_comprehension_to_file()
    print()

    file_tricks()

if __name__ == "__main__":
    main()