

# 参考leetcode格式
# from asyncio.windows_events import NULL

def restoreIpAddresses( s):
    """
    :type s: str
    :rtype: List[str]
    """
    #核心思路是将三个点插入到一个字符串中，不能插在首位，只能插在中间
    #第一次尝试需要尝试三重循环，暴力法      
    def intfun(s):
        temp=0
        for i in s:
            temp*=10
            temp+=int(i)
        return temp
    t=len(s)
    if(len(s)>12):   #四个点分位只能分出3*4=12
        return 0
    ans=[]
    for i in range(1,t-2):
        if((s[0]=='0' and i>0) or i > 3 ):
            print(1)
            break
        if( intfun(s[0:i])> 255 ):
            print(1.0,intfun(s[0:i]))
            break
        for j in range(i,t-2):
            if((s[i]=='0' and j>i) or j>i+3):
                print(2)
                break
            if( intfun(s[i:j]) >255):
                print(2.)
                break
            for k in range(j,t-2):
                if((s[j]=='0' and k>j) or k > j+3):
                    print(3)
                    break
                if(intfun(s[j:k])>255):
                    print(3.)
                    break
                # if((s[j]=='0' and k>ja) or k > j+3):
                #     break
                ans.append(s[0:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:-1])
    return ans
    
restoreIpAddresses("dsadaad")    