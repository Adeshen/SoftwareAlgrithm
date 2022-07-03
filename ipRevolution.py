

# 参考leetcode格式
# from asyncio.windows_events import NULL
def intfun(s):
    # temp=0
    # for i in s:
    #     temp*=10
    #     temp+=int(i)
    # return temp
    return int(s)

def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    #核心思路是将三个点插入到一个字符串中，不能插在首位，只能插在中间
    #第一次尝试需要尝试三重循环，暴力法      
    t=len(s)
    if(len(s)>12):   #四个点分位只能分出3*4=12
        return 0
    ans=[]
    for i in range(1,t):
        if((s[0]=='0' and i>1) or i > 3 ):
            # print(1)
            break
        if(intfun(s[0:i])> 255 ):
            # print(1.0,intfun(s[0:i]))
            break
        for j in range(i+1,t):
            if((s[i]=='0' and j>i+1) or j>i+3):
                # print(2)
                break
            if( intfun(s[i:j]) >255):
                # print(2.)
                break
            for k in range(j+1,t):
                if((s[j]=='0' and k>j+1) or k > j+3):
                    break
                if(intfun(s[j:k])>255):
                    break
                if(s[k]=='0' and k<=t-2):
                    continue
                if(t-k>3):
                    continue
                if(intfun(s[k:t])>255):
                    continue
                ans.append(s[0:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:t])
    return ans
# print(intfun("123456"[0:2]))
# print(int("123"))
print(restoreIpAddresses("25525511135"))    
print(restoreIpAddresses("0000"))
print(restoreIpAddresses("101023"))
print(restoreIpAddresses("172162541"))