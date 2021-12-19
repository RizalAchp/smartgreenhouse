import time
import random
start_time = time.time()
y = 10000
for loop in range(y):
    a = random.uniform(10.1,100.1)
    b = random.uniform(10.1,100.1)
    print(f'data1{a}')
    print(f'data2{b}')
    if a < 70.0:
        print("if pertama")
        if b > 33.0:
            print("if kedua")
        # print(f'rel1 and rel2 hidup')
        else:
            print("else kedua")

    else:
        print("else pertama")
        # print(f'rel1 and rel2 mati')

    # time.sleep(2)
print(f'Execution time: {time.time() - start_time} seconds for {y} iterations.')
