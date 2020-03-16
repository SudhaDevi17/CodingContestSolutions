from functools import lru_cache
class solution:
    def dicesimulator(self , n , rollMax):
        MOD = 10**9 + 7
        print("MOD value is " , MOD)
        @lru_cache(None)
        def dp(i , j , k ):
            if i ==0 :
                return 1
            ans =0
            for d in range(6):
                if d!=j:
                    ans+= dp(i-1 , d , 1)
                elif k+1 <= rollMax[d]:
                    ans += dp(i-1 , d , k+1)
            ans %=MOD
            return ans
        return dp(n , -1 , 0) % MOD

s  = solution()
print(s.dicesimulator(2 , [1,1,1,1,1,1]))