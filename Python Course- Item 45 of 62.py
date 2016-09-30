a = [67, 45, 2, 13, 1, 998]
#      0     1   2   3   4   5 - index order
def corey_sort(a):
    for index in range(1, len(a)): #len(a) = 6(there are 6 numbers in the list above) so our range(1,6) = [1,2,3,4,5]
                                                    #range(start, stop, step)-start and step are optional; index will start at 1 since range(1,6)
        value = a[index]                 #index = 1;  1 in our list is 45 so value = 45 here
        i = index - 1                        #so index = 1 therefore i = 1-1 which = 0 so i = 0
        while i >= 0:                       #i = 0 so this statement is true therefore the if statement will run
            if value < a[i]:                 #value = 45 and i = 0; a[0] is 65; 45 is less than 65 so our if statement is true therefore it will run the following
                a [i + 1] = a[i]             #a[i + 1] is a[0 +1] so a[1] is 45; a[i] = a[0]  which = 65 so we are going to replace 45 with 65 or a[1] with a[0]
                a[i] = value                 #so now a[i] is a[0] which is 45 which = our value which is 45
                i = i - 1                        #i = 0 - 1 which is -1.  This will bring a False value to our while loop and so then we will go to the for loop and 
            else:                               #begin the process again.
                break



b = [89, 23, 33, 45, 10, 12, 45, 45, 45]
def corey_sort(b):
    for index in range(1, len(b)):
        value = b[index]
        i = index - 1
        while i >= 0:
            if value < b[i]:
                b[i + 1] = b[i]
                b[i] = value
                i = i - 1
            else:
                break

corey_sort(a)
print a

corey_sort(b)
print b
