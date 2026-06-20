import subprocess
print("Welcome To Arch Init | By Li Productions")
print("CHOOSE A TEMPLATE :")
print("-------------------------")
print("BASE : 1")
template_choose = input("CHOOSE TEMPLATE : ")
if template_choose == "1":
    subprocess.run("chmod +x templates-shell/base.sh", shell=True)
    subprocess.run("templates-shell/./base.sh",shell=True)

