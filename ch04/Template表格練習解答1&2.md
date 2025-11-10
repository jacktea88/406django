# Django Template 表格練習解答 (題目1-2)

## 題目1 解答：基本學生資料表格

### urls.py
```python
from django.urls import path
from mysite.views import student_list

urlpatterns = [
    path('students/', student_list, name='student_list'), 
]

```
### views.py
```python
from django.shortcuts import render

def student_list(request):
    students = [
        {'id': 1, 'name': '張小明', 'age': 20, 'class': 'A班'},
        {'id': 2, 'name': '李小華', 'age': 19, 'class': 'B班'},
        {'id': 3, 'name': '王小美', 'age': 21, 'class': 'A班'},
        {'id': 4, 'name': '陳小強', 'age': 20, 'class': 'C班'},
    ]
    return render(request, 'student_list.html', {'students': students})
```

### templates/students/student_list.html
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>學生資料列表</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        
        .student-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        
        .student-table th,
        .student-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        
        .student-table th {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            text-align: center;
        }
        
        .student-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        
        .student-table tr:hover {
            background-color: #e8f5e8;
        }
        
        .student-table td {
            text-align: center;
        }
        
        .no-data {
            text-align: center;
            color: #666;
            font-style: italic;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>學生資料管理系統</h1>
        
        {% if students %}
            <table class="student-table">
                <thead>
                    <tr>
                        <th>學號</th>
                        <th>姓名</th>
                        <th>年齡</th>
                        <th>班級</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in students %}
                        <tr>
                            <td>{{ student.id }}</td>
                            <td>{{ student.name }}</td>
                            <td>{{ student.age }}</td>
                            <td>{{ student.class }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        {% else %}
            <div class="no-data">
                目前沒有學生資料
            </div>
        {% endif %}
    </div>
</body>
</html>
```

---

## 題目2 解答：成績表格with條件格式

### urls.py
```python
from django.urls import path
from mysite.views import student_grades

urlpatterns = [
    path('grades/', student_grades, name='student_grades'),
]

```
### views.py
```python
from django.shortcuts import render

def student_grades(request):
    student_grades = [
        {'id': 1, 'name': '張小明', 'chinese': 85, 'math': 92, 'english': 78},
        {'id': 2, 'name': '李小華', 'chinese': 90, 'math': 76, 'english': 88},
        {'id': 3, 'name': '王小美', 'chinese': 72, 'english': 85, 'math': 90},
        {'id': 4, 'name': '陳小強', 'chinese': 88, 'math': 95, 'english': 82},
    ]
    
    # 計算平均分數 (在template中也可以使用custom filter)
    for student in student_grades:
        total = student['chinese'] + student['math'] + student['english']
        student['average'] = round(total / 3, 1)
    
    return render(request, 'student_grades.html', {'student_grades': student_grades})
```

### templates/students/student_grades.html
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>學生成績管理</title>
    <style>
        body {
            font-family: 'Microsoft JhengHei', Arial, sans-serif;
            margin: 20px;
            background-color: #f8f9fa;
        }
        
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            max-width: 1000px;
            margin: 0 auto;
        }
        
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
            font-size: 2em;
        }
        
        .grades-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            font-size: 14px;
        }
        
        .grades-table th,
        .grades-table td {
            border: 1px solid #dee2e6;
            padding: 15px;
            text-align: center;
        }
        
        .grades-table th {
            background-color: #343a40;
            color: white;
            font-weight: bold;
            position: sticky;
            top: 0;
        }
        
        .grades-table tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        
        .grades-table tr:hover {
            background-color: #e9ecef;
            transform: translateY(-1px);
            transition: all 0.2s ease;
        }
        
        /* 條件格式樣式 */
        .grade-excellent {
            background-color: #d4edda !important;
            color: #155724;
            font-weight: bold;
        }
        
        .grade-good {
            background-color: #fff3cd !important;
            color: #856404;
        }
        
        .grade-poor {
            background-color: #f8d7da !important;
            color: #721c24;
        }
        
        .student-name {
            font-weight: bold;
            text-align: left;
        }
        
        .average-score {
            font-weight: bold;
            font-size: 1.1em;
        }
        
        .legend {
            display: flex;
            justify-content: center;
            margin-top: 20px;
            gap: 20px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 3px;
        }
        
        .stats {
            background-color: #e9ecef;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 學生成績管理系統</h1>
        
        {% if student_grades %}
            <div class="stats">
                <strong>班級總人數：{{ student_grades|length }} 人</strong>
            </div>
            
            <table class="grades-table">
                <thead>
                    <tr>
                        <th>學號</th>
                        <th>姓名</th>
                        <th>國文</th>
                        <th>數學</th>
                        <th>英文</th>
                        <th>平均分數</th>
                        <th>等級</th>
                    </tr>
                </thead>
                <tbody>
                    {% for student in student_grades %}
                        <tr>
                            <td>{{ student.id|stringformat:"03d" }}</td>
                            <td class="student-name">{{ student.name }}</td>
                            <td>{{ student.chinese }}</td>
                            <td>{{ student.math }}</td>
                            <td>{{ student.english }}</td>
                            
                            <!-- 平均分數with條件格式 -->
                            {% if student.average >= 85 %}
                                <td class="average-score grade-excellent">{{ student.average }}</td>
                                <td class="grade-excellent">優秀 🌟</td>
                            {% elif student.average >= 70 %}
                                <td class="average-score grade-good">{{ student.average }}</td>
                                <td class="grade-good">良好 👍</td>
                            {% else %}
                                <td class="average-score grade-poor">{{ student.average }}</td>
                                <td class="grade-poor">待加強 📚</td>
                            {% endif %}
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
            
            <!-- 圖例說明 -->
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color grade-excellent"></div>
                    <span>優秀 (≥85分)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color grade-good"></div>
                    <span>良好 (70-84分)</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color grade-poor"></div>
                    <span>待加強 (<70分)</span>
                </div>
            </div>
            
        {% else %}
            <div class="no-data">
                目前沒有成績資料
            </div>
        {% endif %}
    </div>
</body>
</html>
```

---
