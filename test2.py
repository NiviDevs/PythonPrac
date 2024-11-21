import re

if __name__ == '__main__':
    n = int(input())
    #taking input of the form css code
    for _ in range(n):
        s = input()
        #checking if the css code is valid
        if re.match(r'#[0-9a-fA-F]{6}', s):
            print(s)



pattern = (r":?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})")
for i in range(int(input())):
  b = re.findall(pattern, input())
  if b:
    print(*b, sep="\n")
    
#print the email ids
print