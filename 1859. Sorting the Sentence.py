class Solution:
    def sortSentence(self, s: str) -> str:
        n= len(s)
        check=[]
        result=[]
        word=s.split()
        for h in range(n+1):
            check.append(h)
        for x in check:
                for v in range(len(word)):
                    if f"{x}" in word[v]:
                                if word[v] not in result:
                                    result.append(word[v])
        new=" ".join (result) 
        new=str(new)
        num=(1,2,3,4,5,6,7,8,9)
        final=""
        for n in new:
            if n == " ":
                    final=final+" "
            else:
                    if n not in str(num):
                            final=final+n
        g=f"{final}"
        return g
