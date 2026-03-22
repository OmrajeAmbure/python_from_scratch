import math


class Juggler_Sequence:
    def juggler_sequence(self,n):
        result = [];
        while True:
            result.append(n);
            if n==1:
                break;
            if n%2==0:
                n = int(math.sqrt(n));
            else:
                n = int(n*math.sqrt(n));
        return result;

obj = Juggler_Sequence();
print(obj.juggler_sequence(9));