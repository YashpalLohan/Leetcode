class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i in range(len(words)):  # Iterate using index
            if x in words[i]:  
                indices.append(i)  # Store index directly
        return indices