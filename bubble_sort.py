# create a list
NUM_REPEAT = 100
lst = [3,6,1,2,0,9,7,2,10]*NUM_REPEAT

# bubble sort
for k in range(0, len(lst)-1):
    for i in range(0, len(lst)-1):
        if lst[i] > lst[i+1]:
            temp=lst[i+1]
            lst[i+1]=lst[i]
            lst[i]=temp

# make sure the result is correct
assert lst == sorted(lst)

print("bubble sort finished.")
