from searcher_by_name import SearcherByName


user_input = "Modesto Alvarez"
email_year = "2002"

def main():
    
    s = SearcherByName(user_input=user_input,optional="Asturias",year=email_year)
    for data in s.get_data():
       print(f'-> {data["prompt"]}\nService {data["service"]} -> {data["url"]}\n')
    
    for email in s.get_email_data():
        print(email)


if __name__ == "__main__":
    main()