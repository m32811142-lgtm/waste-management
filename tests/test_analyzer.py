import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from analyzer import calculate_volume, classify, sort_by_fill

def test_calculate_volume():
    b = {"capacity_liters": "660", "fill_level_percent": "50"}
    assert calculate_volume(b) == 330.0

def test_classify():
    assert classify("30") == "عادی"
    assert classify("60") == "نیازمند پایش"
    assert classify("90") == "اولویت بالا"

def test_sort_by_fill():
    bins = [
        {"bin_id": "A", "fill_level_percent": "30"},
        {"bin_id": "B", "fill_level_percent": "90"},
    ]
    sorted_bins = sort_by_fill(bins)
    assert sorted_bins[0]["bin_id"] == "B"