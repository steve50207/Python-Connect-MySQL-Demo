# Python-Connect-MySQL-Demo

###### tags `SQL`

## 專案動機
- 近期正在進行軟體測試面試，有鑑於在前公司負責專案有使用到SQL進行資料庫驗證測試，因此開立此專案進行複習與練習，亦作為面試Demo使用。


## 專案目標
- 利用Python與MySQL資料庫建立連線，並建立公司資料庫(如下圖所示)，進行增加(CREATE)、更新(UPDATE)、查詢(READ)、刪除(DELETE)等操作，最後把Python與MySQL兩者執行結果進行比對，驗證Python執行結果正確性。
- ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/1.png)


## 專案工具
- 本項專案使用以下工具:
    - Python:
        -  透過Python搭配mysql-connector-python套件，
           可使用SQL語法對關聯式資料庫進行操作。
    - MySQL:
        -  RMDBS關聯式資料庫系統。
      
      
## 專案環境
- 本項網頁自動化測試專案在下列環境中執行:
    - Python: Python 3.11.0
    - Visaul Studio Code: 1.81.1
    - MySQL Workbench: 8.0.34
        - 以下為MySQL Workbench設定的資料庫連線參數:
            - host="localhost"
            - port="3306"
            - user="root"
            - password="zxc12345"
    - Python 3rd Party Packages: 
        - 可按照下列Python pip指令完成Packages安裝:
            - pip install mysql-connector-python 


## 專案文件架構
- create.py
    - 建立資料庫 demo
    - 在資料庫 demo內，建立以下表格:
        - employee: 員工資料
        - branch: 公司部門資料
        - client: 客戶資料
        - works_with: 員工負責客戶銷售資料
- update.py
    - 按照公司資料庫設定，依序在branch、employee、client、works_with表格插入對應資料
- read.py
    - 針對各項情境對公司資料庫進行讀取，主要練習以下項目:
        - SELECT: 查詢與搭配KEYWORD
            - SELECT * FROM TABLE
            - ORDER BY ASC(DESC): ASC遞增排序(預設),DESC遞減排序
            - LIMIT: 限制查詢資料筆數
            - SELECT Column FROM TABLE
            - DISTINCT: 限制查詢資料不重複
        - Aggregate function: 聚合函數
            - COUNT: 計數
            - AVG: 平均
            - SUM: 總和
            - MAX: 取最大值
            - MIN: 取最小值
        - wildcard: 萬用字元搭配LIKE
            - `%`: 代表多個字元
            - `_`: 代表一個字元
        - union: 聯集，合併不同表格屬性，合併屬性的資料型態需要保持一致
        - join: 合併查詢，用資料表之間欄位的關連性來結合多資料表之所需要的資訊
            - A JOIN B: 
                - 取兩者表格同時符合條件的部分(A ∩ B)
            - A LEFT JOIN B: 
                - A表格全部保留,B則是取表格符合條件的部分(A∪(A ∩ B))
            - A RIGHT JOIN B: 
                - B表格全部保留,A則是取表格符合條件的部分(B∪(B ∩ A))
        - subquery: 子查詢，在一個查詢語句中用另一個查詢語句,判斷時用()包起另一個查詢
            - SELECT * FROM TABLE WHERE COLUMN = 
              (SELECT * FROM TABLE WHERE = DATA): 單個判斷條件
            - SELECT * FROM TABLE WHERE COLUMN IN 
              (SELECT * FROM TABLE WHERE = DATA): 多個判斷條件
- delete.py
    - 刪除公司資料庫表格資料，觀察FOREIGN KEY ON DELETE設定的影響
    - ON DELETE: 當FORIGN KEY對應資料被刪除時，應該採取甚麼做法
        - ON DELETE SET NULL: 刪除後FOREIGN KEY屬性資料設定為NULL 
        - ON DELETE CASCADE: 刪除後FOREIGN KEY屬性對應整筆資料一併刪除


## 執行結果
- create.py
    - 建立database demo
        - Python: - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/2.png)
        - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/3.png)
    - 在database demo內建立以下table:
        - employee: 公司員工資料
            - emp_id: 
                - 屬性定義: 員工id號碼
                - 資料型態: INT
                - 鍵值設定: PRIMARY KEY
            - name: 
                - 屬性定義: 員工姓名
                - 資料型態: VARCHAR(20)
            - birth_date: 
                - 屬性定義: 出生年月日
                - 資料型態: VARCHAR(20)
            - sex:
                - 屬性定義: 性別
                - 資料型態: VARCHAR(1)
            - salary:
                - 屬性定義: 員工薪水
                - 資料型態: INT
            - branch_id: 
                - 屬性定義: 部門id號碼
                - 資料型態: INT
                - 鍵值設定: 
                    - FOREIGN KEY
                    - 關聯branch table PRIMARY KEY branch_id
                    - ON DELETE SET NULL
            - sup_id:
                - 屬性定義: 主管id號碼
                - 資料型態: INT
                - 鍵值設定: 
                    - FOREIGN KEY
                    - 關聯employee table PRIMARY KEY emp_id
                    - ON DELETE SET NULL
             - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/4.png)
             - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/5.png)
         - branch: 公司部門資料
            - branch_id:
                - 屬性定義: 部門id號碼
                - 資料型態: INT
                - 鍵值設定: PRIMARY KEY
            - branch_name:
                - 屬性定義: 部門名稱
                - 資料型態: VARCHAR(20)
            - manager_id:
                - 屬性定義: 部門主管id號碼
                - 資料型態: INT
                - 鍵值設定: 
                    - FOREIGN KEY
                    - 關聯employee table PRIMARY KEY emp_id
                    - ON DELETE SET NULL
             - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/6.png)
             - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/7.png)
         - client
            - client_id:
                - 屬性定義: 客戶id號碼
                - 資料型態: INT
                - 鍵值設定: PRIMARY KEY
            - client_name:
                - 屬性定義: 客戶名稱
                - 資料型態: VARCHAR(20)
            - phone:
                - 屬性定義: 客戶電話號碼
                - 資料型態: INT
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/8.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/9.png)
        - works_with
            - emp_id: 
                - 屬性定義: 員工id號碼
                - 資料型態: INT
                - 鍵值設定: 
                    - 同時為PRIMARY KEY與FOREIGN KEY
                    - 關聯employee table PRIMARY KEY emp_id
                    - ON DELETE CASCADE
            - client_id:
                - 屬性定義: 客戶id號碼
                - 資料型態: INT
                - 鍵值設定: 
                    - 同時為PRIMARY KEY與FOREIGN KEY
                    - 關聯client table PRIMARY KEY client_id
                    - ON DELETE CASCADE
            - total_sales:
                - 屬性定義: 銷售金額
                - 資料型態: INT
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/10.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/11.png)
- update.py
    - 按照公司資料庫設定，依序在branch、employee、client、works_with表格插入對應資料
        - employee表格資料: 
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/12.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/13.png)
        - branch表格資料: 
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/14.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/15.png)
        - client表格資料: 
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/16.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/17.png)
        - works_with表格資料: 
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/18.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/19.png)

