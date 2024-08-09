import json
s=str(input("Nhap xau ky tu: "))
s.split()
my_dict={}
for key in s.split():
    if key in my_dict:
        my_dict[key]+=1
    else:
        my_dict[key]=1
print(j"Dict la:")
print(json.dumps(my_dict, indent=2))
