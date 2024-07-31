contactname=[]
contactnumber=[]

class Contact:
    def AddContact(self, name , number):
        self.name=name
        self.number=number
        contactname.append(self.name)
        contactnumber.append(self.number)
    
    def ReadContact(self):
        count=0
        for item in contactname:
            if contactnumber[count]==0:
                print(count+1,'.',contactname[count])
            else:
                print(count+1,'.',contactname[count],'-->',contactnumber[count])
            count = count + 1
    
    def UpdateContact(self):
        unum=int(input('Enter which contact you want edit: '))
        unum = unum - 1
        print('which item do you want to edit: ')
        print('1.Contact Name.')
        print('2.Contact Number.')
        uitem=int(input('Enter your choice: '))
        if uitem==1:
            contactname[unum]=input('Enter new contact name: ')
        elif uitem==2:
            contactnumber[unum]=input('Enter new contact number: ')
            
    def DeleteContact(self):
        dnum=int(input('enter which contact you want delete: '))
        dnum = dnum -1
        contactname.pop(dnum)
        contactnumber.pop(dnum)
ContactBook=Contact()  
choice =0
while choice!='5':
    print('1. Add Contact')
    print('2. Read Contact')
    print('3. Update Contact')
    print('4. Delete Contact')
    print('5. Exit')
    choice=input('Enter your choice: ')
    
    if choice=='1':
        name=input('Enter your contact name: ')
        number=input('Enter your contact number: ')
        ContactBook.AddContact(name , number)
    elif choice=='2':
        ContactBook.ReadContact()
    elif choice=='3':
        ContactBook.UpdateContact()
    elif choice=='4':
        ContactBook.DeleteContact()
    elif choice=='5':
        print('Exit...')