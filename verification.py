
import csv_writer_utils
import formatting_utils

def getSampleContent(fileName):
    all_of_it = ""
    try:
        with open(fileName, mode='r') as file:
            all_of_it = file.read()
    finally:
        file.close()
        return all_of_it


if __name__ == "__main__":
    content = getSampleContent("test.txt")
    formatted_data = formatting_utils.getFormattedData(content)
    csv_writer_utils.write_csv(formatted_data, "validation")
    