- read.py
    - SELECT: 基本查詢與搭配KEYWORD
        - SELECT * FROM TABLE: 
            - 取得所有員工資料
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/20.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/21.png)
            - 取得所有客戶資料
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/22.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/23.png)
        - ORDER BY ASC(DESC): ASC遞增排序(預設),DESC遞減排序
            - 按薪水低到高取得員工資料
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/24.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/25.png)
        - LIMIT: 限制查詢資料筆數 
            - 取得薪水前3高的員工
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/26.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/27.png)
        - SELECT COLUMN FROM TABLE: 
            - 取得所有員工的名子 
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/28.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/29.png)
        - DISTINCT: 限制查詢資料不重複
            - 取得不重複的部門id
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/30.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/31.png)
    - Aggregate function: 聚合函數 
        - COUNT: 計數
            - 取得所有員工人數
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/32.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/33.png)
            - 取得有主管的員工人數
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/34.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/35.png)
            - 取得所有出生於 1970-01-01 之後的女性員工人數
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/36.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/37.png)
        - AVG: 平均
            - 取得所有員工的平均薪水
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/38.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/39.png)
        - SUM: 總和
            - 取得所有員工薪水的總和
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/40.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/41.png)
        - MAX: 取最大值
            - 取得薪水最高的員工
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/42.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/43.png)
        - MIN: 取最小值
            - 取得薪水最低的員工
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/44.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/45.png)
    - wildcard: 萬用字元搭配LIKE
        - `%`: 代表多個字元
            - 取得電話號碼尾數是335的客戶
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/46.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/47.png)
            - 取得電話號碼開頭是256的客戶
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/48.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/49.png)
            - 取得電話號碼中間是354的客戶
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/50.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/51.png)
            - 取得姓艾的客戶
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/52.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/53.png)
        - `_`: 代表一個字元
            - 取得生日在12月的員工
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/54.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/55.png)
            - 取得生日在9月的員工
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/56.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/57.png)
    - union: 聯集，合併不同表格屬性，合併屬性的資料型態需要保持一致
        - 員工名子 union 客戶名子
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/58.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/59.png)
        - 員工id union 客戶id
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/60.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/61.png)
        - 員工薪水 union 銷售金額
            - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/62.png)
            - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/63.png)
    - JOIN:
        - A JOIN B
            - 將employee表格與branch表格合併後,搜尋所有部門經理資訊
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/64.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/65.png)
            - 同上,但只顯示員工id,員工名稱,部門名稱
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/66.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/67.png)
        - A LEFT JOIN B
            - 同上,但是將JOIN改成LEFT JOIN
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/68.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/69.png)
        - A RIGHT JOIN B
            - 同上,但是將JOIN改成RIGHT JOIN
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/70.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/71.png)
    - subquery: 子查詢，在一個查詢語句中用另一個查詢語句,判斷時用()包起另一個查詢
        - 單個條件判斷
            - 找出研發部門的經理名稱 
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/72.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/73.png)
        - 多個條件判斷
            - 找出單一客戶銷售金額超過50000的員工名稱
                - Python: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/74.png)
                - MySQL: ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/75.png)

- delete.py
    - 刪除表格資料
        - 刪除公司資料庫表格資料，觀察FOREIGN KEY ON DELETE設定的影響
            - 刪除Employee小綠資料
                - ON DELETE SET NULL
                    - Python: 
                        - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/76.png)
                        - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/77.png)
                    - MySQL: 
                        - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/78.png)
                        - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/79.png)
                - ON DELETE CASCADE
                    - Python: 
                        - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/80.png)
                    - MySQL:
                        - ![image](https://github.com/steve50207/Python-Connect-MySQL-Demo/blob/main/png/81.png)


## 相關連結
- [【資料庫】SQL 初學者教學](https://www.youtube.com/watch?v=gvRXjsrpCHw&list=LL)
- [MySQL YT影片練習筆記](https://hackmd.io/@MJUsbP-5S_-z1aM5n6NvlQ/rJ98RF5in)
