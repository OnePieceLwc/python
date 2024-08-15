import pyodbc

# 连接MySQL数据库
dsn_name = 'lwc'
username = 'root'
password = '318318'


def connect_to_database():
    """连接到MySQL数据库并返回连接对象。"""
    try:
        db = pyodbc.connect(f'DSN={dsn_name};UID={username};PWD={password}')
        print("连接MySQL数据库成功")
        return db
    except pyodbc.Error as e:
        print(f"连接数据库失败: {e}")
        exit()


def create_tables(cursor):
    """创建学生、企业和简历表。"""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                password VARCHAR(255),
                resume TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                contact_person VARCHAR(255),
                email VARCHAR(255),
                job_requirements TEXT
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resumes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT,
                company_id INT,
                status VARCHAR(50),
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (company_id) REFERENCES companies(id)
            )
        """)
        cursor.connection.commit()
    except pyodbc.Error as e:
        print(f"创建表时出错: {e}")

def create_job_postings_table(cursor):
    """创建招聘信息表。"""
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS job_postings (
                id INT AUTO_INCREMENT PRIMARY KEY,
                company_id INT,
                job_description TEXT,
                FOREIGN KEY (company_id) REFERENCES companies(id)
            )
        """)
        cursor.connection.commit()
    except pyodbc.Error as e:
        print(f"创建招聘信息表时出错: {e}")

def student_register(cursor, name, password):
    """学生注册功能。"""
    try:
        # 直接插入，不检查用户名是否已存在
        sql = "INSERT INTO students (name, password) VALUES (?, ?)"
        cursor.execute(sql, (name, password))
        cursor.connection.commit()
        print("学生注册成功")
    except pyodbc.Error as e:
        print(f"注册时出错: {e}")


def student_login(cursor, name, password):
    """学生登录功能。"""
    try:
        sql = "SELECT * FROM students WHERE name = ? AND password = ?"
        cursor.execute(sql, (name, password))
        result = cursor.fetchone()
        if result:
            print("学生登录成功")
        else:
            print("学生登录失败")
    except pyodbc.Error as e:
        print(f"登录时出错: {e}")


def fill_personal_info(cursor, student_id, resume):
    """学生填写个人信息和简历。"""
    try:
        sql = "UPDATE students SET resume = ? WHERE id = ?"
        cursor.execute(sql, (resume, student_id))
        cursor.connection.commit()
        print("个人信息和简历填写成功")
    except pyodbc.Error as e:
        print(f"填写信息时出错: {e}")


def send_resume(cursor, student_id, company_id):
    """学生发送简历功能。"""
    try:
        # 检查学生和公司是否存在
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student_result = cursor.fetchone()

        cursor.execute("SELECT * FROM companies WHERE id = ?", (company_id,))
        company_result = cursor.fetchone()

        if student_result and company_result:
            cursor.execute("SELECT * FROM resumes WHERE student_id = ? AND company_id = ?", (student_id, company_id))
            resume_result = cursor.fetchone()

            if resume_result:
                print("已经发送过简历")
            else:
                cursor.execute("INSERT INTO resumes (student_id, company_id, status) VALUES (?, ?, ?)",
                               (student_id, company_id, "待审核"))
                cursor.connection.commit()
                print("简历发送成功")
        else:
            print("学生或公司不存在")
    except pyodbc.Error as e:
        print(f"发送简历时出错: {e}")


def company_register(cursor, name, contact_person, email):
    """企业注册功能。"""
    try:
        sql = "INSERT INTO companies (name, contact_person, email) VALUES (?, ?, ?)"
        cursor.execute(sql, (name, contact_person, email))
        cursor.connection.commit()
        print("企业注册成功")
    except pyodbc.Error as e:
        print(f"企业注册时出错: {e}")


def company_login(cursor, name, email):
    """企业登录功能。"""
    try:
        sql = "SELECT * FROM companies WHERE name = ? AND email = ?"
        cursor.execute(sql, (name, email))
        result = cursor.fetchone()
        if result:
            print("企业登录成功")
        else:
            print("企业登录失败")
    except pyodbc.Error as e:
        print(f"企业登录时出错: {e}")


def publish_job(cursor, company_id, job_requirements):
    """发布招聘信息功能。"""
    try:
        sql = "UPDATE companies SET job_requirements = ? WHERE id = ?"
        cursor.execute(sql, (job_requirements, company_id))
        cursor.connection.commit()
        print("招聘信息发布成功")
    except pyodbc.Error as e:
        print(f"发布招聘信息时出错: {e}")


def close_connection(db):
    """关闭数据库连接。"""
    try:
        db.close()
        print("数据库连接已关闭")
    except pyodbc.Error as e:
        print(f"关闭连接时出错: {e}")

