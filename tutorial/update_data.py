import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='zxc12345',
                                    database='sql_tutorial')

cursor = connection.cursor()

# 新增
# cursor.execute("INSERT INTO `branch` VALUES(5, 'qq', NULL)")


# 修改
# cursor.execute('UPDATE `branch` SET `manager_id` = 206 WHERE `branch_id` = 4;')


# 刪除
# cursor.execute("DELETE FROM `branch` WHERE `branch_id` = 5;")


cursor.close()
connection.commit() # 會更動資料內容需要輸入這個指令才會生效
connection.close()