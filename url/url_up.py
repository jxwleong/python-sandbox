import urllib.request


# https://stackoverflow.com/a/1949360
def is_url_up(url: str):
    return urllib.request.urlopen(url).getcode()


print(is_url_up("https://google.com"))