# 前台操作模块
def update_company_info(cursor, company_id, company_info):
    """更新公司信息。"""
    try:
        sql = "UPDATE companies SET job_requirements = ? WHERE id = ?"
        cursor.execute(sql, (company_info, company_id))
        cursor.connection.commit()
        print("公司信息更新成功")
    except pyodbc.Error as e:
        print(f"更新公司信息时出错: {e}")

def user_login(cursor, username, password, user_type):
    """用户登录功能。"""
    try:
        if user_type == "student":
            sql = "SELECT * FROM students WHERE name = ? AND password = ?"
        elif user_type == "company":
            sql = "SELECT * FROM companies WHERE name = ? AND email = ?"
        cursor.execute(sql, (username, password))
        result = cursor.fetchone()
        if result:
            print("用户登录成功")
        else:
            print("用户登录失败")
    except pyodbc.Error as e:
        print(f"用户登录时出错: {e}")

def user_register(cursor, username, password, user_type):
    """用户注册功能。"""
    try:
        if user_type == "student":
            sql = "INSERT INTO students (name, password) VALUES (?, ?)"
        elif user_type == "company":
            sql = "INSERT INTO companies (name, contact_person) VALUES (?, ?)"
        cursor.execute(sql, (username, password))
        cursor.connection.commit()
        print("用户注册成功")
    except pyodbc.Error as e:
        print(f"用户注册时出错: {e}")

def search_company(cursor, company_id):
    """查询公司信息。"""
    try:
        sql = "SELECT * FROM companies WHERE id = ?"
        cursor.execute(sql, (company_id,))
        result = cursor.fetchone()
        if result:
            print("查询到公司信息：", result)
        else:
            print("未找到公司信息")
    except pyodbc.Error as e:
        print(f"查询公司时出错: {e}")

def search_student(cursor, student_name):
    """查询学生信息。"""
    try:
        sql = "SELECT * FROM students WHERE name = ?"
        cursor.execute(sql, (student_name,))
        results = cursor.fetchall()
        if results:
            print("查询到学生信息：")
            for student in results:
                print("学生ID:", student[0], "学生姓名:", student[1], "密码:", student[2], "简历:", student[3])
        else:
            print("未找到学生信息")
    except pyodbc.Error as e:
        print(f"查询学生时出错: {e}")

def view_job_postings(cursor):
    """查看招聘信息。"""
    try:
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
    except pyodbc.Error as e:
        print(f"查看招聘信息时出错: {e}")

# 管理员模块
def data_maintenance(cursor):
    """数据维护功能。"""
    try:
        # 检查数据完整性
        print("开始检查数据完整性...")

        # 检查学生表中是否存在重复的学生记录
        cursor.execute("SELECT name, COUNT(*) FROM students GROUP BY name HAVING COUNT(*) > 1")
        duplicate_students = cursor.fetchall()
        if duplicate_students:
            print("存在重复的学生记录：")
            for student in duplicate_students:
                print("学生姓名:", student[0], "重复次数:", student[1])
        else:
            print("没有发现重复的学生记录。")

        # 检查学生表中是否存在未填写个人信息的记录
        cursor.execute("SELECT * FROM students WHERE resume IS NULL")
        empty_resumes = cursor.fetchall()
        if empty_resumes:
            print("存在未填写个人信息的学生记录：")
            for student in empty_resumes:
                print("学生ID:", student[0], "学生姓名:", student[1])
        else:
            print("所有学生均已填写个人信息。")

        # 检查数据一致性
        print("开始检查数据一致性...")

        # 检查简历表中的学生ID和公司ID是否都存在于对应的学生表和公司表中
        cursor.execute("""
            SELECT r.student_id, r.company_id 
            FROM resumes r 
            LEFT JOIN students s ON r.student_id = s.id 
            LEFT JOIN companies c ON r.company_id = c.id 
            WHERE s.id IS NULL OR c.id IS NULL
        """)
        inconsistent_resumes = cursor.fetchall()
        if inconsistent_resumes:
            print("存在简历表中学生ID或公司ID在学生表或公司表中不存在的记录：")
            for resume in inconsistent_resumes:
                print("学生ID:", resume[0], "公司ID:", resume[1])
        else:
            print("简历表中的学生ID和公司ID均有效。")

        # 检查招聘信息表中的公司ID是否存在于公司表中
        cursor.execute("""
            SELECT j.company_id 
            FROM job_postings j 
            LEFT JOIN companies c ON j.company_id = c.id 
            WHERE c.id IS NULL
        """)
        inconsistent_job_postings = cursor.fetchall()
        if inconsistent_job_postings:
            print("存在招聘信息表中公司ID在公司表中不存在的记录：")
            for job_posting in inconsistent_job_postings:
                print("公司ID:", job_posting[0])
        else:
            print("所有招聘信息的公司ID均有效。")

        print("数据维护完成")
    except pyodbc.Error as e:
        print(f"数据维护时出错: {e}")

