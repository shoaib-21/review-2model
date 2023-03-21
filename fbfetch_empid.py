import faceRecog
import RRead
import time
import lock
import userdb
import find_fingerprint
import user_login_images
import user_login_register


path = '/home/pi/facial-recognition-main/adminsdk.json'
db = userdb.initializeDB(path)
db2 = user_login_register.initializeDB(r'/home/pi/facial-recognition-main/user-login-register-firebase.json')
print('db2 :' , db2)
cred = user_login_images.initializeImagedb()

while True:
    lock.doorlock()
    
    print("1. RFID /t 2.FINGERPRINT /n" )
    choice = int(input("enter a choice: "))
    authorizeduser=""
    if(choice == 1):
        rfid,rfid_username = RRead.readRfid()
        print(rfid_username)
        #print(rfid)
        rfid_verified = userdb.get_rfid(db,rfid)
        if rfid_verified == rfid_username:
            authorizeduser = faceRecog.Face(rfid_username)
            print(authorizeduser)
        else:
            print("unauthorized rfid card... please try again")
            continue
    elif(choice == 2):
        empid = find_fingerprint.get_fingerprint()
        print(empid)
        if empid == False:
            print("fingerperint not found....  please try again")
            continue
        username=userdb.get_empname(db,empid)
        print(username)
        	
#         if template == 1:
#             username = "shaik sharfuddin"
#         elif template == 2:
#             username = "mustafa"
#         elif template == 3:
#            username = "noor"
        authorizeduser = faceRecog.Face(username)
        print(authorizeduser)
        
    if authorizeduser == False:
        print("Face not matched!!!!   door cannot be open")
        
    else:
        #imgUrl=user_login_images.uploadImage(cred,username,username,authorizeduser)
        #user_login_register.create_entry(username,imgUrl,db2)
        #print("door unlocks...")
        lock.doorunlock()

