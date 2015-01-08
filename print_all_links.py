def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""

def get_next_target(s):
    start_link = s.find('<a href=')
    if start_link == -1:
       return None,0
    else:
        start_quote = s.find('"', start_link+1)
        end_quote = s.find('"',start_quote+1)
        url = s[start_quote+1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print url
            page = page[endpos:]
        else:
            break

