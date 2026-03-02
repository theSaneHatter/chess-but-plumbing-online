print(__name__ + " has been imported!")
import random
import time 

def gen_gid(messages):
    lowest = 0
    gid = f"gid{0}"
    while gid in messages:
        lowest +=1
        gid = f"gid{lowest}"
    print(f"@backend:gen_gid():genorated new gid:>{gid}<")
    return gid
        

    
