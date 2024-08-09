import json
CONFIG= {
    'n':1500,
    'm':2,
    'CLUSTERS':3,
    'ITER':10000,
    'METHOD': 'FCM',
    'MEASURE':'EUCLIDEAN',
    'YEARS':51
}
print("ND cua dict la:")
print(json.dumps(CONFIG,indent=2))

CONFIG["MEASURE"]="MANHATAN"
print("Dict sau khi sua thong so cua MEASURE:")
print(json.dumps(CONFIG,indent=2))

print("Thong so cua METHOD la:")
print(CONFIG.get('METHOD'))

CONFIG.update({'LOSS FUNCTION':'NORM_2'})
print("Dict sau khi them la:")
print(json.dumps(CONFIG,indent=2))

del CONFIG['YEARS']
print("Dict sau khi xoa key YEARS:")
print(json.dumps(CONFIG,indent=2))

s = input("\nNhập một chuỗi: ")
found = False
for key, value in CONFIG.items():
    if s == value:
        print(f"Chuỗi '{s}' trùng với giá trị của thông số: {key}")
        found = True
        break
if not found:
    print(f"Chuỗi '{s}' không trùng với bất kỳ giá trị nào trong từ điển.")

my_set=set()
my_list=list()
for key,value in CONFIG.items():
    my_set.add(key)
    my_list.append((value))
print("Gia tri cua cac thong so trong file la:")
print(my_set)
print(my_list)