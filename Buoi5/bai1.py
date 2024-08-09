import json
my_dict= {
    '2023601123': 3.0,
    '2023601124': 3.6,
    '2023602125': 2.9,
    '2023605998': 3.19,
    '20236018756':1.9
}
count=0
for i in my_dict.values():
    if i >= 3.0 and i <= 3.5:
        count+=1
print("Có",count, "sinh vien có điem tổng ket trong đoan [3.0, 3.5]")

my_dict.update({'2023603655':3.69})
print("Dict sau khi them 1 sv la:",json.dumps(my_dict,indent=2))

k = dict()
my_dict2= my_dict.copy()
for key, value in my_dict2.items():
    if value < 2.0:
        k.setdefault(key, value)
for key in k:
    my_dict2.pop(key)
print("\nDict sau khi Xóa mọi sinh viên có điểm tổng kết nhỏ hơn 2.0 ra khỏi từ điển: ")
print(json.dumps(my_dict2, indent=2))


print("Dict la:")
print(json.dumps(my_dict,indent=2))