
class text:
    def __init__(self,text,*,thin=False,cancel=False,underline=False,bold=False,Italic=False,hide=False,Bg="black",Txt="white"):
        self.__color={
            "black":30,
            "red":31,
            "green":32,
            "yellow":33,
            "blue":34,
            "mazenta":35,
            "cian":36,
            "white":37
        }
        self.underline=""
        if underline:self.underline="\033[4m"
        self.bold=""
        if bold:self.bold="\033[1m"
        self.italic=""
        if Italic:self.italic="\033[3m"
        self.hide=""
        if hide:self.hide=="\033[8m"
        self.cancel=""
        if cancel:self.cancel=="\033[9m"
        self.thin=""
        if thin:self.thin=="\033[9m"
        self.bg="\033["+str(self.__color[Bg]+10)+"m"
        self.txt="\033["+str(self.__color[Txt])+"m"

        self.text=self.cancel+self.thin+self.underline+self.bold+self.italic+self.bg+self.hide+self.txt+text+"\033[m"
useable_color=[
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "mazenta",
    "cian",
    "white"
]
def move_up(n=1):
    print("\033["+str(n)+"A")
def move_up_start(n=1):
    print("\033["+str(n)+"E")
def move_down(n=1):
    print("\033["+str(n)+"B")
def move_down_start(n=1):
    print("\033["+str(n)+"F")
def move_right(n=1):
    print("\033["+str(n)+"C")
def move_left(n=1):
    print("\033["+str(n)+"D")

def clear_before():
    print("\033[1")
def clear_after():
    print("\033[0")
def clear_all():
    print("\033[2")
def clear_line_before():
    print("\033[1K")
def clear_line_after():
    print("\033[0K")
def clear_line_all():
    print("\033[2K")

def scroll_before(n):
    print("\033["+str(n)+"T")
def scroll_after(n):
    print("\033["+str(n)+"S")
class canvas:
    def __init__(self,*,width=10,height=5):
        self.__width=width
        self.__height=height
        print(str(" "*self.__width,"\n")*height)


#print(text("test",cancel=True,thin=True,underline=True,bold=True,Txt="mazenta",Bg="cian").text)
#scroll_before(20)
