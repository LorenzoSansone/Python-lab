import re
#GOAL: 
# 1)user prompt an URL of the twitter profile
# 2)extract the user's username

#BASE VERSION: fragile version
#INPUT: https://twitter.com/davidjmalan -> OUTPUT: davidjmalan
#problems: what if the url has "http" insteand of "https", additional parameter, www?, ecc.
"""
url = input("URL: ").strip()

username = url.replace("https://twitter.com/","")
print(f"Username: {username}")
"""

#SECOND VERSION: regex using re.sub -> useful for cleaning up data and get rid of something we don't want there
#http and https are tolerated
#www. is optional
#https?:// is optional
#PROBLEM: we need re.search cause it tells us if the input has a url from twitter or not. re.sub is useful for cleaning
#up data (not for conditional)
"""
url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url) #
print(f"Username: {username}")
"""

#THIRD VERSION:  regex using re.search
"""
url = input("URL: ").strip()
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2)) #because the username group '(.+)' is the second group of parenthesis (the first one is (www\.))
"""

#FOURTH VERSION:  regex using re.search and non-capturing parenthesis (?:)
#([a-z0-9_]+) represents the character allowed by twitter for username
#I removed the $ because the url can have other information after the username.
url = input("URL: ").strip()
matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1)) #because we used non-capturing parenthesis so the first one now is ([a-z0-9_]+). We don't need to capture (www\.)
