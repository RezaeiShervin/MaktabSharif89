class DuplicateUsernameError(Exception):
    '''Raise when there is a duplicate username'''
    # def __init__(self, message, errors=None):
    #     super(DuplicateUsernameError, self).__init__(message)
    #     self.errors = errors
    pass

class SpecialCharError(Exception):
    def __init__(self, message=None):
        self.message = message
        self.special = ('#', '@', '&', '?', '!', '*', '$')
    def __str__(self):
        return f"Must contain special charachters: {self.special}"

