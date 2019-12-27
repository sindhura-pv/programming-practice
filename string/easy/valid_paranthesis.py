class Solution:
    def isValid(self, s: str) -> bool:
        
        if not s:
            return True
        
        st = []
        input_brackets = ['(', '{', '[']
        
        for i in range(len(s)):
            
            if s[i] in input_brackets:
                st.append(s[i])
                
            elif not st:
                return False
                
            elif s[i] == ')':
                if st.pop() != '(':
                    return False
                
            elif s[i] == '}':
                if st.pop() != '{':
                    return False
                
            elif s[i] == ']':
                if st.pop() != '[':
                    return False
                
        return not st
