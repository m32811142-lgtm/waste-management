def calculate_volume(bin_record):
    capacity = float(bin_record["capacity_liters"])
    fill = float(bin_record["fill_level_percent"])
    return capacity * fill / 100

def classify(fill_percent):
    fill = float(fill_percent)
    if fill < 50:
        return "عادی"
    elif fill < 80:
        return "نیازمند پایش"
    else:
        return "اولویت بالا"

def sort_by_fill(bins):
    return sorted(bins, key=lambda b: float(b["fill_level_percent"]), reverse=True)

def count_by_category(bins):
    result = {"عادی": 0, "نیازمند پایش": 0, "اولویت بالا": 0}
    for b in bins:
        result[classify(b["fill_level_percent"])] += 1
    return result