import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter location: ')
if len(url) < 1: quit()
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved',len(data), 'characters')
tree = ET.fromstring(data)
results = tree.findall('comments/comment')
sum = 0 
count = 0
for item in results:
    sum += int(item.find('count').text)
    count += 1
print('Count: ',count)        
print('Sum', sum)