class SearcherByName:

    def __init__(self, user_input, optional=None, year="0000"):
        self.user_input = user_input
        self.year = year
        self.split_user_input = self.user_input.split(" ")
        
        if optional != None:
            self.optional = optional.split(" ")
        else
            self.optional = []
            
        #temp variables for generating
        self.mutate_variants_of_name = []
        
