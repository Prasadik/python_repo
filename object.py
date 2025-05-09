class exp1:
    def __init__(self,name,domain):
        self.name=name
        self.skill=domain
    def display(self):
        print(self.name,self.skill)

if __name__=="__main__":
    name=input("Enter the name")
    domain=input("Enter the domain")
    obj=exp1(name,domain)
    obj.display()
