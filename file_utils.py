import csv

def load_csv(f_name):
    rows = []
    with open(f_name, newline='') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            rows.append(row)
        return rows
    return None

def write_csv(headers, rows, f_name):
    with open(f_name, "w+") as f:
        writer = csv.DictWriter(f, fieldnames=list(headers))
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
