"""
電力負載核心分析模組
負責計算日均負載、尖峰負載與碳排估算
"""
import csv
from typing import List, Dict, Any

class LoadAnalyzer:
    def __init__(self, data_path: str, emission_factor: float = 0.495):
        self.data_path = data_path
        self.emission_factor = emission_factor
        self.records: List[Dict[str, Any]] = []
        self._load_data()

    def _load_data(self):
        with open(self.data_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.records.append({
                    "timestamp": row["timestamp"],
                    "load_mw": float(row["load_mw"]),
                    "solar_mw": float(row["solar_mw"]),
                    "wind_mw": float(row["wind_mw"])
                })

    def get_peak_load(self) -> Dict[str, Any]:
        """找出最高尖峰負載時段與數值"""
        if not self.records:
            return {}
        peak = max(self.records, key=lambda x: x["load_mw"])
        return {
            "peak_time": peak["timestamp"],
            "peak_load_mw": peak["load_mw"]
        }

    def get_average_load(self) -> float:
        """計算平均負載 (MW)"""
        if not self.records:
            return 0.0
        total = sum(r["load_mw"] for r in self.records)
        return round(total / len(self.records), 2)

    def get_total_renewable_generation(self) -> float:
        """計算總綠能發電量估算 (MW)"""
        return sum(r["solar_mw"] + r["wind_mw"] for r in self.records)

    def generate_summary(self) -> Dict[str, Any]:
        """產出整合報告字典"""
        peak_info = self.get_peak_load()
        avg_load = self.get_average_load()
        renewable_total = self.get_total_renewable_generation()
        
        return {
            "record_count": len(self.records),
            "peak_load": peak_info,
            "average_load_mw": avg_load,
            "renewable_total_mw": renewable_total
        }
