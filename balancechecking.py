class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            unique =[]
            lp=0
            rp=0
            lb=0
            rb=0
            lc=0
            rc=0
            for i in range(0, len(parenthesis)-1):
                if(parenthesis[i]=="("):
                    lp+=1
                if( parenthesis[i] == ")"):
                    rp+=1
                if(parenthesis[i]== "["):
                     lb+=1
                if(parenthesis[i]=="]"):
                     rb+=1
                if(parenthesis[i]=="{"):
                     lc+=1
                if parenthesis[i]=='}':
                     rc+=1
            if( lp==rp and lb==rb and lc== rc):
                 return True
            else:
                 return False
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            pass

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()