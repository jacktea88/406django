## 第三部分：複合表格應用

### 題目3：響應式成績統計表格

**任務：** 建立一個響應式的成績統計表格

**提供的資料結構：**
```python
# views.py
class_summary = [
    {
        'class_name': 'A班',
        'total_students': 25,
        'subjects': {
            'chinese': {'avg': 82.5, 'highest': 95, 'lowest': 65},
            'math': {'avg': 78.2, 'highest': 98, 'lowest': 45},
            'english': {'avg': 85.1, 'highest': 96, 'lowest': 72}
        }
    },
    {
        'class_name': 'B班', 
        'total_students': 23,
        'subjects': {
            'chinese': {'avg': 79.8, 'highest': 92, 'lowest': 58},
            'math': {'avg': 84.3, 'highest': 100, 'lowest': 62},
            'english': {'avg': 81.7, 'highest': 94, 'lowest': 69}
        }
    }
]
```

**要求：**
1. 建立巢狀表格結構
2. 使用colspan和rowspan合併儲存格
3. 實作響應式設計（手機版顯示調整）
4. 加入表格標題和說明
5. 使用Django template的巢狀迴圈

---