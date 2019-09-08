from datetime import datetime



def all_isupper(text):
    return all([w.isupper() for w in text.split()])

def is_date(text, format='%d/%m/%y'):
    try:
        datetime.strptime(text, format)
        return True
    except ValueError:
        return False

def today():
    return datetime.now().strftime("%m-%d-%Y")