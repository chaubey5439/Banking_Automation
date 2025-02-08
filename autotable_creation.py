import sqlite3
con_obj = sqlite3.connect(database= 'bank.sqlite')
cur_obj = con_obj.cursor()

try:
    cur_obj.execute('''create table users(
                    user_acno integer primary key autoincrement,
                    user_pass text,
                    user_name text,
                    user_mob text,
                    user_email text,
                    user_bal float,
                    user_aadhar text,
                    user_opendate datetime,
                    user_acn_type text)
                ''')

    cur_obj.execute('''create table txn(
                    txn_id integer primary key autoincrement,
                    txn_acno int,
                    txn_type text,
                    txn_date datetime,
                    txn_amt float,
                    txn_updated_bal float)
                ''')
    print('tables created')
except:
    pass
con_obj.close()

