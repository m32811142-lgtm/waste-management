import sys
import os

# تنظیم مسیر برای اینکه ماژول‌ها درست پیدا شوند
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from storage import load_bins
from analyzer import sort_by_fill, count_by_category
from priority import rank_bins
from report import generate_report, save_report_csv

def main():
    # مسیر فایل دیتا (از داخل پوشه src به پوشه data)
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "bins.csv")
    report_path = os.path.join(os.path.dirname(__file__), "..", "data", "report.csv")
    
    print("--- شروع پردازش داده‌ها ---")
    
    # خواندن داده‌ها
    bins, invalid = load_bins(data_path)
    
    print(f"✅ رکوردهای معتبر: {len(bins)}")
    print(f"❌ رکوردهای نامعتبر: {len(invalid)}")
    for rec, errs in invalid:
        print(f"   - {rec.get('bin_id', '?')}: {errs}")
    
    print("\n📊 دسته‌بندی مخازن:")
    for cat, count in count_by_category(bins).items():
        print(f"   {cat}: {count}")
    
    print("\n🏆 ۵ مخزن با بالاترین اولویت:")
    for b, score in rank_bins(bins)[:5]:
        print(f"   {b['bin_id']} - امتیاز: {score:.2f} - پرشدگی: {b['fill_level_percent']}%")
    
    # تولید گزارش
    report = generate_report(bins)
    save_report_csv(report, report_path)
    print(f"\n📄 گزارش کامل در مسیر data/report.csv ذخیره شد.")

if __name__ == "__main__":
    main()