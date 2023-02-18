import database

def contacts():
    while True:
        print('1. Show Contacts')
        print('2. New Conact')
        print('3. Delete Contact')
        print('4. Exit')

        num = int(input())
        
        if num==1:
            database.Show_contacts()
            
        elif num==2:
            first_name = str(input('Enter first name:'))
            last_name = str(input('Enter last name:'))
            phone_no = str(input('Enter phone no:'))
            print()
            database.add_contact(first_name, last_name, phone_no)
        elif num==3:  
            database.Show_contacts()
            delete_id=str(input('Enter your deleting id:'))   
            database.Delete_contact(delete_id)
            print('\t 1 contact deleted from your contacts')
            print()
            
        else:
            return False

if __name__=='__main__':
    contacts()