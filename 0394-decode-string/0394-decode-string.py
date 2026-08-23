class Solution(object):
    def decodeString(self, s):
        main_stack=[]
        number_stack=[]
        i=0

        while i<len(s):
            ch=s[i]
            if ch.isdigit():
                num=0
                while i<len(s) and s[i].isdigit():
                    num=num*10+int(s[i])
                    i+=1

                number_stack.append(num)
                i-=1

            elif ch=='[':
                main_stack.append(ch)

            elif ch==']':
                string=""

                while main_stack[-1]!='[':
                    string=main_stack.pop()+string

                main_stack.pop()

                repeat=number_stack.pop()

                main_stack.append(string * repeat)

            else:
                main_stack.append(ch)

            i+=1

        return "".join(main_stack)