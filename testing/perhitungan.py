from timeit import default_timer as timer
a = 1
data = {"a":0.0, "b":0.0 }

def one():
    start_ = timer()
# print(a*100.0)
    for i in range(100):
        data['a'] = a/0.01
        i+=1
    end_ = timer()
    print(f'pembagian = :{end_ - start_}')
    print(f'pembagian = :{type(end_ - start_)}\n')

def two():
    start = timer()
# print(a*100.0)
    for i in range(100):
        data['b'] = a*100.0
        i+=1
    end = timer()
    print(f'perkalian = :{end - start}')
    print(f'perkalian = :{type(end - start)}\n')


if __name__ == "__main__":
    two()
    one()
    print(data,'\n')
