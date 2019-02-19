import subprocess

print ("""



MMMMMMMM               MMMMMMMM                 RRRRRRRRRRRRRRRRR                    XXXXXXX       XXXXXXX
M:::::::M             M:::::::M                 R::::::::::::::::R                   X:::::X       X:::::X
M::::::::M           M::::::::M                 R::::::RRRRRR:::::R                  X:::::X       X:::::X
M:::::::::M         M:::::::::M                 RR:::::R     R:::::R                 X::::::X     X::::::X
M::::::::::M       M::::::::::M                   R::::R     R:::::R                 XXX:::::X   X:::::XXX
M:::::::::::M     M:::::::::::M                   R::::R     R:::::R                    X:::::X X:::::X
M:::::::M::::M   M::::M:::::::M                   R::::RRRRRR:::::R                      X:::::X:::::X
M::::::M M::::M M::::M M::::::M ---------------   R:::::::::::::RR   ---------------      X:::::::::X
M::::::M  M::::M::::M  M::::::M -:::::::::::::-   R::::RRRRRR:::::R  -:::::::::::::-      X:::::::::X
M::::::M   M:::::::M   M::::::M ---------------   R::::R     R:::::R ---------------     X:::::X:::::X
M::::::M    M:::::M    M::::::M                   R::::R     R:::::R                    X:::::X X:::::X
M::::::M     MMMMM     M::::::M                   R::::R     R:::::R                 XXX:::::X   X:::::XXX
M::::::M               M::::::M                 RR:::::R     R:::::R                 X::::::X     X::::::X
M::::::M               M::::::M                 R::::::R     R:::::R                 X:::::X       X:::::X
M::::::M               M::::::M                 R::::::R     R:::::R                 X:::::X       X:::::X
MMMMMMMM               MMMMMMMM                 RRRRRRRR     RRRRRRR                 XXXXXXX       XXXXXXX



""")

#this tool coded by MRX - don't change anything

print ("-------------------------------waiting-------------------------------")

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
for i in a:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print ("{:<30}|  {:<}".format(i, results[0]))
        except IndexError:
            print ("{:<30}|  {:<}".format(i, ""))
    except subprocess.CalledProcessError:
        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
a = input("")
