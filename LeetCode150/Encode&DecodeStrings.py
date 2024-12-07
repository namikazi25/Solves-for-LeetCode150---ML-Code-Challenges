
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for i in range(len(strs)):
            # new_str += str(len(strs[i])) + "/" + strs[i]
            new_str += "/" + strs[i]
        return new_str
            

    def decode(self, s: str) -> List[str]:
        return s.split("/")[1:] 

strs = ["Hello", "World"]

new_str = Solution().encode(strs)
print(Solution().decode(new_str))