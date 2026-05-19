import urllib.parse

from CONSTANTS import *


class SearcherByName:

    def __init__(self, user_input, optional=None, year="0000"):
        # inputs
        self.user_input = user_input
        self.year = year        
        self.optional = optional.split() if optional else []
        
        # raw data
        self.split_user_input = self.user_input.split()

        
        # pipeline vars 
        self.mutate_variants_of_name = []
        self.search_prompts = []
        self.result_data = []
        
        # pipeline vars for email generator
        self.mutate_variants_of_name_for_email = []
        self.result_generate_emails = []

#-----------START-NAME-SEARCH-PROMPT----------

    











    def _manual_append_mutate(self):
        
        if len(self.split_user_input) >= 2:
            
            first = self.split_user_input[0]
            last = self.split_user_input[1]
            
            self.mutate_variants_of_name.append(f"{first[0]} {last}") # "J Smit"
            self.mutate_variants_of_name.append(f"{first} {last[0]}") # "John S"
            
            # special_search_prompts(SOCIAL_NETWORKS and FILE_TYPES)
            self.special_search_prompts.append(f'"{first} {last}" {SOCIAL_NETWORKS}')
            self.special_search_prompts.append(f'"{first} {last}" {FILE_TYPES}')
    
    def _automate_append_mutate(self):
        
        for separator in SEPARATORS:
            self.mutate_variants_of_name.append(f'"{separator.join(self.split_user_input)}"')
    
        for i in self.split_user_input:
            self.mutate_variants_of_name.append(f'"{i}"')
            
    def _result_line_generator(self):
    
        for search_prompt in self.mutate_variants_of_name:
            for service, link in GENERAL_SEARCH_LINKS_TEMPLATE.items():
                self.result_generate_links.append(f"{service} for {search_prompt} -> {link.replace("|REPLACE|", urllib.parse.quote(search_prompt))}")
                self.result_generate_links.append(f"{service} for {search_prompt} + optional -> {link.replace("|REPLACE|", urllib.parse.quote(search_prompt+" ".join(self.optional)))}")

                
        for search_prompt in self.special_search_prompts:
            for service, link in GENERAL_SEARCH_LINKS_TEMPLATE.items():
                self.result_generate_links.append(f"{service} for {self.user_input} -> {link.replace("|REPLACE|", urllib.parse.quote(search_prompt))}")
        
#-----------END-NAME-SEARCH-PROMPT----------

#-----------START-EMAIL-GENERATOR----------

