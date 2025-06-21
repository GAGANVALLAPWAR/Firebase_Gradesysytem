import firebase_admin
from firebase_admin import credentials, db
cred=credentials.Certificate("C:/Users/Lenovo/OneDrive/Desktop/Python Basis/newpython-27ed2-firebase-adminsdk-fbsvc-eb058be97e.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app (cred,{"databaseURL":"https://newpython-27ed2-default-rtdb.firebaseio.com/"})

totalmarks=0
for i in range(6):
    marks=int(input(f"enter subject: {i}"))
    totalmarks+=marks
    print(totalmarks)
avg=totalmarks/6
print(avg)


if(avg>=95):
    b="A+"

elif(avg>=85):
    b="A"

elif(avg>=70):
    b="B"

elif(avg>=60):
    b="C"

elif(avg>35):
    b="D"

else:
    b="fail"



ref=db.reference('Grade_Systemss')
ref.push({"percentage is: ":avg,
          "grade is: ":b})

print("data sent successfully...!")