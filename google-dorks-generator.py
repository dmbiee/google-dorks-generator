import urllib.parse


SOCIAL_NETWORKS = " site:twitter.com OR site:facebook.com OR site:instagram.com OR site:tiktok.com OR site:youtube.com OR site:linkedin.com "
FILE_TYPES = " filetype:pdf OR filetype:doc OR filetype:docx "
GENERAL_SEARCH_LINKS_TEMPLATE =[
    "https://www.google.com/search?q=|PROMPT|",
    "https://www.google.com/search?q=|PROMPT|&udm=2",
    "https://www.bing.com/search?q=|PROMPT|",
    "https://www.bing.com/images/search?q=|PROMPT|&first=1",
    "https://search.yahoo.com/search?p=|PROMPT|",
    "https://yandex.com/search/?text=|PROMPT|",
    "https://webmii.com/people?n=|PROMPT|",
]


user_input = input("Name of target: ")

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
        for link in GENERAL_SEARCH_LINKS_TEMPLATE:
            print(link.replace("|PROMPT|", urllib.parse.quote(i)))


def main():
    name_controller(user_input)

if __name__ == "__main__":
    main()