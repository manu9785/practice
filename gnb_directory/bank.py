print("""how many users detail you want to enter now""")
for directory in range(int(input())):
        print("""ENTER the details in the following sequence name,contact,age,sex.""")
        directory={
                    'name':input(),
                    'contact':input(),
                    'age':input(),
                    'sex':input()
                     }
        for key, value in directory.items():
                print(key, "::", value)

