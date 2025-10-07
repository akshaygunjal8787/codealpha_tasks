import re

# Step 1: Input file name
input_file = "sample_text.txt"     # your input text file name
output_file = "extracted_emails.txt"  # output file name

try:
    # Step 2: Read content from file
    with open(input_file, "r") as file:
        text = file.read()

    # Step 3: Use regex to find all email addresses
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    # Step 4: Remove duplicates using set()
    unique_emails = sorted(set(emails))

    # Step 5: Save extracted emails to a new file
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    # Step 6: Display results
    print(" Email Extraction Complete!")
    print(f"Total {len(unique_emails)} unique emails found.")
    print(f"Saved to file: {output_file}")

except FileNotFoundError:
    print(" Input file not found. Please check the file name or path.")
except Exception as e:
    print("️ An error occurred:", e)
