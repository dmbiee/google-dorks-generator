import urllib.parse

from CONSTANTS import (
    SEPARATORS,
    SOCIAL_NETWORKS,
    FILE_TYPES,
    GENERAL_SEARCH_LINKS_TEMPLATE,
    EMAIL_DOMAINS,
)

class SearcherByName:

    def __init__(self, user_input, optional=None, year="0000"):
        # inputs
        self.user_input = user_input
        self.year = year        
        self.optional = optional.split() if optional else []
        
        # raw data
        self.split_user_input = self.user_input.split()
        self.splited_user_input_lower = self.user_input.lower().split()

        
        # pipeline vars 
        self.mutate_variants_of_name = []
        self.search_prompts = []
        self.result_data = []
        
        # pipeline vars for email generator
        self.mutate_variants_of_name_for_email = []
        self.result_generate_emails = []

        # RUN
        self._run()

#-----------PIPELINE-NAME-SEARCH----------

    def _run(self):
        (
            self._generate_name_variants()
                ._generate_search_prompts()
                ._build_links()
        )
        (
            self._generate_email_variants()
                ._build_emails()
        )
        return self

#-----------STAGE-1----------

    def _generate_name_variants(self):

        (
        self._manual_append_mutate()
            ._automate_append_mutate()
           )
        return self
    
    def _manual_append_mutate(self):
        
        if len(self.split_user_input) >= 2:
            
            first = self.split_user_input[0]
            last = self.split_user_input[1]
            
            self.mutate_variants_of_name.append(f"{first[0]} {last}") # "J Smit"
            self.mutate_variants_of_name.append(f"{first} {last[0]}") # "John S"

        return self
            
    def _automate_append_mutate(self):
        
        for separator in SEPARATORS:
            self.mutate_variants_of_name.append(f'{separator.join(self.split_user_input)}')
    
        for i in self.split_user_input:
            self.mutate_variants_of_name.append(f'{i}')
        
        return self
            
#-----------STAGE-2----------
            
    def _generate_search_prompts(self):

        for prompt in self.mutate_variants_of_name:
            self.search_prompts.append(f'"{prompt}" '+ f'"{" ".join(self.optional)}"')

        # special_search_prompts(SOCIAL_NETWORKS and FILE_TYPES)
        self.search_prompts.append(f'"{" ".join(self.split_user_input)}" {SOCIAL_NETWORKS}')
        self.search_prompts.append(f'"{" ".join(self.split_user_input)}" {FILE_TYPES}')

        return self

#-----------STAGE-3----------

    def _build_links(self):

        optional_text = " ".join(self.optional)

        for search_prompt in self.search_prompts:
            for service, link in GENERAL_SEARCH_LINKS_TEMPLATE.items():
                
                final_url =link.replace("|REPLACE|", urllib.parse.quote(search_prompt))

                self.result_data.append({
                    "prompt": search_prompt,
                    "service": service,
                    "url": final_url,
                    "optional": optional_text
                })
        
        return self

#-----------OPEN-METHODS-----------

    def get_data(self) -> list:
        """Data is a list of dicts
            Dict syntax:
        "prompt": STRING, 
        "service": STRING, 
        "url": STRING, 
        "optional": STRING
        """
        return self.result_data

#-----------END-PIPELINE-NAME-SEARCH----------




#-----------PIPELINE-EMAIL-GENERATOR-BY-NAME----------

#-----------STAGE-1----------
    def _generate_email_variants(self):

        email_separators = ["", ".", "-", "_"]

        

        #---automatic---
        for separator in email_separators:
            self.mutate_variants_of_name_for_email.append(separator.join(self.splited_user_input_lower)) #johnsmit
            self.mutate_variants_of_name_for_email.append(separator.join(self.splited_user_input_lower)+self.year) #johnsmit1234
            self.mutate_variants_of_name_for_email.append(separator.join(self.splited_user_input_lower)+self.year[2:]) #johnsmit34

        #---manual---
        self.mutate_variants_of_name_for_email.append(f"{self.splited_user_input_lower[0][0]}{self.splited_user_input_lower[1]}") # "jsmit"
        self.mutate_variants_of_name_for_email.append(f"{self.splited_user_input_lower[0]}{self.splited_user_input_lower[1][0]}") # "johns"
        self.mutate_variants_of_name_for_email.append(f"{self.splited_user_input_lower[0][0]}{self.splited_user_input_lower[1][0]}") # "js"

        return self

#-----------STAGE-2----------
    def _build_emails(self):

        for local_path in self.mutate_variants_of_name_for_email:
            for domain_path in EMAIL_DOMAINS:
                self.result_generate_emails.append(local_path+domain_path)
        return self

#-----------OPEN-METHODS-----------

    def get_email_data(self) -> list:
        return self.result_generate_emails