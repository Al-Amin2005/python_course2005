#name = "sn"

#if(len(name)==0):
#    print("failed")
#else:
#    if(len(name)<2):
#        print("the len name length must be minimum 2")
#    else:
#        print("success")    

name = "salman"
phone = "01302413198"
email = "s"

if(len(name)==0 or len(phone)==0 or len(email)==0):
    status = "failed"
    print(status)

else:
    if(len(name)<2):
        print("the len name length must be minimum 2 ")
    elif(len(phone)!=11):
        print("the phone number size must be equal to 11")
    else:
        print("success")

