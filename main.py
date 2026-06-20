import subprocess
base_location = "src/templates-shell/base.sh"
print("Welcome To Arch Init | By Li Productions")
print("CHOOSE A TEMPLATE :")
print("-------------------------")
print("BASE : 1")
print("This Installs, Git,YAY,Fastfetch,BASE-DEVEL,VS CODE")
print("This Installs A Community Version OF VS CODE Or If You Are On GNOME You CAN Just Download The Flathub Version In The GNOME APP STORE")
print(f"This is gonna run base.sh located at {base_location}")
template_choose = input("CHOOSE TEMPLATE : ")
if template_choose == "1":
    subprocess.run("chmod +x src/templates-shell/base.sh", shell=True)
    subprocess.run("src/templates-shell/./base.sh",shell=True)

