empname=["abc","adfaf","fasfd","gfdsg"]
print(empname)
for emp in empname:
    print(emp)
for i,name in enumerate(empname):
    print(i,name)
for i in range(1,10):
    print(i)
empdict={
        "id": 1,
        "name": "adfs",
        "domain": "devops"
        }
for emp_key in empdict.keys():
    print(emp_key)
for emp_values in empdict.values():
    print(emp_values)
for key,value in empdict.items():
    print(key,value)
