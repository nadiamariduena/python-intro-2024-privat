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

#
# ----- ACCESSing the data ---
# band ={

# "vocals": "Plant",
# "guitar": "Page"

# }
print(band["vocals"])
print(band.get("guitar"))
#result:
# i get plant and page, because these are the values that are aligned to the dictionary in line 27
# Plant
# Page


#
#
# ----- print all keys ---

print(band.keys())
# result: dict_keys(['vocals', 'guitar'])
#
#
# ----- print all keys ---

print(band.values())
#result
#dict_values(['Plant', 'Page'])

# -------- ALL
#list of key/value pairs as tuples
# print(band.items())
#dict_items([('vocals', 'Plant'), ('guitar', 'Page')])

#
# band ={

# "vocals": "Plant",
# "guitar": "Page"

# }
# --- modifying
# band["vocals"] = "Coverdale"
# band.update({"bass": "JPJ"})
# print(band)
# result: {'vocals': 'Coverdale', 'guitar': 'Page', 'bass': 'JPJ'}
# see all
# print(band.items())
#result
#dict_items([('vocals', 'Coverdale'), ('guitar', 'Page'), ('bass', 'JPJ')])

#---------------------------
# 🟡 remove the last item
#---------------------------
# - removes the last item added to a dictionnary
# 1 for that i will add a new item. the below is before i add the new item:
# dict_values(['Plant', 'Page'])
# ('guitar', 'Page')
#- add a new item
band["glow"] = "flower"
print(band)
# 2 result, after i added the new item:
# dict_values(['Plant', 'Page'])
# {'vocals': 'Plant', 'guitar': 'Page', 'glow': 'flower'}
# 3 now remove the last item added
print(band.popitem())
# 4 result, here you can see that the glow flower are outside the square brackets
# {'vocals': 'Plant', 'guitar': 'Page', 'glow': 'flower'}
# ('glow', 'flower')
#---------------------

#
#
# ---- deleting
# 1 create a new item
band["drums"] = "Bonita"
#result: {'vocals': 'Plant', 'guitar': 'Page', 'drums': 'Bonita'}
# 2 delete the new item
del band["drums"]
#result after deleting
# {'vocals': 'Plant', 'guitar': 'Page'}
print(band)
#
#------ CLEAR

# 1. for this example, i will use the other dictionary i have at the top

# band2 = dict(
# vocals="Plant",
# guitar="Page"
# )