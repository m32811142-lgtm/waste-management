import csv
from validator import validate_record

def load_bins(filepath):
    valid_bins = []
    invalid_records = []
    seen_ids = set()
    
    with open(filepath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            errors = validate_record(row, seen_ids)
            if errors:
                invalid_records.append((row, errors))
            else:
                valid_bins.append(row)
                seen_ids.add(row["bin_id"])
    
    return valid_bins, invalid_records

def save_bins(bins, filepath):
    if not bins:
        return
    fieldnames = list(bins[0].keys())
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(bins)