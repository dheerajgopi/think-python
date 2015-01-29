import urllib

zipcode = raw_input('pls enter the zip code   ---   ')

url = 'http://www.uszip.com/'+ zipcode

conn = urllib.urlopen(url)

for line in conn:
    if 'Population' in line:
        print line 
