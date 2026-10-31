class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        mc=0
        for w in sentences:
            c=len(w.split())
            if c>mc:
                mc=c
        return mc

        