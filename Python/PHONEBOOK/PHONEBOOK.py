#/****************************************************************************/
#/****************************************************************************/
#/**************************		Author: SAHER GHANEM 	   *********************/
#/**************************		   ITI-INTAKE43          *********************/
#/**************************		    PHONEBOOK		         *********************/
#/**************************		   Version:1.00 	       *********************/
#/**************************		DATE: 12/25/2022       	 *********************/
#/****************************************************************************/
#/****************************************************************************/

import os
import re   

def main():
  phoneBook = None 
  contact = {}     
  
  while True :
    choice = int(input(''' 
                           ****** The_PHONEBOOK ******
                           ****** Author: Saher Ghanem *******
                           1. Create Phone book \n 
                           2. Add New Contact \n 
                           3. Modify Contact \n 
                           4. Display Contact \n 
                           5. Search Contact \n 
                           6. Delete Contact \n 
                           7. Delete Phone Book \n 
                           8. Exit \n 
                           Please Enter Your Choice : '''))
    # Adding a new PhoneBook
    if choice  == 1 :
      if phoneBook == None :
        phoneBook = {}
        print("  ")
        print("            PhoneBook is Created          ")
        print("  ")
      else :
        print("  ")
        print("This PhoneBook Already Exists!")
        print("  ")
############################################################################################



    # Adding a new Contact
    elif choice == 2 :
      if phoneBook == None :
        print("  ")
        print("            NO PHONEBOOK!            ")
        print("  ")
      else :
        print("  ")
        print("************_Add_Contact_************")
        print("  ")
        # Entering DATA
        name       = input("Please Enter the Name:  (The First Char is Upper Cased) :")
        gender     = input("Please Enter the Gender (The First Char is Upper Cased) :")
        phone_num  = input("Please Enter the Phone number :")
        email      = input("Please Enter the Email :")
      
        # Checking the Egyptian Number's Validity , Email Address , Name & Gender [REGEX]
        correct_name        = re.search(r'[A-z]+',name)
        correct_gender      = re.search(r'[F,M]+\w+',gender)
        correct_phone_num   = re.search(r'[0][1][0 1 2]\d{8}',phone_num)
        correct_email_add   = re.search(r'[a-z\d.-]+@+[\w.]+',email)
        
        # if any one of them return None print wrong entry
        if correct_phone_num == None or correct_email_add == None or correct_name == None or correct_gender == None:
          print("            Wrong Entry!, Please Enter a Valid one!")
      
        else :
          if phone_num not in contact :
            contact[phone_num] = {'Gender :':gender,'Name :':name,'Email :':email}
            print('            Added Successfully')
      
          else :
            print('            This Contact Already Exists!')
############################################################################################




    # Editing a Contact
    elif choice == 3 :
      if phoneBook == None :
        print("            NO PHONEBOOK!")
      
      else :
        print("  ")
        print("************EDIT_CONTACT************")
        print("  ")
        phone_num = input("            Enter the contact's number to be edited : ")
      
        if phone_num in contact :          
          for i in contact.keys():
            if i == phone_num :
              name = input("            Enter new name : ")
              gender = input("            Enter new Gender : ")
              email = input("            Enter new email : ")
      
              # Checking the Egyptian Number's Validity , Email Address , Name & Gender [REGEX]
              correct_phone_num = re.search(r'[0][1][0 1 2]\d{8}',phone_num)
              correct_email_add = re.search(r'[a-z\d.-]+@+[\w.]+',email)
              correct_name      = re.search(r'[A-z]+',name)
              correct_gender      = re.search(r'[F,M]+\w+',gender)
      
              if correct_phone_num == None or correct_email_add == None or correct_name == None or correct_gender == None:
                print("  ")
                print("            Wrong Entry!, Please Enter a Valid one!")
                print("  ")
      
      
              else : 
                contact[phone_num] = {'Gender :':gender,'Name :':name,'Email :':email}
                print("  ")
                print("            Contact Updated !")
                print("  ")
      
        else :
          print("  ")
          print("            Contact is not found in Phone Book")
          print("  ")
############################################################################################




    # Displaying a Contact
    elif choice == 4 :
      if phoneBook == None :
        print("  ")
        print("            NO PHONEBOOK!")
        print("  ")
      else :
        if contact == {} :
          print("  ")
          print("            Empty")
          print("  ")
        else :
          for a in contact.items() :
            print("  ")
            print("            Contact is :",a)
            print("  ")
############################################################################################




    # Searching for a contact
    elif choice == 5 :
      if phoneBook == None :
        print("  ")
        print("            NO PHONEBOOK!")
        print("  ")
      else :
        search_num = input("            Enter his/her Contact Number : ")
        if search_num in contact :
          print("  ")
          print ("            FOUND") 
          print("  ")
        else :
          print("  ")
          print("            Contact is not Found!") 
          print("  ")
############################################################################################



  
    # Deleting a contact
    elif choice == 6 :
      if phoneBook == None :
        print("  ")
        print("            Contact is not Found!")
        print("  ")
      else :
        delete_contact = input("            Enter his/her Contact Number : ")
    
        if delete_contact in contact :
          confirmation = input("            Are you sure you want to delete this contact? - 'Y/N' \n")
    
          if confirmation == 'Y' or confirmation == 'y':
            del contact [delete_contact]
            print("  ")
            print ("            Contact Deleted!")
            print("  ")
          else : 
            print("  ")
            print("            Contact not deleted")
            print("  ")
        else :
          print("  ")
          print("            Contact not found!")
          print("  ")
############################################################################################




    # Deleting the phone book
    elif choice == 7:
      if phoneBook == None :
        print("  ")
        print("            NO PHONEBOOK TO DELETE!") 
        print("  ")
      else :
        del phoneBook
        print("  ")
        print("            PHONEBOOK DELETED")
        print("  ")
############################################################################################





    # Exit
    elif choice == 8:
      break
  else :
    print("  ")
    print("            Not Valid Entry,Please Try Again")
    print("  ")
if __name__=='__main__':
  main()