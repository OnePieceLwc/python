import pyodbc

# 连接SQL Server数据库
server = '127.0.0.1,1433'
database = 'Stu_Course'
username = 'sa'
password = '123456'
db = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password,timeout=3)

print("连接SQL Server数据库")
# 创建学生表
cursor = db.cursor()
# cursor.execute("CREATE TABLE students (id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255), password VARCHAR(255), resume TEXT)")

# 创建企业表
# cursor.execute("CREATE TABLE companies (id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255), contact_person VARCHAR(255), email VARCHAR(255), job_requirements TEXT)")

# 学生注册
def student_register(name, password):
    sql = "INSERT INTO students (name, password) VALUES (%s, %s)"
    values = (name, password)
    cursor.execute(sql, values)
    db.commit()
    print("学生注册成功")

# 学生登录
def student_login(name, password):
    sql = "SELECT * FROM students WHERE name = %s AND password = %s"
    values = (name, password)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("学生登录成功")
    else:
        print("学生登录失败")

# 学生填写个人信息和制作简历
def fill_personal_info(student_id, resume):
    sql = "UPDATE students SET resume = %s WHERE id = %s"
    values = (resume, student_id)
    cursor.execute(sql, values)
    db.commit()
    print("个人信息和简历填写成功")

# 学生浏览企业信息并发送简历
def send_resume(student_id, company_id):
    # 检查学生和公司是否存在
    student_sql = "SELECT * FROM students WHERE id = %s"
    student_values = (student_id,)
    cursor.execute(student_sql, student_values)
    student_result = cursor.fetchone()

    company_sql = "SELECT * FROM companies WHERE id = %s"
    company_values = (company_id,)
    cursor.execute(company_sql, company_values)
    company_result = cursor.fetchone()

    if student_result and company_result:
        # 发送简历的逻辑
        # 先检查是否已经发送过简历
        resume_sql = "SELECT * FROM resumes WHERE student_id = %s AND company_id = %s"
        resume_values = (student_id, company_id)
        cursor.execute(resume_sql, resume_values)
        resume_result = cursor.fetchone()

        if resume_result:
            print("已经发送过简历")
        else:
            # 发送简历
            insert_resume_sql = "INSERT INTO resumes (student_id, company_id, status) VALUES (%s, %s, %s)"
            insert_resume_values = (student_id, company_id, "待审核")
            cursor.execute(insert_resume_sql, insert_resume_values)
            db.commit()
            print("简历发送成功")
    else:
        print("学生或公司不存在")

# 企业注册
def company_register(name, contact_person, email):
    sql = "INSERT INTO companies (name, contact_person, email) VALUES (%s, %s, %s)"
    values = (name, contact_person, email)
    cursor.execute(sql, values)
    db.commit()
    print("企业注册成功")

# 企业登录
def company_login(name, email):
    sql = "SELECT * FROM companies WHERE name = %s AND email = %s"
    values = (name, email)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("企业登录成功")
    else:
        print("企业登录失败")

# 发布招聘信息
def publish_job(company_id, job_requirements):
    sql = "UPDATE companies SET job_requirements = %s WHERE id = %s"
    values = (job_requirements, company_id)
    cursor.execute(sql, values)
    db.commit()
    print("招聘信息发布成功")

# 关闭数据库连接
db.close


# 前台操作模块
# 学生信息填写
def fill_personal_info(student_id, resume):
    sql = "UPDATE students SET resume = ? WHERE id = ?"
    values = (resume, student_id)
    cursor.execute(sql, values)
    db.commit()
    print("个人信息和简历填写成功")

# 公司信息填写更新
def update_company_info(company_id, company_info):
    sql = "UPDATE companies SET company_info = ? WHERE id = ?"
    values = (company_info, company_id)
    cursor.execute(sql, values)
    db.commit()
    print("公司信息更新成功")

# 用户登录
def user_login(username, password, user_type):
    if user_type == "student":
        sql = "SELECT * FROM students WHERE name = ? AND password = ?"
    elif user_type == "company":
        sql = "SELECT * FROM companies WHERE name = ? AND password = ?"
    values = (username, password)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("用户登录成功")
    else:
        print("用户登录失败")

