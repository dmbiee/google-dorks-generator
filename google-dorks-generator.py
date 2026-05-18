import urllib.parse

from CONSTANTS import *




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

def name_controller(user_input : str):

    splited_user_input = user_input.split(" ")
    list_of_variants_for_name = []
    
    separators = [
        " ",
        ".",
        ", ",
        "_",
        "",]
    
    for separator in separators:
        list_of_variants_for_name.append(f'"{separator.join(splited_user_input)}"')
    
    for i in splited_user_input:
        list_of_variants_for_name.append(f'"{i}"')

    #---manual append---
    if len(splited_user_input) >= 2:
        list_of_variants_for_name.append(f"{splited_user_input[0][0]} {splited_user_input[1]}") # "J Smit"
        list_of_variants_for_name.append(f"{splited_user_input[0]} {splited_user_input[1][0]}") # "John S"
        list_of_variants_for_name.append(f'"{splited_user_input[0]} {splited_user_input[1]}" {SOCIAL_NETWORKS}')
        list_of_variants_for_name.append(f'"{splited_user_input[0]} {splited_user_input[1]}" {FILE_TYPES}')


    general_search_service(list_of_variants_for_name)

def general_search_service(list_to_search):
    
    for i in list_to_search:
        for key, link in GENERAL_SEARCH_LINKS_TEMPLATE.items():
            print(f"{key} for {i} -> {link.replace("|REPLACE|", urllib.parse.quote(i))}")


def main():
    #name_controller(user_input)
    email_name_generator(user_input)




if __name__ == "__main__":
    main()