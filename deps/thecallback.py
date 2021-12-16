class TheCallback:
    """TheCallback."""

    a = []
    b = []
    c = []
    d = []
    def dhtcallback(self,a):
        """dhtcallback.

        :param a:
        """
        self.a.clear()
        self.a.append(a[4])
        self.a.append(a[5])
        return self.a

    def soilcallback(self,b):
        """soilcallback.

        :param b:
        """
        self.b.clear()
        self.b.append(b[2])
        self.b.append(b[3])
        return self.b

    def hcsrcallback(self,c):
        """hcsrcallback.

        :param c:
        """
        self.c.clear()
        self.c.append(c[2])
        # self.c.append(c[3])
        return self.c

    def ldrcallback(self,d):
        """ldrcallback.

        :param d:
        """
        self.d.clear()
        self.d.append(d[2])
        self.d.append(d[3])
        return self.d


def fun_test():
    """fun_test."""
    callback = TheCallback()
    calldht = callback.dhtcallback
    for i,j in zip(range(0,10),range(0,10)):
        a = callback.a
        calldht([i,j])

        print(a[0])


if __name__ == "__main__":
    fun_test()

