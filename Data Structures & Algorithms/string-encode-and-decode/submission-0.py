class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for s in strs:
            encoded_string+= str(len(s)) + "#" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string=[]
        i=0

        while i<len(s):
            j=i

            while s[j]!="#":
                j+=1

            length=s[i:j]
            start_string = j + 1
            end_string = start_string + int(length)

            decoded_string.append(s[start_string:end_string])
            i=end_string
        
        return decoded_string

dummy_input = ["Hello","World"]
obj=Solution()
encoded_string=obj.encode(dummy_input)
decoded_string=obj.decode(encoded_string)
print(decoded_string)

