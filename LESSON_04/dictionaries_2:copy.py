#dictio 1
member1 = {
    'name': 'Robert Plant',
    'instrument': 'vocals'
}
#---------
#dictio 2
member2 = {
    'name': 'Jimmy Page',
    'instrument': 'guitar'
}
#---------
#dictio 3
# here we will nest the 2 dictios from above
band = {
    "member1": member1,
    "member2": member2
}
#
# show the content
print(band)
#