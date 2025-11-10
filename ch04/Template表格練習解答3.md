# Django Template 表格練習解答 (題目3)



## 題目3 解答：響應式成績統計表格

### views.py
```python
from django.shortcuts import render

def class_summary(request):
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
    
    return render(request, 'students/class_summary.html', {'class_summary': class_summary})
```

### templates/students/class_summary.html
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>班級成績統計</title>
    <style>
        * {
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Microsoft JhengHei', Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f1f3f4;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2.2em;
        }
        
        .summary-table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 14px;
            overflow-x: auto;
        }
        
        .summary-table th,
        .summary-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: center;
        }
        
        .summary-table th {
            background-color: #34495e;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
            z-index: 10;
        }
        
        .summary-table .class-header {
            background-color: #3498db;
            color: white;
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .summary-table .subject-header {
            background-color: #95a5a6;
            color: white;
            writing-mode: vertical-rl;
            text-orientation: mixed;
            padding: 8px 4px;
            min-width: 40px;
        }
        
        .summary-table .stat-cell {
            font-weight: bold;
        }
        
        .avg-cell { background-color: #e8f8f5; }
        .highest-cell { background-color: #d5f4e6; }
        .lowest-cell { background-color: #fadbd8; }
        
        .total-students {
            background-color: #f8f9fa;
            font-weight: bold;
        }
        
        /* 響應式設計 */
        .table-wrapper {
            overflow-x: auto;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        
        @media screen and (max-width: 768px) {
            body {
                padding: 10px;
            }
            
            .container {
                padding: 15px;
            }
            
            h1 {
                font-size: 1.8em;
            }
            
            .summary-table {
                font-size: 12px;
            }
            
            .summary-table th,
            .summary-table td {
                padding: 8px 4px;
            }
            
            .subject-header {
                writing-mode: horizontal-tb !important;
                text-orientation: mixed;
                padding: 4px !important;
                min-width: auto !important;
            }
        }
        
        @media screen and (max-width: 480px) {
            .summary-table {
                font-size: 10px;
            }
            
            .summary-table th,
            .summary-table td {
                padding: 6px 2px;
            }
            
            h1 {
                font-size: 1.5em;
            }
        }
        
        .legend {
            margin-top: 20px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
        }
        
        .legend h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        
        .legend-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 3px;
            border: 1px solid #ccc;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📈 班級成績統計報表</h1>
        
        {% if class_summary %}
            <div class="table-wrapper">
                <table class="summary-table">
                    <thead>
                        <tr>
                            <th rowspan="2">班級</th>
                            <th rowspan="2">總人數</th>
                            <th colspan="3">國文</th>
                            <th colspan="3">數學</th>
                            <th colspan="3">英文</th>
                        </tr>
                        <tr>
                            <th class="subject-header">平均</th>
                            <th class="subject-header">最高</th>
                            <th class="subject-header">最低</th>
                            <th class="subject-header">平均</th>
                            <th class="subject-header">最高</th>
                            <th class="subject-header">最低</th>
                            <th class="subject-header">平均</th>
                            <th class="subject-header">最高</th>
                            <th class="subject-header">最低</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for class_data in class_summary %}
                            <tr>
                                <td class="class-header">{{ class_data.class_name }}</td>
                                <td class="total-students">{{ class_data.total_students }}</td>
                                
                                <!-- 國文成績 -->
                                <td class="avg-cell stat-cell">{{ class_data.subjects.chinese.avg }}</td>
                                <td class="highest-cell stat-cell">{{ class_data.subjects.chinese.highest }}</td>
                                <td class="lowest-cell stat-cell">{{ class_data.subjects.chinese.lowest }}</td>
                                
                                <!-- 數學成績 -->
                                <td class="avg-cell stat-cell">{{ class_data.subjects.math.avg }}</td>
                                <td class="highest-cell stat-cell">{{ class_data.subjects.math.highest }}</td>
                                <td class="lowest-cell stat-cell">{{ class_data.subjects.math.lowest }}</td>
                                
                                <!-- 英文成績 -->
                                <td class="avg-cell stat-cell">{{ class_data.subjects.english.avg }}</td>
                                <td class="highest-cell stat-cell">{{ class_data.subjects.english.highest }}</td>
                                <td class="lowest-cell stat-cell">{{ class_data.subjects.english.lowest }}</td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            
            <!-- 圖例說明 -->
            <div class="legend">
                <h3>📋 統計說明</h3>
                <div class="legend-grid">
                    <div class="legend-item">
                        <div class="legend-color avg-cell"></div>
                        <span>平均分數</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color highest-cell"></div>
                        <span>最高分數</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color lowest-cell"></div>
                        <span>最低分數</span>
                    </div>
                </div>
                <p style="margin-top: 15px; color: #666; font-size: 0.9em;">
                    💡 提示：此表格支援響應式設計，可在各種裝置上正常顯示
                </p>
            </div>
            
        {% else %}
            <div style="text-align: center; padding: 40px; color: #666;">
                目前沒有班級統計資料
            </div>
        {% endif %}
    </div>
</body>
</html>
```

---

## 解答重點說明



### 題目3 重點
- 複雜表格結構 (`colspan`, `rowspan`)
- 響應式設計 (`@media` queries)
- 巢狀資料的處理
- 表格的語意化設計
- 可用性和美觀性的平衡

### 學習要點總結
1. **Django Template語法**：熟練使用循環、條件判斷
2. **HTML語意化**：正確使用表格相關標籤
3. **CSS設計**：響應式布局、條件格式、使用者體驗
4. **資料處理**：複雜資料結構的顯示和計算
5. **程式組織**：View和Template的職責分離