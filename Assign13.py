"""# create a python list
mylist=["apple","banana","kiwi"]
print(mylist)

# list lenth
list=[1,2,3,5,6]
print(len(list))


# type
my_list=[1,2,3,5]
print(type(my_list))

my_list1=list((1,2,3,4))
print(my_list1)
print(type(my_list1))

# how to access the list
l1=[1,2,3,4,5,6,7]
print(l1[0])
print(l1[-1])
"""

# Positive Indexing:  0   1   2   3   4   5   6   7
#                     1   2   3   4   5   6   7   8
# Negative Indexing: -8  -7  -6  -5  -4  -3  -2  -1

mylist = [1,2,3,4,5,6,7,8]
print(mylist[2:5])

# 👉 Syntax: list[start:end:step]
# - start: कहाँ से शुरू करना है
# - end: कहाँ तक जाना है (end exclusive = end वाला element शामिल नहीं होगा)
# - step: कितने index पर jump करना है (default = 1)

# अब देखें: mylist[2:5]
# - start = 2 → यानी index 2 से शुरू होगा
# - end = 5   → यानी index 5 तक जाएगा, लेकिन index 5 वाला element शामिल ❌ नहीं होगा
# - step default = 1 → यानी एक-एक करके elements लेंगे

# Index-wise देखें:
# index 2 -> 3 ✅ (start)
# index 3 -> 4 ✅
# index 4 -> 5 ✅
# index 5 -> 6 ❌ (end exclusive, इसलिए नहीं आएगा)

# इसलिए final output होगा: [3, 4, 5]



mylist = [1,2,3,4,5,6,7,8,9]
print(mylist[:4])

# 👉 Slicing का syntax है: list[start:end:step]
# - start: कहाँ से शुरू करना है (default = 0)
# - end: कहाँ तक जाना है (लेकिन यह index exclusive होता है, यानी उस index का element शामिल नहीं होगा)
# - step: कितने- कितने index पर jump करना है (default = 1)

# यहाँ हमने लिखा है mylist[:4]
# - start खाली है → इसका मतलब है कि slicing index 0 से शुरू होगी
# - end = 4 → यानी index 4 तक जाएगा लेकिन index 4 वाला element शामिल नहीं होगा
# - step default = 1 → एक-एक करके elements लेंगे

# Index-wise elements देखें:
# index 0 -> 1
# index 1 -> 2
# index 2 -> 3
# index 3 -> 4
# index 4 -> 5 (❌ शामिल नहीं होगा, क्योंकि end exclusive है)

# तो final output होगा: [1, 2, 3, 4]



thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# 👉 Slicing का syntax होता है: list[start:end:step]
# - start: कहाँ से शुरू करना है (default = 0)
# - end: कहाँ तक जाना है (लेकिन यह index शामिल नहीं होता, exclusive होता है)
# - step: कितने- कितने index पर jump करना है (default = 1)

# यहाँ हम लिख रहे हैं thislist[2:]
# - start = 2 (यानि index 2 से शुरू होगा)
# - end = खाली छोड़ा है, तो यह list के आखिरी element (index 6) तक जाएगा
# - step = default 1 है (यानि एक-एक करके elements लेंगे)

# अब index-wise elements देखें:
# index 0 -> "apple"
# index 1 -> "banana"
# index 2 -> "cherry" ✅ (यहीं से start होगा)
# index 3 -> "orange"
# index 4 -> "kiwi"
# index 5 -> "melon"
# index 6 -> "mango"

# तो इस slicing का output होगा:
# ['cherry', 'orange', 'kiwi', 'melon', 'mango']




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# 👉 Negative indexing में list को पीछे से गिना जाता है
# "apple"  -> -7
# "banana" -> -6
# "cherry" -> -5
# "orange" -> -4
# "kiwi"   -> -3
# "melon"  -> -2
# "mango"  -> -1

# यहाँ slicing है thislist[-4:-1]
# - start = -4 → यानी "orange" से शुरू होगा
# - end   = -1 → यानी "mango" तक जाएगा लेकिन end exclusive है,
#                इसलिए "mango" शामिल नहीं होगा
# - step  = default 1 → एक-एक करके elements लेंगे

# इसलिए output होगा: ['orange', 'kiwi', 'melon']




