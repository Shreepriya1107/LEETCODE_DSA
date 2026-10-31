class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        c = 0
        for i in range(len(operations)):
            if operations[i] == "++X" or operations[i] == "X++":
                c+=1
            elif operations[i] == "--X" or operations[i] == "X--":
                c-=1
        return c
        