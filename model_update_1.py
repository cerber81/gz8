import csv
def read():
    with open('Hogwarts.csv','r',newline='\n',encoding='utf-8') as f:
        r=csv.reader(f,delimiter=";")
        for rec in r:
            print(rec)
def update():
    with open('Hogwarts.csv','r',newline='\n',encoding='utf-8') as f:
        n_id= input('Enter id of employee that you want to change :')
        print('1. Change Name')
        print('2. Change Position')
        print('3. Change Owl ')
        print('4. Change Comments')
        found=0
        r=csv.reader(f,delimiter=";")
        nrec =[]
        for rec in r:
            if rec[0] ==n_id:
                print('Current record:',rec)
                rec[1] = input("Enter the name:")
                print('Updated record:',rec)
                found=1
            nrec.append(rec)

        if found == 0:
            print('no')
            f.close()
        else:
            with open('Hogwarts.csv','w',newline='',encoding='utf-8') as f:
                w=csv.writer(f,delimiter=';')
                w.writerows(nrec)

read()
update()

