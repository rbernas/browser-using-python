import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL:')
print "Retrieving" + url
results = []
count = 0

uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
for item in lst:
	count += 1
	x = float(item.find('count').text)
	results.append(x)

print "Count:", count
print "Sum: ", sum(results)


