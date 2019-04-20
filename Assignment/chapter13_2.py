import urllib.request, urllib.parse, urllib.error
import json
 
sum,count = 0,0
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
results = json.loads(data)

lst = results["comments"]
#print(lst)
for item in lst:
    sum += item["count"]
    count+=1
    
print(count)
print(sum)