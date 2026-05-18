class SearcherByName:

    def __init__(self, user_input, optional=None, year="0000"):
        self.user_input = user_input
        self.year = year
        splited_user_input = self.user_input.lower().split()
