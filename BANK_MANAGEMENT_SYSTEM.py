#this project is made by Sourav Dey

import mysql.connector
mysql.connector.connect(host='localhost',user='root',password='1234',database='BANK_MANAGEMENT')

def OpenAcc():
    n=input("Enter The Name: ")
    ac=input("Enter The Account No: ")
    db=input("Enter The Date Of Birth: ")
    add=input("Enter The Address: ")
    cn=input("Enter The Contact Number: ")
    ob=int(input("Enter The Opening Balance: "))
    data1=(n,ac,ob,add,cn,ob)
    data2=(n,ac,ob)
    sql1=('insert into account values (%s,%s,%s,%s,%s,%s)')
    sql2=('insert into amount values(%s,%s,%s)')
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    print("Data Entered Successfully")
    main()
    
def DespoAmo():
    amount=input("Enter The Amount You Want To Deposit: ")
    ac=input("Enter The Account No: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]+amount
    sql=('update amount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()
    
def WithdrawAmount():
    amount=input("Enter The Amount You Want To Withdraw: ")
    ac=input("Enter The Account No: ")
    a='select balance from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    t=result[0]- amount
    sql=('update amount set balance where AccNo=%s')
    d=(t,ac)
    x.execute(sql,d)
    mydb.commit()
    main()

def BalEnq():
    ac=input("Enter The account no: ")
    a='select * from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    print("Balance For account:",ac,"is",result[-1])
    main()
    
def DisDetails():
    ac=input("Enter The account no: ")
    a='select * from account where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(a,data)
    result=x.fetchone()
    for i in result:
        print(i)
    main()
    
def CloseAcc():
    ac=input("Enter The account no: ")
    sql1='delete from account where AccNo=%s'
    sql2='delete from amount where AccNo=%s'
    data=(ac,)
    x=mydb.cursor()
    x.execute(sql1,data1)
    x.execute(sql2,data2)
    mydb.commit()
    main()
    
def main():
    print( ''' 
               1. OPEN NEW ACCOUNT
               2. DEPOSIT AMOUNT
               3. WITHDRAW AMOUNT
               4. BALANCE ENQUIRY
               5. DISPLAY CUSTOMER DETAILS
               6. CLOSE AN ACCOUNT''')
               
    choice = input(" Enter The Task You Want To Perform: ")
    if(choice== '1'):
       OpenAcc()
    elif(choice== '2'):
         DespoAmo()
    elif(choice== '3'):
         WithdrawAmount()
    elif(choice== '4'):
         BalEnq()
    elif(choice== '5'):
         DisDetails()
    elif(choice== '6'):
         CloseAcc()
    else:
        print("Invalid Choice")
main()
    
