
# File Sorting Utility

The **File Sorting Utility** is a simple Python script that helps you organize files in a directory by sorting them into subfolders based on their file extensions. It also removes any empty folders after the sorting process.

## Features

- Sorts files into subfolders based on their extensions.
- Removes empty folders created during sorting.
- User-friendly command-line interface.

## Prerequisites

- Python 3.x installed on your system.

## How to Use

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.

### Sorting Files

1. Navigate to the directory containing the downloaded script using the terminal.
2. Run the script by executing the following command:

   ```bash
   python file_sorting_utility.py
   ```

3. The script will prompt you to provide a file path to sort. Enter the path to the directory containing the files you want to sort.

4. The script will automatically create subfolders for each file extension and move the files accordingly.

5. Once the sorting is complete, the script will remove any empty folders.

### Note

- Make sure you provide a valid file path when prompted. The script will not proceed if the path is invalid.

## Example

Suppose you have a directory named `Documents` with various files such as `report.docx`, `notes.txt`, `image.jpg`, and `presentation.pptx`. After running the script, the `Documents` directory will contain subfolders like `docx`, `txt`, `jpg`, and `pptx`, each containing the corresponding files.

