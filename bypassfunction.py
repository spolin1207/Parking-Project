# import os


# def generate_passcode():
#     file_path = 'bypasscodes.txt'

#     # check if size of file is 0
#     if os.stat(file_path).st_size == 0:
#         print('No bypass codes were added')
#         exit()

#     code = ""

#     # Extract Code
#     with open('bypasscodes.txt', 'r') as f:
#         code = f.readlines()[-1]

#     # Removes bypass code used from file
#     fd = open("bypasscodes.txt", "r")
#     d = fd.read()
#     fd.close()
#     m = d.split("\n")
#     s = "\n".join(m[:-1])
#     fd = open("bypasscodes.txt", "w+")
#     for i in range(len(s)):
#         fd.write(s[i])
#     fd.close()

#     print("Last line of file deleted")
#     if os.stat(file_path).st_size == 0:
#         print("Must add new set of codes")

#     return code

file = open("bypasscodes.txt", "r")
Counter = 0

# Reading from file
Content = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        Counter += 1

print("You have", Counter, "codes left")
