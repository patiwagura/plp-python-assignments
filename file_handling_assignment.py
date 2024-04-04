# File handling assignment - Week 05.
'''
  1. create a new text file my_file.txt in write mode 'w'
  write atleast 3 lines of text, include a mix of strings & numbers.
  
  2. Read contents of my_file.txt & display them.
  
  3. append mode 'a' - add additional text to file.
  
  4. Implement error handling, try ... except blocks to handle file exceptions (FileNotFoundError, PermissionError).
  
'''

def create_file(filename):
  try:
    with open(filename, 'w') as f:
      for x in range(3):
        f.write(f" testing writing to file : {x} \n")
        
  except:
    print("Failed to open file " + filename)
    
# read contents from file.
def read_file(filename):
  try:
    with open(filename, 'r') as f:
      for x in f.readlines():
        print(x, end='')
  except:
    print("failed to read file : " + filename)
    
# append additional text to file.
def append_file(filename, text):
  try:
    with open(filename, 'a') as f:
      for x in range(3):
        f.write(f" appending -- {text} {x} \n")
  except:
    print("failed to open file " + filename)
    
# run the program.
filename = 'my_file.txt'
create_file(filename)
append_file(filename, "text to append ")
read_file(filename)
