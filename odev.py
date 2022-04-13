import json
import time
user_list=[]
def register_user():
    print("-"*30)
    username = input("Kullanici Adi Giriniz : ")
    name = input("Isim Giriniz : ")
    surname = input("Soyisim Giriniz : ")
    email = input("E-mail Giriniz : ")
    password = input("Sifre Giriniz : ")
    user_template = {
    "Username":"",
    "Name":"",
    "Surname":"",
    "E-mail":"",
    "Password":""
}
    user_template["Username"]= username
    user_template["Name"] = name
    user_template["Surname"] = surname
    user_template["E-mail"] = email
    user_template["Password"] = password
    user_list.append(user_template)
    return user_list
def show_users():
    i=0
    while i in range(0,len(user_list)):
        print("-"*30+"\n"+"Kullanici Adi : "+user_list[i]["Username"]+"\nIsim : "+user_list[i]["Name"]+"\nSoyisim : "+user_list[i]["E-mail"]+"\nSifre : "+user_list[i]["Password"]+"\n"+"-"*30)
        i+=1
def update_user():
    usernamex = input("Degistirmek istediginiz kullanicinin kullanici adini giriniz : ")
    for a in range(0,len(user_list)) :
        if usernamex == user_list[a]["Username"]:
            updated_username = input("Yeni kullanici adi giriniz : ")
            user_list[a]["Username"] = updated_username
            updated_name = input("Yeni isim giriniz : ")
            user_list[a]["Name"] = updated_name
            updated_surname = input("Yeni soyismi giriniz : ")
            user_list[a]["Surname"] = updated_surname
            updated_email = input("Yeni e-mail adresi giriniz : ")
            user_list[a]["E-mail"] = updated_email
            updated_password = input("Yeni sifre giriniz : ")
            user_list[a]["Password"] = updated_password
    print("\n"+"="*30+"\nKullanici guncellemeyi basardiniz ! Ana menuye yonlendiriliyorsunuz ...")
def delete_user():
    usernamey = input("Guncellemek istediginiz kullanicinin kullanici adini giriniz : ")
    for y in range(0,len(user_list)) :
        if usernamey == user_list[y]["Username"]:
            user_list.pop(y)
            
def save_users():  
    writeData = json.dumps(user_list)
    f = open("demirlog", "a")
    f.write(writeData)
    f.close()
    print("\n"+"="*30+"\nKullanicilari kaydetmeyi basardiniz ! Ana menuye yonlendiriliyorsunuz ...")
def ui():
    print("-"*30+"\n"+"Kullanıcı Veri Tabanına Hoş Geldiniz ! \n"+"-"*30)
    print("Lutfen Yapmak Istediginiz Islemin Numarasini Giriniz \n"+"="*30)
    op = input("1 - Kullanici Ekleme \n2 - Kullanicilari Silme \n3 - Kullanicilari Gorme \n4 - Kullanici Guncelleme \n5 - Kullanicilari Kaydetme"+"\n6 - Uygulamadan Cikis\n"+"="*30+"\n-->")
    if op == "1" :
        register_user()
        print("Kullanici eklemeyi basardiniz ! Ana menuye yonlendiriliyorsunuz ...")
        time.sleep(2)
        ui()
    elif op == "2" :
        delete_user()
        print("\n"+"="*30+"\nKullanici silmeyi basardiniz ! Ana menuye yonlendiriliyorsunuz ...")
        time.sleep(2)
        ui()
    elif op == "3" :
        show_users()
        print("\n"+"="*30+"\nKullanicilari gostermeyi basardiniz ! Ana menuye yonlendirilmek icin herhangi bir tusa basin")
        main_menu = input("")
        print(main_menu)
        time.sleep(2)
        ui()
    elif op == "4" :
        update_user()
        time.sleep(2)
        ui()
    elif op == "5" :
        save_users()
        time.sleep(2)
        ui()
    elif op == "6" :
        print("Gorusmek Uzere ..!")
        time.sleep(2)
        exit()
    else : 
        print("Uygun Islem Numarasi Seciniz !..")
        time.sleep(2)
        ui()
ui()
#Class kullanmadığım için def main fonksiyonuna da ihtiyacım kalmadı.  Çok fazla eksiğim var ama bu eksikleri nasıl düzelteceğimi bilmiyorum :) #