import sqlite3

conn = sqlite3.connect("Bank.db")

cursor = conn.cursor()

# cursor.execute(f"insert into Account(name,phone,aadhar,dob,gender,address,acc_type,amount,account_number) values('Bhavani' ,987654321,123456567232, '03-02-2000', 'Female', 'hyd', 'savings account', 500,1234556788)")

# cursor.execute(''' Create Table Account(
#                name Varchar(32) not null, phone number(10) check(length(phone=10)),
#                aadhar number(12) unique not null,
#                dob date,
#                address varchar(100) not null,
#                account_num  INTEGER PRIMARY KEY AUTOINCREMENT,
#                gender varchar(7),
#                pin number(4) default(0),
#                amount number(8,2),
#                acc_type varchar(10) not null) ''')

def acc_creation(name,dob,phone,address,aadhar,gender,acc_type):
   cursor.execute(f"insert into Account(name,dob,phone,address,aadhar,gender,acc_type,amount) values('{name}','{dob}', {phone},'{address}',{aadhar},'{gender}','{acc_type}',500)")

   conn.commit()
   print("acc created successfully")

def pin_generation(acc,pin,c_pin):
    # data = cursor.execute(f" select * from Account where account_num = {acc}")
    # print(data)
    if pin == c_pin:
        cursor.execute(f"update Account set pin = {pin} where account_num = {acc}")
        conn.commit()
        print("successfully set pin, don't share with anyone")
    else:
        print("pin and confirm pin dont match")

def balance(acc,pin):
    data = cursor.execute(f"select * from Account where account_num = {acc}")
    result = data.fetchone()

    if(pin == result[-3]):
        print(f"balance is {result[-2]}")
    else:
        print("invalid pin")

def deposit(acc,pin):
    data = cursor.execute(f"select * from Account where account_num = {acc}")
    var = data.fetchone()
    if pin == var[-3]:
        amt = float(input("Paisaa donaaa"))
        if amt >=100 and amt <=1000:
           money = var[-2]
           cursor.execute(f"update Account set amount = {amt+money} where account_num = {acc}")
           conn.commit()
        
           print("Sab bara bar hai doubt hai tho khud se check karle")
        else:
             print("invalid amount")
    else:
        print("re-enter the pin")


def withdrawal(acc,pin):
    data = cursor.execute(f"select * from Account where account_num = {acc}")
    var = data.fetchone()
    if pin == var[-3]:
        money = var[-2]
        amt = float(input("enter the amt:"))
        if amt<=var[-2] and amt<10000 and amt >=100:
            cursor.execute(f"update Account set amount = {money - amt} where account_num = {acc}")
            conn.commit()
            print(f"{amt} has been withdrawed successfully")
        else:
            print("invalid amt")
    else:
        print("invalid pin")


def acc_transfer(from_acc, to_acc,pin):
    data = cursor.execute(f"Select * from Account where account_num = {from_acc}")
    from_account = data.fetchone()
    if pin == from_account[-3]:
        amt = float(input("enter the money"))
        if amt<= from_account[-2] and amt >=100:
            cursor.execute(f"update Account set amount = {from_account[-2]-amt} where account_num = {from_acc}")
            conn.commit()


            data1 = cursor.execute(f"select * from Account where account_num ={to_acc}")
            to_account = data1.fetchone()

            cursor.execute(f"update Account set amount = {to_account[-2]+amt} where account_num = = {to_acc}")
            conn.commit()
            print("amt transfered successfully")
        else:
            print("invalid amt")
    else:
        print("invalid pin")

print("*"*40)
user_input = int(input('''welcome to SBI\n choose the below options  \n 1)Account Creation \n 2) Pin Generation \n 3) Balance Enquiry\n 4) Withdrawl \n 5) Deposit \n 6) Account Transefer \n'''))
# print(user_input)
if user_input == 1:
    print("thanks for choosing our bank:")
    name = input("enter your sweet name:")
    dob = input("enter when the hell did you born :")
    phone = input("baby number do naa.....! :")
    address = input("address pettu :")
    aadhar = input("enter the aadhar number :")
    gender = input("sir miru madam ahh :")
    acc_type = input("what your type....(account) :")
    acc_creation(name,dob,phone,address,aadhar,gender,acc_type)

elif user_input ==2:
    print("********* GENERATE YOUR PIN **********")
    acc = int(input("ENTER THE ACCOUNT NUMBER"))
    pin = int(input("ENTER YOUR PIN"))
    c_pin = int(input("CONFIRM PIN"))
    pin_generation(acc,pin,c_pin)

elif user_input == 3:
    print("************BALANCE ENQUIRY *************")
    acc= int(input("ENTER THE ACCOUNT NUMBER"))
    pin = int(input("ENTER YOUR PIN"))
    balance(acc,pin)
elif user_input == 4:
    print("******DEPOIST*********")
    acc= int(input("ENTER THE ACCOUNT NUMBER"))
    pin = int(input("ENTER THE PIN"))
    deposit(acc,pin)
elif user_input == 5:
      print("*******WITHDRAWAL*********")
      acc= int(input("ENTER THE ACCOUNT NUMBER"))
      pin = int(input("ENTER THE PIN"))
      withdrawal(acc,pin)
elif user_input == 6:
    print("*******WITHDRAWAL*********")
    from_acc= int(input("ENTER THE ACCOUNT NUMBER"))
    to_acc = int("ENTER THE ACCOUNT NUMBER ")
    pin = int(input("ENTER THE PIN"))
    acc_transfer(from_acc,to_acc, pin)
else:
    quit()