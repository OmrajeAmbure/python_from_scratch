class nthFibonacci_solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        if n == 0:
            return n;
        if n == 1:
            return n;
        if n > 1:
            return self.nthFibonacci(n-1) + self. nthFibonacci(n-2);
nth = nthFibonacci_solution();
print(nth.nthFibonacci(0));
print(nth.nthFibonacci(1));
print(nth.nthFibonacci(5));