def data_backup(cursor):
    """数据备份功能。"""
    try:
        query = "SELECT * FROM students"
        cursor.execute(query)
        rows = cursor.fetchall()

        with open('backup.csv', 'w') as file:
            for row in rows:
                file.write(','.join([str(value) for value in row]) + '\n')

        print("数据备份完成")
    except pyodbc.Error as e:
        print(f"数据备份时出错: {e}")

def check_data_integrity(cursor):
    """检查数据完整性。"""
    try:
        cursor.execute("SELECT name, COUNT(*) FROM students GROUP BY name HAVING COUNT(*) > 1")
        duplicate_students = cursor.fetchall()
        if duplicate_students:
            print("存在重复的学生记录：")
            for student in duplicate_students:
                print("学生姓名:", student[0], "重复次数:", student[1])

        cursor.execute("SELECT * FROM students WHERE resume IS NULL")
        empty_resumes = cursor.fetchall()
        if empty_resumes:
            print("存在未填写个人信息的学生记录：")
            for student in empty_resumes:
                print("学生ID:", student[0], "学生姓名:", student[1])
    except pyodbc.Error as e:
        print(f"检查数据完整性时出错: {e}")

def check_data_consistency(cursor):
    """检查数据一致性。"""
    try:
        cursor.execute("SELECT r.student_id, r.company_id FROM resumes r LEFT JOIN students s ON r.student_id = s.id LEFT JOIN companies c ON r.company_id = c.id WHERE s.id IS NULL OR c.id IS NULL")
        inconsistent_resumes = cursor.fetchall()
        if inconsistent_resumes:
            print("存在简历表中学生ID或公司ID在学生表或公司表中不存在的记录：")
            for resume in inconsistent_resumes:
                print("学生ID:", resume[0], "公司ID:", resume[1])

        cursor.execute("SELECT j.company_id FROM job_postings j LEFT JOIN companies c ON j.company_id = c.id WHERE c.id IS NULL")
        inconsistent_job_postings = cursor.fetchall()
        if inconsistent_job_postings:
            print("存在招聘信息表中公司ID在公司表中不存在的记录：")
            for job_posting in inconsistent_job_postings:
                print("公司ID:", job_posting[0])
    except pyodbc.Error as e:
        print(f"检查数据一致性时出错: {e}")

def main_menu(cursor):
    """主菜单，提供操作选项。"""
    while True:
        print("\n欢迎使用学生与企业管理系统")
        print("1. 学生注册")
        print("2. 学生登录")
        print("3. 填写个人信息")
        print("4. 发送简历")
        print("5. 企业注册")
        print("6. 企业登录")
        print("7. 发布招聘信息")
        print("8. 查询公司信息")
        print("9. 查询学生信息")
        print("10. 查看招聘信息")
        print("11. 数据维护")
        print("12. 数据备份")
        print("0. 退出")

        choice = input("请选择操作（0-12）：")

        if choice == '1':
            name = input("请输入学生姓名：")
            password = input("请输入密码：")
            student_register(cursor, name, password)
        elif choice == '2':
            name = input("请输入学生姓名：")
            password = input("请输入密码：")
            student_login(cursor, name, password)
        elif choice == '3':
            student_id = int(input("请输入学生ID："))
            resume = input("请输入简历内容：")
            fill_personal_info(cursor, student_id, resume)
        elif choice == '4':
            student_id = int(input("请输入学生ID："))
            company_id = int(input("请输入公司ID："))
            send_resume(cursor, student_id, company_id)
        elif choice == '5':
            name = input("请输入公司名称：")
            contact_person = input("请输入联系人：")
            email = input("请输入电子邮件：")
            company_register(cursor, name, contact_person, email)
        elif choice == '6':
            name = input("请输入公司名称：")
            email = input("请输入电子邮件：")
            company_login(cursor, name, email)
        elif choice == '7':
            company_id = int(input("请输入公司ID："))
            job_requirements = input("请输入招聘要求：")
            publish_job(cursor, company_id, job_requirements)
        elif choice == '8':
            company_id = int(input("请输入公司ID："))
            search_company(cursor, company_id)
        elif choice == '9':
            student_name = input("请输入学生姓名：")
            search_student(cursor, student_name)
        elif choice == '10':
            view_job_postings(cursor)
        elif choice == '11':
            data_maintenance(cursor)
        elif choice == '12':
            data_backup(cursor)
        elif choice == '0':
            print("退出系统")
            break
        else:
            print("无效的选择，请重新输入。")

# 主程序
if __name__ == "__main__":
    db = connect_to_database()
    cursor = db.cursor()

    create_tables(cursor)
    create_job_postings_table(cursor)

    main_menu(cursor)  # 调用主菜单

    close_connection(db)
