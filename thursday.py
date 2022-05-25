##lines=["name is Dhurba\n","LovesLiverpool\n","Stydy BsCit\n"]
##with open("dhurba.txt","w+") as file:
##    file.writelines(lines)
##    file.seek(0)
##    for line in file.readlines():
##        print(line,end="")

with open("table.txt","w") as file:
    for a in range(1,11):
        file.write("%d*%d=%d\n"%(2,a,2*a))
file.close()

    
