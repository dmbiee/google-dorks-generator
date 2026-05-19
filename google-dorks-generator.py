import urllib.parse

from CONSTANTS import *
from searcher_by_name import SearcherByName




#user_input = input("Name of target: ")

user_input = "Modesto Alvarez"
email_year = "2002"

def email_name_generator(user_input : str):
    splited_user_input = user_input.lower().split()
    result = []

    #---manual---
    result.append(f"{splited_user_input[0][0]}{splited_user_input[1]}") # "jsmit"
    result.append(f"{splited_user_input[0]}{splited_user_input[1][0]}") # "johns"
    result.append(f"{splited_user_input[0][0]}{splited_user_input[1][0]}") # "js"
    result.append("".join(splited_user_input))
    result.append(".".join(splited_user_input))

    result.append("".join(splited_user_input)+email_year)
    result.append(".".join(splited_user_input)+email_year[2:])

    email_with_domain_generator(result)

def email_with_domain_generator(list_of_optiones):

    for i in list_of_optiones:
        for domain in EMAIL_DOMAINS:
            print(i+domain)

def main():
    #email_name_generator(user_input)
    
    s = SearcherByName(user_input=user_input,optional="Asturias",year=email_year)
    for data in s.get_data():
        print(f'-> {data["prompt"]}\nService {data["service"]} -> {data["url"]}\n')


if __name__ == "__main__":
    main()