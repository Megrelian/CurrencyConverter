


with open("name.txt","r") as f1:
    name = f1.read()

with open ("surname.txt","r") as f2:
    surname = f2.read()


with open("full_namet.xt", "w+") as f3:
    full_name = name + " " +surname
    f3.write(full_name)