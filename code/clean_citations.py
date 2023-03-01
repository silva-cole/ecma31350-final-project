import csv
import glob


csv_files = ['extracted.csv', 'extracted2.csv', 'extracted3.csv', 'extracted4.csv', 'extracted5.csv']

numbers = ['0','1','2','3','4','5','6','7','8','9']

# Loop through each CSV file
for file in csv_files:
    # Open the CSV file
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Loop through each row in the file
        for row in reader:
            # Get the current value of the "time" field
            citation = row['time']
            
            str = ''
            i = 0
            while i < len(citation):
                if citation[i].isdigit():
                    str += citation[i]
                i += 1

            # Convert the "time" field to an integer
            new_citation = int(str)
            # Update the value of the "time" field in the row
            row['time'] = new_citation
