import sqlite3

boglanish = sqlite3.connect("futbolchilar arxivi.db")
kursor = boglanish.cursor()
username = "ronaldo"
password = "practice"
tanlov = int(input("1.Admin\n2.Foydalanuvchi: "))
if(tanlov == 1):
    user = input("Maxsus Usernameni kiriting: ")
    parol = input("Maxsus Parolni kiriting: ")
    if(user != username and parol != password):
        print("Username yoki parol xato!")
    elif(user == username and parol != password):
        print("Password xato!")
    elif(user != username and parol == password):
        print("Username xato!")
    else:
        print("Xush kelibsiz!")
        def Table_qosh():
            kursor.execute("CREATE TABLE IF NOT EXISTS futbolchilar(Name TEXT,Yil INT,Davlat TEXT,Jamoasi TEXT,Pozitsiyasi TEXT)")
            boglanish.commit()
    
        def data_qosh():
            kursor.execute("INSERT INTO futbolchilar VALUES('Ronaldo',1982,'Portugaliya','Manchester United','Hujumchi')")
            boglanish.commit()
        def data_qosh2():
            kursor.execute("INSERT INTO futbolchilar VALUES('Javlonbek',2005,'Ozbekiston','FC Locomotiv','Himoyachi')")
            boglanish.commit()
        def data_qosh3(ism,yil,davlat,klub,position):
            kursor.execute("INSERT INTO futbolchilar VALUES(?,?,?,?,?)",(ism,yil,davlat,klub,position))
            print("Malumotlar Kiritildi!")
            boglanish.commit()
        Table_qosh()
        data_qosh()
        data_qosh2()
        data_qosh3(input("Ism: "),int(input("Yil: ")),input("Davlat: "),input("Klub: "),input("Position: "))
elif(tanlov == 2):
    print("User paneliga Xush kelibsiz!")
    def data_oqi():
        kursor.execute("SELECT * FROM futbolchilar")
        malumotlar = kursor.fetchall()
        for i in malumotlar:
            print(*i)
    data_oqi()