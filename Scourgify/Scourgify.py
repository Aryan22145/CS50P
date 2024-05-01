import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
else:
    try:
        newfile = []
        newfile2 = []
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file, fieldnames=["name", "house"])
            for row in reader:
                newfile.append({'name': row['name'], 'house': row['house']})
            for n in range(len(newfile)):
                x = newfile[n]['name']
                if ',' in x:
                    lastname, firstname = x.split(', ')
                else:
                    continue
                newfile2.append({'firstname': firstname, 'lastname': lastname, 'house': newfile[n]['house']})

        with open(sys.argv[2], 'w') as file2:
            fieldnames = ['first', 'last', 'house']
            writer = csv.DictWriter(file2, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(newfile2)):
                writer.writerow({
                    'first': newfile2[i]['firstname'],
                    'last': newfile2[i]['lastname'],
                    'house': newfile2[i]['house']
                })
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')