# 用户注册
def user_register(username, password, user_type):
    if user_type == "student":
        sql = "INSERT INTO students (name, [password]) VALUES (?, ?)"
    elif user_type == "company":
        sql = "INSERT INTO companies (name, [password]) VALUES (?, ?)"
    values = (username, password)
    cursor.execute(sql, values)
    db.commit()
    print("用户注册成功")

# 学生对公司的查询
def search_company(company_id):
    sql = "SELECT * FROM companies WHERE id = ?"
    values = (company_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("查询到公司信息：", result)
    else:
        print("未找到公司信息")

# 公司对学生的查询
def search_student(student_id):
    sql = "SELECT * FROM students WHERE id = ?"
    values = (student_id,)
    cursor.execute(sql, values)
    result = cursor.fetchone()
    if result:
        print("查询到学生信息：", result)
    else:
        print("未找到学生信息")

# 本次招聘信息查看
def view_job_postings():
    sql = "SELECT * FROM companies WHERE job_requirements IS NOT NULL"
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        print("本次招聘信息：")
        for row in result:
            print("公司ID:", row[0])
            print("公司名称:", row[1])
            print("招聘要求:", row[4])
            print("------------------------------")
    else:
        print("暂无招聘信息")

# 调用
student_id = 1
resume = "个人简历内容..."
fill_personal_info(student_id, resume)

company_id = 1
company_info = "公司信息更新..."
update_company_info(company_id, company_info)

username = "student1"
password = "password123"
user_type = "student"
user_login(username, password, user_type)

username = "student1"
password = "password123"
user_type = "student"
user_register(username, password, user_type)

company_id = 1
search_company(company_id)

student_id = 1
search_student(student_id)

view_job_postings()

# 管理员模块
# 数据维护
def data_maintenance():
    try:
        # 检查数据完整性
        # check_data_integrity()

        # 检查数据一致性
        # check_data_consistency()

        print("数据维护完成")

    except mysql.connector.Error as err:
        print(f"数据库错误: {err}")

# 数据备份
def data_backup():
    try:
        # 查询学生表的所有数据
        query = "SELECT * FROM students"
        cursor.execute(query)
        rows = cursor.fetchall()

        # 将数据导出到CSV文件
        with open('backup.csv', 'w') as file:
            for row in rows:
                file.write(','.join([str(value) for value in row]) + '\n')

        print("数据备份完成")

    except mysql.connector.Error as err:
        print(f"数据库错误: {err}")

# 检查数据完整性
def check_data_integrity():
    # 检查学生表中是否存在重复的学生记录
    cursor.execute("SELECT name, COUNT(*) FROM students GROUP BY name HAVING COUNT(*) > 1")
    duplicate_students = cursor.fetchall()
    if duplicate_students:
        print("存在重复的学生记录：")
        for student in duplicate_students:
            print("学生姓名:", student[0], "重复次数:", student[1])

    # 检查学生表中是否存在未填写个人信息的记录
    cursor.execute("SELECT * FROM students WHERE resume IS NULL")
    empty_resumes = cursor.fetchall()
    if empty_resumes:
        print("存在未填写个人信息的学生记录：")
        for student in empty_resumes:
            print("学生ID:", student[0], "学生姓名:", student[1])


# 检查数据一致性
def check_data_consistency():
    # 检查简历表中的学生ID和公司ID是否都存在于对应的学生表和公司表中
    cursor.execute("SELECT r.student_id, r.company_id FROM resumes r LEFT JOIN students s ON r.student_id = s.id LEFT JOIN companies c ON r.company_id = c.id WHERE s.id IS NULL OR c.id IS NULL")
    inconsistent_resumes = cursor.fetchall()
    if inconsistent_resumes:
        print("存在简历表中学生ID或公司ID在学生表或公司表中不存在的记录：")
        for resume in inconsistent_resumes:
            print("学生ID:", resume[0], "公司ID:", resume[1])

    # 检查招聘信息表中的公司ID是否存在于公司表中
    cursor.execute("SELECT j.company_id FROM job_postings j LEFT JOIN companies c ON j.company_id = c.id WHERE c.id IS NULL")
    inconsistent_job_postings = cursor.fetchall()
    if inconsistent_job_postings:
        print("存在招聘信息表中公司ID在公司表中不存在的记录：")
        for job_posting in inconsistent_job_postings:
            print("公司ID:", job_posting[0])

# 调用
data_maintenance()
data_backup()
