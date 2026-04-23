# Django + Bootstrap + VS Code 開發環境

---

## 一、環境準備
### 1. 安裝 Python
```bash
python --version
```

### 2. 建立虛擬環境
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

macOS / Linux:
```bash
source venv/bin/activate
```

### 3. VS Code 套件安裝

安裝以下 Extensions：

Python
Django (Baptiste Darthenay)
Bootstrap IntelliSense
HTML CSS Support (ecmel)
IntelliSense for CSS class names in HTML (Zignd)

---

## 二、安裝 Django
```bash
pip install django
django-admin startproject mysite
cd mysite
python manage.py runserver
```

---

## 三、Bootstrap 設定（本地）
方法一（local）
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
```

方法二（CDN）
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
```

---

## 四、VS Code 設定（重點）
```json
{
    "bootstrapIntelliSense": {
        "enable": true,
        "bsVersion": "5.3",
        "showSuggestions": true,
        "autoComplete": true
    },
    "files.associations": {
        "*.html": "html",
        "*.djhtml": "html"
    },
    "css.enabledLanguages": ["html","django-html"],
    "html-css-support.enabledLanguages": ["html","django-html"],
    "html-css-support.styleSheets": [
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
    ],
    "editor.quickSuggestions": {
        "strings": true
    }
}
```

---

## 五、專案結構
```
mysite/
├── templates/
├── static/css/bootstrap.min.css
```

---

## 六、範例
```html
<h1 class="text-primary">Hello Django</h1>
<button class="btn btn-success">Click</button>
```

---

完成後即可使用 Django + Bootstrap + IntelliSense 開發。
