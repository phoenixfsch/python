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

def checkFile(file):
    if file.closed:
        print(f"File: {file.name} is closed.")
    else:
        print(f"File: {file.name} remained open")
  
def getMatchingLines(inputfile,rexp,result):
    print("Extract info from file.")
    with FileManager(inputfile, 'r') as f: 
        for line in f:
            if rexp.search(line):
                result.append(re.sub(rexp,"meow",line))

    checkFile(f)

    return result

def writeResults(outputfile,result):
    print("Write results to a new file.")
    with FileManager(outputfile, 'w') as f: 
        f.write('\n'.join(result))

    checkFile(f)

def main():

    result = [""]
    if len(sys.argv) != 3:
        print("Please, provide an input and an output file as an argument: script <in> <out>")
        sys.exit()   
    else:
        logFilePath=str(sys.argv[1])
        resultFilePath=str(sys.argv[2])

    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Arguments: {str(sys.argv)}")
    print(f"Input file: {logFilePath}")
    print(f"Output file: {resultFilePath}")

    regexp=re.compile('[a-zA-Z]+(?=\s\d)\s\d+\s08:[0-5]\d:[0-5]\d')

    getMatchingLines(logFilePath,regexp,result)
    writeResults(resultFilePath,result)

if __name__ == '__main__':
    main()





