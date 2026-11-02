import csv
from analyzer import calculate_volume, classify

def generate_report(bins):
    total = len(bins)
    active = sum(1 for b in bins if b["status"] == "active")
    inactive = total - active
    avg_fill = sum(float(b["fill_level_percent"]) for b in bins) / total if total else 0
    total_capacity = sum(float(b["capacity_liters"]) for b in bins)
    total_volume = sum(calculate_volume(b) for b in bins)
    high_priority = [b for b in bins if classify(b["fill_level_percent"]) == "اولویت بالا"]
    
    return {
        "تعداد کل": total,
        "فعال": active,
        "غیرفعال": inactive,
        "میانگین پرشدگی": round(avg_fill, 2),
        "مجموع ظرفیت": total_capacity,
        "مجموع حجم پسماند": round(total_volume, 2),
        "مخازن اولویت بالا": high_priority,
    }

def save_report_csv(report, filepath):
    with open(filepath, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for key, value in report.items():
            if isinstance(value, list):
                writer.writerow([key, ", ".join(b["bin_id"] for b in value)])
            else:
                writer.writerow([key, value])