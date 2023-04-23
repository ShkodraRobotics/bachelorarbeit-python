from OpencvTest.app_class_tk import nootebook_frame


class slid_me(nootebook_frame):
    def __init__(self):
        super().__init__()
    def slider0 (self,i):
        ls0 = "A" + i + ";"
        nootebook_frame.giver(i)
        #return ls0
    def slider1(self,i):
        ls0 = "B" + i+ ";"
        return ls0
    def slider2(self,i):
        ls0 = "C" + i+ ";"
        return ls0
    def slider3(self,i):
        ls0 = "D" + i+ ";"
        return ls0
    def slider4(self,i):
        ls0 = "E" + i+ ";"
        return ls0

