def validate_record(record, seen_ids):
    errors = []
    
    # بررسی فیلدهای خالی
    required = ["bin_id", "latitude", "longitude", 
                "capacity_liters", "fill_level_percent", "status"]
    for field in required:
        if field not in record or record[field] == "":
            errors.append(f"فیلد {field} خالی است")
    
    if errors:
        return errors
    
    # شناسه تکراری
    if record["bin_id"] in seen_ids:
        errors.append(f"شناسه تکراری: {record['bin_id']}")
    
    # مختصات
    try:
        lat = float(record["latitude"])
        lon = float(record["longitude"])
        if not (-90 <= lat <= 90):
            errors.append("عرض جغرافیایی نامعتبر")
        if not (-180 <= lon <= 180):
            errors.append("طول جغرافیایی نامعتبر")
    except ValueError:
        errors.append("مختصات عددی نیست")
    
    # ظرفیت
    try:
        cap = float(record["capacity_liters"])
        if cap <= 0:
            errors.append("ظرفیت باید مثبت باشد")
    except ValueError:
        errors.append("ظرفیت عددی نیست")
    
    # درصد پرشدگی
    try:
        fill = float(record["fill_level_percent"])
        if fill < 0 or fill > 100:
            errors.append("درصد پرشدگی باید بین ۰ و ۱۰۰ باشد")
    except ValueError:
        errors.append("درصد پرشدگی عددی نیست")
    
    return errors