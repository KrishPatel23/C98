def countWords():
    fileName=input("Enter The File Name:")
    numberofwords=0
    file=open(fileName, 'r')
    for i in file: 
        words=i.split()
        numberofwords=numberofwords+len(words)
    print(numberofwords)
countWords()
    
