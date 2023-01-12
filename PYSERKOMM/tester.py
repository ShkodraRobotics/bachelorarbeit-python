class sep:

    def __init__(self):
        pass

    def seper(s):
        li = []
        helpers = ""
        for data in s:
            helper = data

            if helper == ";":
                li.append(helpers)
                helpers = ""
            else:
                helpers += helper

        for da in li:
            return (da)