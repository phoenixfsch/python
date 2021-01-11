# Python exercise 0
import re, sys

class FileManager(): 
    def __init__(self, filename, mode): 
        self.filename = filename 
        self.mode = mode 
        self.file = None
          
    def __enter__(self): 
        self.file = open(self.filename, self.mode) 
        return self.file
      
    def __exit__(self, exc_type, exc_value, exc_traceback): 
        self.file.close() 

def main():
    if len(sys.argv) != 3:
        print("Please, provide an input and an output file as an argument: script <in> <out>")
        sys.exit()   
    else:
        logFilePath=str(sys.argv[1])
        resultFilePath=str(sys.argv[2])

    print('Number of arguments:', len(sys.argv))
    print('Arguments:', str(sys.argv))
    print('Input file:', logFilePath)
    print('Output file:', resultFilePath)

    regexp=re.compile('[a-zA-Z]+(?=\s\d)\s\d+\s11:[0-5]\d:[0-5]\d')
    #result=""

    result=getMatchingLines(logFilePath,regexp)
    writeResults(resultFilePath,result)
      
def getMatchingLines(inputfile,rexp):
    print('Extract info from file.')
    with FileManager(inputfile, 'r') as f: 
        for line in f:
            if rexp.search(line):
                result=re.sub(rexp,"meow",line)

    if f.closed:
        print("File:",f.name," is closed.")
    else:
        print("File:",f.name," remained open")
    
    #print(result)
    return result

def writeResults(outputfile,result):
    print('Write results to a new file.')
    with FileManager(outputfile, 'w') as f: 
        f.write(result)

    if f.closed:
        print("File:",f.name," is closed.")
    else:
        print("File:",f.name," remained open")

if __name__ == '__main__': main()





