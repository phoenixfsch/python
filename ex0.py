# Python exercise 0
from sys import argv
import re

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

def addLeadingZeroToNumber(number):
    return str(0)+str(number)

def getInput():
    while True:
        try:
            hour=int(input("Please, define the desired hour to find the correct lines in the log file."))
        except ValueError:
            print("Invalid input. Only int type is acceptable.")
            continue
        else:
            if len(str(hour)) < 2:
                hour=addLeadingZeroToNumber(hour)
                break
            elif hour < 13:
                break
            else:
                continue

    return str(hour)

def main():

    result = [""]
    if len(argv) != 3:
        print("Please, provide an input and an output file as an argument: script <in> <out>")
        exit()
    else:
        logFilePath=str(argv[1])
        resultFilePath=str(argv[2])

    print(f"Number of arguments: {len(argv)}")
    print(f"Arguments: {str(argv)}")
    print(f"Input file: {logFilePath}")
    print(f"Output file: {resultFilePath}" )

    hour=getInput()
    regexp=re.compile(f'[a-zA-Z]+(?=\s\d)\s\d+\s{hour}:[0-5]\d:[0-5]\d')

    print(f"Looking for logs at {hour} hour")
    getMatchingLines(logFilePath,regexp,result)
    writeResults(resultFilePath,result)

if __name__ == '__main__':
    main()
