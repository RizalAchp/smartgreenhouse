from timeit import default_timer as timer

class TheCallback:
    """TheCallback.

    :dict = `data = dict[str, int/float]`
                    dictionary keseluruhan data dari callback
    """
    data = {
        'humid': 0.0,  'temp': 0.0, 'soil': 0, 'hcsr': 0, 'ldr': 0,
        'relay1': 0, 'relay2': 0, 'relay3': 0, 'relay4':0
    }
    def dht_callback(self,a):
        """dhtcallback.
        :param a: return data dari input dht
                dimasukkan kedalam dict data
        """
        self.data['humid'] = a[4]
        self.data['temp'] = a[5]

    def soil_callback(self, b):
        """soilcallback.
        :param b: return data dari input soilsensor
                dimasukkan kedalam dict data
        """
        self.data['soil'] = b[2]

    def hcsr_callback(self,c):
        """hcsrcallback.
        :param c: return data dari input hcsr
                dimasukkan kedalam dict data
        """
        self.data['hcsr'] = c[2]

    def ldr_callback(self,d):
        """ldrcallback.
        :param d: return data dari input ldr
                dimasukkan kedalam dict data
        """
        self.data['ldr'] = d[2]

    def rel1_callback(self,r1):
        """rel1_callback.
        :param e:
        """
        self.data['relay1'] = r1[0]*100.0

    def rel2_callback(self,r2):
        """rel2_callback.
        :param e:
        """
        self.data['relay2'] = r2[0]*100.0

    def rel3_callback(self,r3):
        """rel3_callback.
        :param e:
        """
        self.data['relay3'] = r3[0]*100.0

    def rel4_callback(self,r4):
        """rel4_callback.
        :param e:
        """
        self.data['relay4'] = r4[0]*100.0


if __name__ == "__main__":
    def test_with_dict():
        """fun_test."""
        callback = TheCallback()
        start = timer()
        for i in range(1000):
            callback.rel4_callback([0,0,i])
            # print(f'{callback.data["soil"]}')
        end = timer()
        print(f'Time for dict calculations:{round(end - start, 6)}')

    def test_with_list():
        callback = TheCallback()
        start = timer()
        for j in range(1000):
            callback.rel3_callback([0,0,j])
            # print(f'{callback._c}')
        end = timer()
        print(f'Time for list calculations:{round(end - start, 6)}')

    try:
        test_with_dict()
        test_with_list()
    except:
        pass
