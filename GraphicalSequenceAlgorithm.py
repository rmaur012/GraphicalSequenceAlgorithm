#Setting up the sequence list
try:
        sizeOfSeq = raw_input("How many vetices are there? ")
        sizeOfSeq = int(sizeOfSeq)
        index = 0
        sequence = [None]*sizeOfSeq
except ValueError:
        print 'A Non-Numerical Value Was Entered. Please Try Again And Enter With A Numerical Value.'
        quit()


#The user inputs the degrees of the vertices, then sorts it in reverse.
#It will also calculate sum of the sequence of degrees to then be evaluated in the second if statement after the loop
seqSum = 0
while sizeOfSeq>0:
        try:
                sequence[index]=int(raw_input("Enter The Degree For A Vertex: "))
                seqSum = seqSum + sequence[index]
                sizeOfSeq=sizeOfSeq-1
                index=index+1
        except ValueError:
                print 'A Non-Numerical Value Was Entered. Please Enter A Numerical Value.'
sequence.sort(reverse = True)


#Checks if a degree is bigger or equal to number of vertices, 
#then will check if the sum of the sequence = 2*(number of edges), which would make it not graphical if it does not equal,
#then it proceeds with algorithm if it's not determined to be either of the first two
if sequence[0]>=len(sequence):
        print 'The Sequence Is Not Graphical: Degree Is Higher Than The Number Of Vertices'

elif seqSum%2 !=0:
        print 'The Sequence Is Not Graphical: The Sum Of The Degrees In The Sequence Is Not Divisible By 2'
        
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
