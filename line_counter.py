import os
file_line = 0 
total_lines = 0


for file in os.listdir(os.getcwd()):
 if file.endswith(".java"): 
  with open(os.path.join(os.getcwd(), file)) as f:
   file_line = 0
   for line in f:
    file_line = file_line + 1;
   print(file + "  Count: " + str(file_line))
   total_lines = file_line + total_lines
  continue
 else:
  continue
print("\nTotal Lines :" + str(total_lines))




