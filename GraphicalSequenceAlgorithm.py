#Setting up the sequence list
sizeOfSeq = raw_input("How many vetices are there? ")
sizeOfSeq = int(sizeOfSeq)
index = 0
sequence = [None]*sizeOfSeq

#The user inputs the degrees of the vertices, then sorts it in reverse
while sizeOfSeq>0:
        sequence[index]=int(raw_input("Enter The Degree For A Vertex: "))
        sizeOfSeq=sizeOfSeq-1
        index=index+1
sequence.sort(reverse = True)

#Checks if a degree is bigger or equal to number of vertices, proceeds with algorithm if it's not
if sequence[0]>=len(sequence):
        print 'The Sequence Is Not Graphical: Degree Is Higher Than The Number Of Vertices'

else:   #Algorithm starts here
        seqIndex = 1
        iteration = 0
        negFound = False
        
        while iteration<len(sequence):
                num = sequence[0]
                sequence[0] = 0
                while num>0:
                        sequence[seqIndex]= sequence[seqIndex]-1
                        num = num -1
                        seqIndex = seqIndex + 1
                sequence.sort(reverse=True)
                if sequence[len(sequence)-1]<0:
                        negFound = True
                        break
                seqIndex = 1
                iteration = iteration + 1
                
        if negFound == True:
                print 'The Sequence Is Not Graphical: A Term Of The Sequence Was Negative'
        else:
                print 'The Sequence Is Graphical!'

#Prints The State Of The Sequence At The End Of The Algorithm
print 'Algorithm Ended With Sequence As: {0}'.format(sequence)
