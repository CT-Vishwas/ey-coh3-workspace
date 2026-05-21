# fh = open('C:\\Users\\VishwasKSingh\\Workspace\\ey-coh3-workspace\\data\\data.csv')
print("This is vishwas\\ I am learning python\\")
print("This is vishwas\t I am learning python\n")
print("This is vishwas\\t I am learning python\\n")

# fh = open(r'C:\Users\VishwasKSingh\Workspace\ey-coh3-workspace\data\data.csv')
# data = fh.read()
# print(data)
# fh.close()

file_path = r'C:\Users\VishwasKSingh\Workspace\ey-coh3-workspace\data\data1.csv'
try:
    with open(file_path, 'r') as fh:
        data = fh.read()
        print(data)
        fh.write("\nmanoj,25,tumkur")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except IOError as e:
    print(f"IO error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")