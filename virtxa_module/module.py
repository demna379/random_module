import webbrowser

def move_zeros(lst):
    lstn = []
    lstf = []

    for i in lst:
        if i == 0 and type(i) is int:
            lstn.append(i)
        else:
            lstf.append(i)
    
    return lstf + lstn

def pig_it(text):
    lstn = []
    for i in text.split():
        if i.isalpha():
            lstn.append(i[1:] + i[0] + "ay")
        else:
            lstn.append(i)  
    return ' '.join(lstn)

def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02}:{minutes:02}:{secs:02}"

def generate_hashtag(s):
    if not s:
        return False
    lstn = []
    for i in s.split():
        lstn.append(i.capitalize())
    random = '#' + ''.join(lstn)
    if len(random) > 140:
        return False
    else:
        return random
    
def domain_name(url):
    if url[0:7] == "http://":
        url = url[7:]
    elif url[0:8] == 'https://':
        url = url[8:]
    
    if url[:4] == "www.":
        url = url[4:]
    
    return url.split(".")[0]

def first_non_repeating_letter(s):
    for i in s:
        if s.lower().count(i.lower()) == 1:
            return i
    return ''

def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

def solution(number):
    if number < 1:
        return 0
    lstn = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            lstn.append(i)
    return sum(lstn)

def likes(names):
    if not names:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names[2:])} others like this'

def important():
    return webbrowser.open('https://youtu.be/xvFZjo5PgG0')

def virtxa_deme():
    return webbrowser.open('https://www.facebook.com/people/Demna-Maisuradze/pfbid0GH2qHUBRCEE2aJzTHkYFkXoSWP75dEY6uKretUYshtms7RWnPH3EjTcBJ7Gvn67hl/#')