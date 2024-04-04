class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged_in: function(args[0])
        else: print('user is not logged in')
    return wrapper


@is_authenticated
def create_blog_post(user): 
    if type(user) == User: print(f"This is {user.name}'s new blog post.")


new_user = User("angela")
# new_user.is_logged_in = True
create_blog_post(new_user)