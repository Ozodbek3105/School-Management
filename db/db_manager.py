import psycopg2


class Database:
    instance = None

    def __init__(self):
        self.conn = psycopg2.connect(database="school",
                                     host="localhost",
                                     user="postgres",
                                     password="Ozodbek04@",
                                     port="5432")

        self.cursor = self.conn.cursor()
        self.create_tables()

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def create_tables(self):
        sql = """
        CREATE TABLE IF NOT EXISTS students(
            student_id varchar(15) Primary Key,
            names varchar(100),
            gender bool,
            grade integer,
            birthday date,
            age integer,
            address varchar(200),
            phone_number varchar(15),
            email varchar(15)
        )"""
        self.cursor.execute(sql)
        self.conn.commit()

    def student_add(self, student_id, names, gender, grade, birthday, age, address, phone, email):
        sql = """INSERT INTO students(student_id, names, gender,grade,birthday,age,address,phone_number,email)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        self.cursor.execute(sql, (student_id, names, gender, grade, birthday, age, address, phone, email))
        self.conn.commit()

    def student_delete(self, student_id):
        sql = """DELETE FROM students WHERE student_id=%s"""
        self.cursor.execute(sql, (student_id,))
        self.conn.commit()

    def student_update(self, name, student_id):
        sql = """UPDATE  students SET name=%s WHERE student_id=%s"""
        self.cursor.execute(sql, (name, student_id))
        self.conn.commit()

    def student_read(self):
        sql = """SELECT * FROM students"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = Database.get_instance()
    # add
    db.student_add("ozod","csdc",True,4,"2000-02-02",23,"Toshkent",1232312322,"ozod@gmail.com")
    # select
    for row in db.student_read():
        print(row)
