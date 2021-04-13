# Write a function that when given a URL as a string, 、
#   parses out just the domain name and returns it as a string.
# For example:
#
# domain_name("http://github.com/carbonfive/raygun") == "github"
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"
from urllib.parse import urlparse
# import publicsuffix2
import re

def domain_name(url: str):
    tld_list = ['com', 'net', 'co', 'ru']
    if re.match(r'((http://)|(https://)).*', url) is None:
        url_http = 'http://{}'.format(url)
    else:
        url_http = url
    url_words = urlparse(url_http).hostname.split('.')
    for i in range(len(url_words)):
        if url_words[i] in tld_list:
            return url_words[i-1]

    # print(hostname, type(hostname), tld, type(tld))
    # hostname.replace('.{}'.format(tld), '')
    # return publicsuffix2.get_sld(hostname.replace('.{}'.format(tld), ''))


print(domain_name("http://google.com"),"google")
print(domain_name("http://google.co.jp"), "google")
print(domain_name("www.xakep.ru"), "xakep")
print(domain_name("https://youtube.com"), "youtube")
