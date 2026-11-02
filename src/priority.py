def compute_priority(bin_record, w1=0.7, w2=0.3):
    fill = float(bin_record["fill_level_percent"]) / 100
    # امتیاز اضافی: مخزن غیرفعال امتیاز کمتر
    extra = 1.0 if bin_record["status"] == "active" else 0.0
    return w1 * fill + w2 * extra

def rank_bins(bins):
    scored = [(b, compute_priority(b)) for b in bins]
    return sorted(scored, key=lambda x: x[1], reverse=True)