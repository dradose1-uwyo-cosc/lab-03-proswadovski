names = ["Peyton","Emma","Braden","Ryan","Wesley","Martin"]
print(names)
del names[0]
print(names)
for name in names:
    print(f"{name} is on my table")
    names.sort()
    print(names)