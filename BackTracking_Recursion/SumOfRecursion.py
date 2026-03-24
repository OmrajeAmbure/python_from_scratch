class Sum_Of_Recursion:
    sum = 0;
    def sum_of_recursion(self,n):
            if n == 0 :
                return ;
            return self.sum_of_recursion(n-1);
obj = Sum_Of_Recursion();
obj.sum_of_recursion(8);