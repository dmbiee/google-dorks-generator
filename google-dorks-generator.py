import urllib.parse


SOCIAL_NETWORKS = " site:twitter.com OR site:facebook.com OR site:instagram.com OR site:tiktok.com OR site:youtube.com OR site:linkedin.com "
FILE_TYPES = " filetype:pdf OR filetype:doc OR filetype:docx "
GENERAL_SEARCH_LINKS_TEMPLATE = {
    "google_web" : "https://www.google.com/search?q=|PROMPT|",
    "googele_img":"https://www.google.com/search?q=|PROMPT|&udm=2",
    "bing_web":"https://www.bing.com/search?q=|PROMPT|",
    "bing_img":"https://www.bing.com/images/search?q=|PROMPT|&first=1",
    "yahoo":"https://search.yahoo.com/search?p=|PROMPT|",
    "yandex":"https://yandex.com/search/?text=|PROMPT|",
    "webmii":"https://webmii.com/people?n=|PROMPT|",
}

EMAIL_DOMAINS = [
    "@gmail.com",
    "@hotmail.com",
    "@hotmail.es",
    "@outlook.com",
    "@outlook.es",
    "@live.com",
    "@live.es",
    "@msn.com",
    "@yahoo.com",
    "@yahoo.es",
    "@icloud.com",
    "@me.com",
    "@protonmail.com",
    "@gmx.com",
    "@gmx.es",
    "@terra.es",
    "@terra.com",
    "@orange.es",
    "@telefonica.net",
    "@movistar.es",
    "@jazztel.es",
    "@euskalnet.net",
    "@ono.com",
    "@mail.com",
    "@aol.com  ",
]

USERNAME_MASK = [
    "|USERNAME|",
    "|USERNAME|1",
    "|USERNAME|123",
    "_|USERNAME|",
    "__|USERNAME|",
    "_|USERNAME|_",
    "|USERNAME|_",
    "|USERNAME|__",
    "0|USERNAME|",
    ".|USERNAME|",
    "|USERNAME|.",
    ".|USERNAME|."]

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
            print(f"{key} for {i} -> {link.replace("|PROMPT|", urllib.parse.quote(i))}")


def main():
    #name_controller(user_input)
    email_name_generator(user_input)




if __name__ == "__main__":
    main()