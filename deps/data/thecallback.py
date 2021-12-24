

class TheCallback:
    """TheCallback.
    :list a: data appending dht dari list data yang didapatkan callback
    :list b: data appending soil sensor dari list data yang diapatkan callback
    :list c: data appending hcsr sensor dari list data yang didapatkan callback
    :list d: data appending ldr sensor dari list data yang diapatkan callback
    :list e: data appending potensio dari list data yang didapatkan callback
    :list f: data appending potensio2 dari list data yang didapatkan callback
    :list r1: data appending relay1 dari list data yang didapatkan callback
    :list r2: data appending relay2 dari list data yang didapatkan callback
    :list r3: data appending relay3 dari list data yang didapatkan callback
    :list r4: data appending relay4 dari list data yang didapatkan callback
    """
    _a = []
    _b = []
    _c = []
    _d = []
    _r1 = []
    _r2 = []
    _r3 = []
    _r4 = []
    _rels = []


    def dht_callback(self,a):
        """dhtcallback.

        :param a: return data dari input dht
        """
        self._a.clear()
        self._a.append(a[4])
        self._a.append(a[5])
        return self._a

    def soil_callback(self, b):
        """soilcallback.

        :param b: return data dari input soilsensor
        """
        self._b.clear()
        self._b.append(b[2])
        return self._b

    def hcsr_callback(self,c):
        """hcsrcallback.

        :param c: return data dari input hcsr
        """
        self._c.clear()
        self._c.append(c[2])
        # self._c.append(c[3])
        return self._c

    def ldr_callback(self,d):
        """ldrcallback.

        :param d: return data dari input ldr
        """
        self._d.clear()
        self._d.append(d[2])
        return self._d

    def rel1_callback(self,e):
        """rel1_callback.

        :param e:
        """
        self._r1.clear()
        self._r1.append(e[0]*100.0)
        return self._r1

    def rel2_callback(self,e):
        """rel2_callback.

        :param e:
        """
        self._r2.clear()
        self._r2.append(e[0]*100.0)
        return self._r2

    def rel3_callback(self,e):
        """rel3_callback.

        :param e:
        """
        self._r3.clear()
        self._r3.append(e[0]*100.0)
        return self._r3

    def rel4_callback(self,e):
        """rel4_callback.

        :param e:
        """
        self._r4.clear()
        self._r4.append(e[0]*100.0)
        return self._r4

    def rels_callback(self,rels):
        """rel4_callback.

        :param e:
        """
        self._rels.clear()
        self._rels.append(rels[0]*100.0)
        self._rels.append(rels[1]*100.0)
        self._rels.append(rels[2]*100.0)
        self._rels.append(rels[3]*100.0)
        return self._r4

    # def pot1_callback(self,e):
    #     """ldrcallback.

    #     :param d: return data dari input potensio satu
    #     """
    #     self._e.clear()
    #     self._e.append(e[2])
    #     return self._e

    # def pot2_callback(self,f):
    #     """ldrcallback.

    #     :param d: return data dari input potensio dua
    #     """
    #     self.f.clear()
    #     self.f.append(f[2])
    #     return self.f

def fun_test():
    """fun_test."""
    callback = TheCallback()
    calldht = callback.dht_callback
    for i,j in zip(range(0,10),range(0,10)):
        a = callback._a
        calldht([i,j])

        print(a[0])


if __name__ == "__main__":
    fun_test()

