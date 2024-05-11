# version 1
band ={

"vocals": "Plant",
"guitar": "Page"

}
print(band)
#result: {'vocals': 'Plant', 'guitar': 'Page'}
#
# version 2

band2 = dict(
vocals="Plant",
guitar="Page"
)

print(band2)
#result: {'vocals': 'Plant', 'guitar': 'Page'}
print(type(band))
#result: <class 'dict'>
print(len(band))
#result: 2