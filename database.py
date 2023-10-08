import sqlite3

con = sqlite3.connect("superbarbershop.db")
c = con.cursor()

# USERS
c.execute('''CREATE TABLE IF NOT EXISTS users
             (chat_id INTEGER PRIMARY KEY,
              username TEXT,
              full_name TEXT,
              phone TEXT)
              ''')

# EMPLOYEES
c.execute('''CREATE TABLE IF NOT EXISTS employees
             (employee_id INTEGER PRIMARY KEY,
              full_name TEXT,
              role TEXT,
              phone TEXT)
              ''')

c.execute('''INSERT INTO employees (full_name, role, phone) VALUES
             ('Andriy Melnikov','Owner','+380123456789'),
             ('Milana Pavun','Master hairdresser','+380987654321'),
             ('Pavlo Mazilo','Hairdresser','+380654321789'),
             ('Melon Krabik','Trainee','+380321654987');
             ''')

# SCHEDULE
c.execute('''CREATE TABLE IF NOT EXISTS schedule
             (schedule_id INTEGER PRIMARY KEY,
              employee INTEGER,
              date TEXT,
              start_time TEXT,
              shift_time REAL,
              FOREIGN KEY(employee) REFERENCES employees(employee_id))
              ''')

'''

c.execute( _ _ _ INSERT INTO schedule (employee, date, start_time, shift_time) VALUES
             (,'','',10),
             (,'','',8),
             (,'','',10),
             (,'','',8),
             (,'','',6),
             (,'','',6),
             (,'','',6);
             _ _ _)

'''
             
# SERVICES
c.execute('''CREATE TABLE IF NOT EXISTS services
             (service_id INTEGER PRIMARY KEY,
              service_name TEXT,
              service_info TEXT,
              price REAL,
              time REAL)
              ''')

c.execute('''INSERT INTO services (service_name, service_info, price, time) VALUES
             ('Master cut','',60,60),
             ('Master long hair','',75,60),
             ('Master beard trim','',40,40),
             ('Master shave','',50,60),
             ('Master head shave','',50,40),
             ('Buzz cut','',30,30),
             ('Kids cut','',40,30),
             ('Braids','per hour',100,60);
             ''')

# APPOINTMENTS
c.execute('''CREATE TABLE IF NOT EXISTS appointments
             (app_id INTEGER PRIMARY KEY,
              app_date TEXT,
              app_time TEXT,
              comments TEXT,
              service INTEGER,
              user INTEGER,
              FOREIGN KEY(service) REFERENCES services(service_id),
              FOREIGN KEY(user) REFERENCES users(chat_id)
              )''')

con.commit()
