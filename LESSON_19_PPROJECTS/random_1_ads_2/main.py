from helper import fashion_ads


#step 1
def display_fashion_list(ad):


    print(f" Display Text:  {ad['text']}")
    print(f" Display Image:  {ad['image']}")

    print("__________")


# step 2
def main_loop():

    #3
    # show 3 items from the list on the helper.py (i have actually 4 items)
    for x in range(3):

        #4 assign the 'a' var to the list of items 'fashion_ads' coming from the helper.py
        a = fashion_ads()

        # 5 use the 'A' which is carrying the list of items 'fashion_ads' coming from the helper.py
        # display the function in step1, add the param 'a' from step 4) which is carrying the list of items 'fashion_ads' coming from the helper.py
        display_fashion_list(a)




if __name__ == "__main__":

    main_loop()

# ------ output ------------
# lucizor@lucibellsan:~/Documents/0_PYTHON-all/PYTHON-PRIVAT/python-intro-2024-privat/LESSON_19_PPROJECTS/random_1_ads_2$ python main.py
#  Display Text:  🌻 Discover our Summer Collection!
#  Display Image:  image1.jpg
# __________
#  Display Text:  🌻 Discover our Summer Collection!
#  Display Image:  image1.jpg
# __________
#  Display Text:  🩷 Explore the Latest Trends in Fashion!
#  Display Image:  image2.jpg