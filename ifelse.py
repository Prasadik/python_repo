empdict={
        "id":111,
        "name":"abc",
        "domain":"Devops",
        }
empname=["abc","dfsa","sdadsfa","dsfaf"]
if "abc" in empname:
    print("abc found in list")
else:
    print("abc not found in list")
if "abc" not in empname:
    print("abc not in the list")
else:
    print("abc is in the list")
if empname:
    print("list is not empty")
else:
    print("list is empty")
if not empname:
    print("list is empty2")
else:
    print("list is not empty2")
if "id" in empdict:
    print("id found in dictionary")
else:
    print("id not found in dictionary")
if "abc" in empdict.values():
    print("abc is present in dictionary")
else:
    print("abc is not present in dictionary")
if empdict["name"] == "abc":
    print("abc is found in dictionary")
else:
    print("abc is not found in dictionary")
str = "Devops Engineer"
strlower = str.lower()
print(strlower)
strupper=str.upper()
print(strupper)
if str.startswith("devops"):
    print("starts with devops pattern")
else:
    print("does not starts with devops pattern")
if str.lower().startswith("dev"):
    print("starts with dev pattern")
else:
    print("does not starts with dev pattern")
str1= "devops sre release"
strreplace=str1.replace(" ", ",")
print(strreplace)
val1,val2=strreplace.split(",",1)
print(val1,val2)
val1,val2,val3=strreplace.split(",",2)
print(val1,val2,val3)
val1,val2=strreplace.rsplit(",",1)
print(val1,val2)


