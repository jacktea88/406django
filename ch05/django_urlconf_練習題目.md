# Django URLconf 練習習題

## 練習主題：線上書店管理系統

### 情境說明
你正在開發一個線上書店管理系統，需要設計完整的URL結構來處理不同的功能頁面。這個練習可運用Django URLconf的各種用法。

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


## 第一部分：基礎URL配置

### 題目1：建立基本URL結構

**任務：** 為書店系統建立基本的URL配置

**需要實現的頁面：**
- 首頁：顯示書店介紹
- 書籍列表：顯示所有書籍
- 關於我們：公司介紹頁面
- 聯絡我們：聯絡資訊頁面

**要求：**
1. 建立主專案的 `urls.py` 
2. 建立 books app 的 `urls.py`
3. 使用 `include()` 函數組織URL
4. 設定適當的URL命名 (name參數)
5. 建立對應的view函數

**預期URL結構：**
```
/                    -> 首頁
/books/              -> 書籍列表
/about/              -> 關於我們  
/contact/            -> 聯絡我們
```

**完成標準：**
- [ ] URL路由正確配置
- [ ] 使用include()組織結構
- [ ] 每個URL都有適當的名稱
- [ ] View函數能正常回應

---

## 第二部分：帶參數的URL

### 題目2：動態URL參數處理

**任務：** 實現書籍詳細頁面和分類功能

**需要實現的功能：**
- 書籍詳細頁面：顯示單本書的詳細資訊
- 書籍分類頁面：依據分類顯示書籍
- 作者頁面：顯示特定作者的所有書籍
- 搜尋功能：根據關鍵字搜尋書籍

**要求：**
1. 使用路徑參數 (`<int:pk>`, `<str:slug>`)
2. 實現URL反向解析
3. 處理可選參數
4. 加入查詢字串參數處理
5. 設定URL參數驗證

**預期URL結構：**
```
/books/1/                    -> 書籍詳細頁面 (ID=1)
/books/category/fiction/     -> 小說分類頁面
/books/author/john-doe/      -> 作者頁面
/books/search/               -> 搜尋頁面

```

**完成標準：**
- [ ] 正確使用路徑參數
- [ ] URL反向解析功能
- [ ] 參數驗證和錯誤處理
- [ ] 查詢字串參數處理

---



## 參考資源

- [Django URL dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [URL namespaces](https://docs.djangoproject.com/en/stable/topics/http/urls/#url-namespaces)
- [URL reversing](https://docs.djangoproject.com/en/stable/topics/http/urls/#reverse-resolution-of-urls)
- [Path converters](https://docs.djangoproject.com/en/stable/topics/http/urls/#path-converters)

