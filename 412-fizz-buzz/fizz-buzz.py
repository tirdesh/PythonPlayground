class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * n
        for i in range(len(res)):
            k=i+1
            if k%3==0 and k%5==0:
                res[i]="FizzBuzz"
            elif k%3==0:
                res[i]="Fizz"
            elif k%5==0:
                res[i]="Buzz"
            else:
                res[i] = str(k)
        return res
        