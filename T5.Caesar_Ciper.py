""" This code is a codification/decodification program"""
""" In code ASCII, all characters have a specifical number. The lower letters is between 97 - 122"""

user_text = str(input("Introduceti textul dorit: ")).lower()
user_choice = input("Doriti ca textul dumneavoastra sa fie codificat/decodificat?: ").lower()
lista = ""
i = 0
if user_choice == "codificat":
     step_convert = int(input("Introduceti pasul cu cat doriti sa fie codificat textul: "))
     while i < len(user_text):
          if user_text[i] == " ":
               lista += " "
          elif (ord(user_text[i]) + step_convert) <= 122 :
               lista = lista + chr(ord(user_text[i]) + step_convert)
          elif step_convert > 26:
               new_step_convert = step_convert % 26
               if (ord(user_text[i]) + new_step_convert) <= 122:
                    lista = lista + chr(ord(user_text[i]) + new_step_convert)
               else :
                    lista = lista + chr(ord(user_text[i]) + new_step_convert - 26)
          else :
               lista = lista + chr(ord(user_text[i]) + step_convert - 26)
          i += 1
     print(lista)
elif user_choice == "decodificat":
     step_convert = int(input("Introduceti pasul cu cat doriti sa fie decodificat textul: "))
     while i < len(user_text):
          if user_text[i] == " ":
               lista += " "
          elif (ord(user_text[i]) - step_convert) >= 97 :
               lista = lista + chr(ord(user_text[i]) - step_convert)
          elif step_convert > 26 :
               new_step_convert = step_convert % 26
               if (ord(user_text[i]) - new_step_convert) >= 97:
                    lista = lista + chr(ord(user_text[i]) - new_step_convert)
               else :
                    lista = lista + chr(ord(user_text[i]) - new_step_convert + 26)
          else :
               lista = lista + chr(ord(user_text[i]) - step_convert + 26)
          i += 1
     print(lista)
else :
     print("Verificati alegerea dumneavoastra!")

