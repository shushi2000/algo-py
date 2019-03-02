i1 = 3141592653589793238462643383279502884197169399375105820974944592
i2 = 2718281828459045235360287471352662497757247093699959574966967627

final_result = 0
ip = 0 
for i in reversed(str(i1)):
    jp = 0
    for j in reversed(str(i2)):
        print (int(i), int(j), jp, ip)
        temp = int(i) * int(j) * (10**jp) * (10 ** ip)
        print(temp)
        final_result += temp
        jp += 1
    ip += 1

assert final_result == i1 * i2
print ("{} * {} = {}".format(i1, i2, final_result))

