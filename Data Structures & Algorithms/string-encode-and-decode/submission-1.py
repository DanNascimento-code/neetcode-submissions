class Solution:

    def encode(self, strs: List[str]) -> str:
       encoded_string = "".join(f"{len(s)}#{s}" for s in strs) 
       return encoded_string     

    def decode(self, encoded_string: str) -> List[str]:
        res, i = [], 0
        while i < len(encoded_string):
            j = encoded_string.index("#", i)
            length = int(encoded_string[i:j])
            res.append(encoded_string[j+1:j+1+length])
            i = j + 1 + length
        return res

        
