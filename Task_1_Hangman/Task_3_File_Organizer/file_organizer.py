# =====================================================
# PROJECT: Automated File Organizer
# INTERNSHIP: Datheon Python Programming Internship
# DEVELOPER: Auwal Mohammed Bello
# LANGUAGE: Python
# =====================================================

import os
import shutil
import tempfile


def get_category(extension):
    """Return a folder category based on file extension."""

    categories = {
        "Documents": [
            ".pdf", ".doc", ".docx", ".txt",
            ".xls", ".xlsx", ".ppt", ".pptx"
        ],
        "Images": [
            ".jpg", ".jpeg", ".png", ".gif",
            ".bmp", ".webp"
        ],
        "Videos": [
            ".mp4", ".avi", ".mov", ".mkv",
            ".wmv"
        ],
        "Archives": [
            ".zip", ".rar", ".7z", ".tar", ".gz"
        ],
        "Code": [
            ".py", ".js", ".html", ".css",
            ".java", ".cpp", ".php"
        ]
    }

    for category, extensions in categories.items():
        if extension in extensions:
            return category

    return "Others"


def organize_files(folder):
    """Organize files into category folders."""

    moved_count = 0
    error_count = 0

    print("\nStarting file organization...\n")

    # Scan the folder before moving files.
    with os.scandir(folder) as entries:
        files = [
            entry for entry in entries
            if entry.is_file()
        ]

    for entry in files:
        filename = entry.name
        extension = os.path.splitext(filename)[1].lower()
        category = get_category(extension)

        destination_folder = os.path.join(folder, category)

        try:
            os.makedirs(destination_folder, exist_ok=True)

            destination = os.path.join(
                destination_folder, filename
            )

            # Avoid overwriting a file with the same name.
            if os.path.exists(destination):
                name, ext = os.path.splitext(filename)
                number = 1

                while os.path.exists(destination):
                    new_name = f"{name}_{number}{ext}"
                    destination = os.path.join(
                        destination_folder, new_name
                    )
                    number += 1

            shutil.move(entry.path, destination)

            print(f"MOVED: {filename} -> {category}/")
            moved_count += 1

        except OSError as error:
            print(f"ERROR: Could not move {filename}: {error}")
            error_count += 1

    print("\n" + "=" * 40)
    print("       EXECUTION SUMMARY")
    print("=" * 40)
    print("Files moved successfully:", moved_count)
    print("Errors encountered:", error_count)


def main():
    print("=" * 40)
    print("      AUTOMATED FILE ORGANIZER")
    print("=" * 40)

    # Create a safe temporary workspace for demonstration.
    # This test does not organize files on your iPhone.
    folder = tempfile.mkdtemp(prefix="auwal_organizer_")

    sample_files = [
        "report.pdf",
        "photo.jpg",
        "video.mp4",
        "backup.zip",
        "script.py",
        "notes.txt",
        "unknown.xyz"
    ]

    # Create sample files for testing.
    for filename in sample_files:
        path = os.path.join(folder, filename)

        with open(path, "w", encoding="utf-8") as file:
            file.write("Sample file created for testing.\n")

    print("Demo workspace:", folder)

    organize_files(folder)

    print("\nFinal folder structure:")

    for category in sorted(os.listdir(folder)):
        category_path = os.path.join(folder, category)

        if os.path.isdir(category_path):
            print(f"\n{category}/")

            for filename in sorted(os.listdir(category_path)):
                print("  -", filename)

    print("\nFile organization demonstration completed!")


if __name__ == "__main__":
    main()
