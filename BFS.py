# BFS(breath first search)
from collections import deque
def word_ladder(beginWord:str, endWord: str, wordList:list[str])->list[str]:
    wordSet=set(wordList)
    if endWord not in wordSet:
        return[]
    queue=deque()
    queue.append((beginWord,[beginWord]))
    while queue:
        current_word, path=queue.popleft()
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord=current_word[:i]+c+current_word[i+1:]
                if nextWord==endWord:
                    return path+[endWord]
                if nextWord in wordSet:
                    wordSet.remove(nextWord)
                    queue.append((nextWord,path+[nextWord]))
    return []
beginWord=input("enter the begin word:").strip()
endWord=input("enter the endword:").strip()
wordList_input=input("Enter the word list:").strip()
wordList=wordList_input.split()
result=word_ladder(beginWord,endWord,wordList)
if result:
    print(",".join(result))
else:
    print([])
