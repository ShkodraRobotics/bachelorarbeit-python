class sep:

    def __init__(self):
        pass


    def sep(s):
        li = []
        helpers =""
        for data in s:
            helper = data

            if helper == ";":
                li.append(helpers)
                helpers =""
            else:
                helpers += helper



        for da in li:
            print(da)