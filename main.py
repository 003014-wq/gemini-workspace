"""
主程式入口：讀取負載數據並印出分析報表
"""
import os
import json
from analyzer import LoadAnalyzer

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(base_dir, "config.json")
    data_file = os.path.join(base_dir, "data", "sample_load.csv")

    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)

    print(f"=== {config.get('system_name')} ===")
    
    analyzer = LoadAnalyzer(
        data_path=data_file,
        emission_factor=config.get("emission_factor_kg_per_kwh", 0.495)
    )

    summary = analyzer.generate_summary()
    print(f"分析資料筆數: {summary['record_count']}")
    print(f"平均負載: {summary['average_load_mw']} MW")
    print(f"尖峰負載: {summary['peak_load']['peak_load_mw']} MW (時間: {summary['peak_load']['peak_time']})")
    print(f"綠能發電總量估算: {summary['renewable_total_mw']} MW")

    threshold = config.get("alert_threshold_mw", 35000)
    if summary['peak_load']['peak_load_mw'] > threshold:
        print(f"[警告] 尖峰負載已超過警戒閾值 ({threshold} MW)！")

if __name__ == "__main__":
    main()
