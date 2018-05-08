class Sieve:
    @staticmethod
    def sieve(n):
        a = []
        for x in range(2, n + 1):
            a.append(x)
        p = 2
        sqrt = int(n ** (1 / 2))
        while p <= sqrt:
            if a[p] != 0:
                j = p * p
                while j <= n:
                    a[j - 2] = 0
                    j = j + p
            p += 1
        a = [value for value in a if value != 0]
        return a


