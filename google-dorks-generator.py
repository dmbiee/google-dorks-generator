from searcher_by_name import SearcherByName
import TEXT as t

#user_input = "Hugo Diaz Iglesias"

def generate_by_name():
    
    print("Running: generate by name...\n")
    name = input("First name (required): ")
    extra_info = input("Additional info (city, nickname, workplace, etc.): ")
    birth_year = input("Birth year (YYYY): ")
    print("\n Generate...\n")
    
    s = SearcherByName(user_input=name,optional=extra_info,year=birth_year)
    
    for data in s.get_data():
       print(f'-> {data["prompt"]}\nService {data["service"]} -> {data["url"]}\n')
    
    for email in s.get_email_data():
        print(email)
 
 
def search_by_photo():
    print(t.SEARCH_IMAGE)


ROUTES = {
    "1": generate_by_name,
    "2": lambda: print("(in development)"),
    "3": lambda: print("(in development)"),
    "4": search_by_photo,
}

def route(choice: str):
    handler = ROUTES.get(choice)

    if handler:
        handler()
    else:
        print("Invalid option")


def main():
    print(t.LOGO)
    print(t.AUTOR)
    
    print(t.MAIN_MENU)
    choice = input("Select what you want to do (1-4):")
    
    route(choice)
    
    
if __name__ == "__main__":
    main()