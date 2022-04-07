
def verify_email(email):
    if "@" not in email:
        return False 
    
    split_email = email.split("@")
    identifier = "".join(split_email[:-1])
    domain = split_email[-1]

    if len(identifier) < 1:
        return False 
    
    if "." not in domain:
        return False 

    split_domain = domain.split(".")
    for section in split_domain:
        if len(section) == 0:
            return False 

    return True 

def verify_phone(phone_number):
    phone_num = phone_number.replace("-", "")
    if len(phone_num) <10 or len(phone_num) > 10:
        return False 
    return phone_num


def get_contact_by_name(first_name, last_name, contacts):
    for contact in contacts:
        if contact['first_name'] == first_name and contact['last_name'] == last_name:
            return contact 

    return None 