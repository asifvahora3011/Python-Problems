'''You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after
converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum
number of matching words with the query.
Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
Input:
Please input your query string
“Python is”
Output:
3 results found:
python is not python snake
python is good
Python is cool'''
import time
def matchingWords(query,sentences):
    queryWords = query.split(" ")
    sentencesWords = sentences.split(" ")
    score =0
    for queryWord in queryWords:
        # print(f"i={queryWord}")
        for sentencesWord in sentencesWords:
            # print(f"j={sentencesWord}")
            if queryWord.lower()==sentencesWord.lower():
                score+=1
    return score
if __name__ == '__main__':
    sentences=["Python is good","python is cool","snake"]
    query=input("Enter a query:\n")
    t1=time.time()
    scores = [matchingWords(query,sentence) for sentence in sentences]
    sortsentence=[sortsent for sortsent in sorted(zip(scores,sentences),reverse= True) if sortsent[0]!=0]
    print(f"{len(sortsentence)} results found!")
    for score, item in sortsentence:
        print(f"{item}: with the score of:{score} ")
    t2 = time.time()
    print(f"Results found in {t2-t1} seconds")