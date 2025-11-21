import os
import json
#STUDENT INFORMATION SYSTEM 

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("[}x{]           STUDENT INFORMATION                   [}x{]")

studentrecords = {}

while True:
    print("SELECT FROM THE OPTIONS BELOW")
    print("ADD INFORNATION \t type 'a' ")
    print("SEARCH RECORDS \t type 's' ")
    print("MODIFY RECORDS \t type 'm' ")
    print("IMPORT RECORDS \t type 'i' ")
    print("DELETE RECORDS \t type 'd' ")
    print("EXIT PROGRAM \t type 'e' ")

    choice = input(" Select your choice     :: ").lower()

    if choice == 'a':
        os.system('cls')
        print("[}x{]           ADDING INFORMATION                   [}x{]")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        searchcode = input(" type the assigned student ID code for this student  ::")

        firstname = input(" type students FIRST NAME   ::").upper()
        lastname = input(" type students LAST NAME   ::").upper()
        course = input(" type your course here(abbreviation only)   ::").upper()
        section = input(" type your class section   ::").upper()

        studentrecords = {searchcode : [firstname, lastname, course, section]}
        print(".    .   .   .   .   DATA SAVED!   .   .   .   .   .")

        continue
    elif choice == 's' :
        os.system('cls')
        print("[}x{]          SEARCH STUDENT RECORD                   [}x{]")
        searchID = input(" Input your STUDENT ID to search  :: ")
        for id in studentrecords.keys():
            if searchID in studentrecords.keys():
                print(".    .   .   SEARCHING STUDENT RECORDS   .   .   .")
                print(".    .   .   STUDENT RECORD FOUND!   .   .   .")
                for i in studentrecords[searchID]:
                    print(f"-- {i}")
            else:
                print(".    .   .   SEARCHING STUDENT RECORDS   .   .   .")
                print(".    .   .   NO RECORD FOUND!   .   .   .")
        continue
    elif choice == 'm' :
        os.system('cls')
        print("[}x{]          MODIFY STUDENT RECORD                   [}x{]")
        searchID = input(" Input your STUDENT ID to search  :: ")
        for id in studentrecords.keys():
            if searchID in studentrecords.keys():
                print(".    .   .   SEARCHING STUDENT RECORDS   .   .   .")
                print(".    .   .   STUDENT RECORD FOUND!   .   .   .")
                for i in studentrecords[searchID]:
                    print(f"-- {i}")
                
                firstname = input(" type students FIRST NAME   ::").upper()
                lastname = input(" type students LAST NAME   ::").upper()
                course = input(" type your course here(abbreviation only)   ::").upper()
                section = input(" type your class section   ::").upper()

                studentrecords[searchID][0] = firstname
                studentrecords[searchID][1] = lastname
                studentrecords[searchID][2] = course
                studentrecords[searchID][3] = firstname

                print(".    .   .   DATA UPDATED!   .   .   .")
                print(studentrecords)
            else:
                print(".    .   .   SEARCHING STUDENT RECORDS   .   .   .")
                print(".    .   .   NO RECORD FOUND!   .   .   .")
    
        continue
    elif choice == 'i' :
        os.system('cls')
        print("IMPORT STUDENT RECORDS")

        with open('studentrecords.json','r') as newfile:
            studentjson = jsom.load(newfile)

        studentrecords = studentjson
        print(".    .   .   DATA RECORDS IMPORTED   .   .   .")

        continue

    elif choice == 'd' : 
        os.system('cls')
        print("[}x{]          DELETE STUDENT RECORD                   [}x{]")
        searchID = input(" Input your STUDENT ID to search  :: ")
        for id in studentrecords.keys():
            if searchID in studentrecords.keys():
                print(".    .   .   SEARCHING STUDENT RECORDS   .   .   .")
                print(".    .   .   STUDENT RECORD FOUND!   .   .   .")
                for i in studentrecords[searchID]:
                    print(f"-- {i}")
                studentrecords.pop(searchID)
                print(".    .   .   RECORDS DELETED!    .   .   .")
            else:
                print(".    .   .   SEARCHING STUDENT RECORDS   .   .   .")
                print(".    .   .   NO RECORD FOUND!   .   .   .")
        continue
    elif choice == 'e' :
        print ("-   -   -   RETRIEVING DATA -   -   -")
        print ("[}x{]           DATA EXIT                   [}x{]")
        break
    
