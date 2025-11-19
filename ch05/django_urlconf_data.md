# Django URLconf 練習

## 練習主題：線上書店管理系統

### 情境說明
開發一個線上書店管理系統，需要設計完整的URL結構來處理不同的功能頁面。
這個練習可運用Django URLconf的各種用法。

#### ===== 模擬資料 =====
##### 習題一 模擬書籍資料
    books = [
        {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450},
        {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520},
        {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380},
    ]
    
    context = {
        'books': books,
        'page_title': '書籍列表'
    }

##### 習題二 模擬書籍資料
MOCK_BOOKS = [
    {
        'id': 1, 'title': 'Python程式設計', 'author': '王小明', 
        'author_slug': 'wang-xiaoming', 'category': 'programming', 
        'price': 450, 'isbn': '978-1-234-56789-0', 'year': 2023
    },
    {
        'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 
        'author_slug': 'li-xiaohua', 'category': 'web-development', 
        'price': 520, 'isbn': '978-1-234-56789-1', 'year': 2024
    },
    {
        'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 
        'author_slug': 'zhang-datong', 'category': 'computer-science', 
        'price': 380, 'isbn': '978-1-234-56789-2', 'year': 2023
    },
    {
        'id': 4, 'title': '機器學習實戰', 'author': '王小明', 
        'author_slug': 'wang-xiaoming', 'category': 'machine-learning', 
        'price': 600, 'isbn': '978-1-234-56789-3', 'year': 2024
    },
]

##### 習題三 模擬書籍資料
BOOKS_DATA = [
    {'id': 1, 'title': 'Python程式設計', 'author': '王小明', 'price': 450, 'category_id': 1},
    {'id': 2, 'title': 'Django網頁開發', 'author': '李小華', 'price': 520, 'category_id': 1},
    {'id': 3, 'title': '資料結構與演算法', 'author': '張大同', 'price': 380, 'category_id': 2},
    {'id': 4, 'title': '機器學習入門', 'author': '陳小美', 'price': 600, 'category_id': 3},
]

CATEGORIES_DATA = [
    {'id': 1, 'name': 'Programming', 'description': '程式設計相關書籍'},
    {'id': 2, 'name': 'Computer Science', 'description': '計算機科學相關書籍'},
    {'id': 3, 'name': 'Machine Learning', 'description': '機器學習相關書籍'},
]

REVIEWS_DATA = [
    {'id': 1, 'book_id': 1, 'rating': 5, 'comment': '很棒的書！', 'user': '讀者A'},
    {'id': 2, 'book_id': 1, 'rating': 4, 'comment': '內容豐富', 'user': '讀者B'},
    {'id': 3, 'book_id': 2, 'rating': 5, 'comment': 'Django入門首選', 'user': '讀者C'},
]

---


