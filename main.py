import os
import base64

if not os.path.exists("master.txt"):
     print("Set your Master Password 🔐")
     new_pass=input("Create password: ")

     with open("master.txt","w") as f:
          f.write(new_pass)
     print("Password set successfully! Restart app.")
     exit()
else:
    with open("master.txt","r") as f:
         saved_pass=f.read()

    user_input=input("Enter master password: ")

    if user_input!=saved_pass:
       print("Wrong password! access denied ❌")
       exit()
    else:
     print("Access granted✅")
passwords=[]
while True:
    print("\n======PASSWORD MANAGER 🔐=======")

    print("1. ADD PASSWORD")
    print("2. VIEW PASSWORDS")
    print("3. DELETE PASSWORDS")
    print("4. SEARCH PASSWORD")
    print("5. CHANGE MASTER PASSWORD")
    print("6. EXIT")

    print("=============================")

    choice=input("\nEnter your choice (1-4): ")

    if choice =="1":
        app=input("Enter app name: ")
        pwd=input("Enter Pasword: ")
        encoded_pwd=base64.b64encode(pwd.encode()).decode()

        with open("data.txt","a") as f:
              f.write(app+","+encoded_pwd+"\n")
        print("password saved to file!")

    elif choice == "2":
             show=input("Do You Want To See Passwords? (yes/no): ").lower()

             with open("data.txt", "r") as f:
                lines = f.readlines()

             count = 1

             for line in lines:
                     data = line.strip().split(",")
                     
                     decoded_pwd=base64.b64decode(data[1]).decode()
                     if show == "yes":
                          print(f"{count}.App: {data[0]} | password: {decoded_pwd}")
                     else:
                        hidden = "*" * len(decoded_pwd) 
                        print(f"{count}. App: {data[0]} | Password: {hidden}")  
                     count+=1
    elif choice =="3":
           with open("data.txt", "r") as f:
                 lines=f.readlines()
           if len(lines)==0:
                 print("No passwords to delete!")
           else:
                 print("\n select password to delete:")

                 for i in range(len(lines)):
                       data=lines[i].strip().split(",")
                       print(f"{i+1}. {data[0]}")
                 try:
                     num = int(input("Enter number to delete: "))
                    
                     if num > 0 and num <= len(lines):
                       lines.pop(num-1)

                       with open("data.txt", "w") as f:
                        f.writelines(lines)

                       print("Password deleted successfully!")
                     else: 
                       print("Invalid number!")
                 except:
                      print("please enter numbers only!")
    elif choice=="4":
         search=input("Enter app name to search:").lower()

         found=False

         with open("data.txt","r") as f:
              lines=f.readlines()
         for line in lines:
              data=line.strip().split(",")
              app=data[0].lower()
              decoded_pwd=base64.b64decode(data[1]).decode()

              if search in app:
                   hidden="*"* len(decoded_pwd)
                   print(f"Found-> App:{data[0]}| Password:{hidden}")
                   found=True
         if not found:
              print("No matching app found ❌")
    elif choice=="5":
         old=input("Enter old password: ")
         with open ("master.txt","r")as f:
              saved=f.read()
         if old==saved:
              new=input("Enter new Password: ")
              with open("master.txt","w") as f:
                   f.write(new)
              print("Password Changed Successfully ✅" )
         else:
              print("Wrong old password ❌")
    elif choice =="6":
            print("\nExiting...Thank you! 👋")
            break
    else:
            print("\nINVALID CHOICE ! PLEASE ENTER 1-4 ONLY.")
