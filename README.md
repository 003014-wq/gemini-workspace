# 電力負載分析與報表系統 (Power Load Analyzer)

這是一個專門設計用來測試 Gemini 程式碼分析、結構解讀與架構重構的示範專案。

## 專案功能
- 讀取每小時電力負載與綠能發電數據（太陽能、風力）。
- 計算尖峰負載（Peak Load）與日平均負載。
- 評估碳排強度（以每度電排放係數計算）。
- 產出文字版與 JSON 結構之分析摘要報表。

## 檔案結構
```text
.
├── README.md               # 專案說明文件
├── config.json             # 系統設定參數（閾值、碳排係數）
├── main.py                 # 主執行程式入口
├── analyzer.py             # 核心分析邏輯與計算模組
└── data/
    └── sample_load.csv     # 示範負載數據集
```

## 快速開始
```bash
python main.py
```
