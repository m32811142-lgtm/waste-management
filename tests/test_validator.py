import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from validator import validate_record

def test_duplicate_id():
    seen = {"B001"}
    rec = {"bin_id": "B001", "latitude": "38", "longitude": "46",
           "capacity_liters": "660", "fill_level_percent": "50", "status": "active"}
    assert any("تکراری" in e for e in validate_record(rec, seen))

def test_invalid_fill():
    rec = {"bin_id": "B002", "latitude": "38", "longitude": "46",
           "capacity_liters": "660", "fill_level_percent": "120", "status": "active"}
    assert any("پرشدگی" in e for e in validate_record(rec, set()))
    
def test_negative_capacity():
    rec = {"bin_id": "B003", "latitude": "38", "longitude": "46",
           "capacity_liters": "-50", "fill_level_percent": "50", "status": "active"}
    assert any("ظرفیت" in e for e in validate_record(rec, set()))