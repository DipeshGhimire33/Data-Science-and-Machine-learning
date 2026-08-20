import uuid


def validate_email(func):
    """
    Validate email before function run
    """
    def inner(user_email:str):
        if user_email.endswith("@skill.com"):
            return func(user_email)
    
        return "Only support email from skillshikshya"

    return inner

@validate_email
def get_reset_code(email):
    return str(uuid.uuid1())[:8]

print(get_reset_code("John@skill.com"))
        