instructor=dict(name='colt',owns_dog=True,num_courses=4,favorite_language='python',is_halarious=False)


for v in instructor.values():
    print(v)


for k in instructor.keys():
        print(k)

for k,v in instructor.items():
    print(f"{k}+{v}")


    # searching key values
    "name" in instructor

    # searching for values
"colt" in instructor.values()