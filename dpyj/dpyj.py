#! /usr/bin/python3
#######################################
#DPYJ(DecoratedPYthonJson)--Version1.1#
#######################################
import json
import sys
sys.path.append("/usr/bin/beatbox4108/dpyj/")
import texts
import subprocess
import os
class syntax:
    def __output_text(self):
        self.text+=texts.text("\n",Txt="blue",Bg="yellow").text
        for self.__tmp2 in self.__tmp1["text"]:
            if not "type" in self.__tmp2:self.__tmp2["type"]="normal"
            if self.__tmp2["type"]=="quote":
                if not "color" in self.__tmp2:
                    self.__tmp2["color"]="black"
                if not "bg" in self.__tmp2:
                    self.__tmp2["bg"]="white"
                if not "say" in self.__tmp2:self.__tmp2["say"]="Unknoun"
                self.text+=texts.text("\n",Txt="blue",Bg="yellow").text
                self.text+=texts.text(
                    "quote say "+self.__tmp2["say"]+":\n"+self.__tmp2["text"],
                    Txt=self.__tmp2["color"],
                    Bg=self.__tmp2["bg"],
                    cancel=self.__tmp2.get("cancel"),
                    bold=self.__tmp2.get("bold"),
                    Italic=self.__tmp2.get("italic"),
                    thin=self.__tmp2.get("thin"),
                    underline=self.__tmp2.get("underline"),
                    hide=self.__tmp2.get("hide")
                ).text.replace("\n","\t\n")
                return
            else:
                if not "color" in self.__tmp2:
                    self.__tmp2["color"]="blue"
                if not "bg" in self.__tmp2:
                    self.__tmp2["bg"]="yellow"
            self.text+=texts.text(
                self.__tmp2["text"],
                Txt=self.__tmp2["color"],
                Bg=self.__tmp2["bg"],
                cancel=self.__tmp2.get("cancel"),
                bold=self.__tmp2.get("bold"),
                Italic=self.__tmp2.get("italic"),
                thin=self.__tmp2.get("thin"),
                underline=self.__tmp2.get("underline"),
                hide=self.__tmp2.get("hide")
            ).text.replace("\n","\t\n")
        self.text+=texts.text("\n",Txt="blue",Bg="yellow").text
    def __output_code(self):
        self.codeonly+=self.__tmp1["code"]+"\n"
        if self.__tmp1.get("file")==None:
            self.__tmp1["file"]=sys.argv[1]
        if not self.__tmp1["file"] in self.write_file: self.write_file[self.__tmp1["file"]]=""
        self.write_file[self.__tmp1["file"]]+=self.__tmp1["code"]+"\n"
        self.text+=texts.text("\n"+self.__tmp1["file"]+" CODE:\n\t"+self.__tmp1["code"]+"\n-----",Bg="cian").text
    def __init__(self,format_dict,author=None):
        self.format=format_dict
        self.text=""
        self.codeonly=""
        self.write_file={}
        if author!=None:self.format["author"]=author
        if self.format.get("author")==None:
            self.format["author"]="Unknoun"
        if self.format.get("title")==None:
            self.format["title"]="untitled"
        if self.format.get("pythonversion")==None:
            self.format["pythonversion"]=3
        self.text+=texts.text("\n"+self.format["title"],Bg="blue",Txt="white",bold=True).text
        self.text+=texts.text("\nAuthor:"+self.format["author"],Bg="red",Txt="white",bold=True).text
        for self.__tmp1 in self.format["code"]:
            self.text+=texts.text("\n"+("="*20),Bg="blue",Txt="white").text
            if not "type" in self.__tmp1:
                self.__tmp1["type"]="text"
            if self.__tmp1["type"]=="text":
                for self.__tmp2 in self.__tmp1["text"]:
                    self.__output_text()
                self.__output_code()
            elif self.__tmp1["type"]=="description":
                    self.__output_text()
            elif self.__tmp1["type"]=="code":
                self.__output_code()
            elif self.__tmp1["type"]=="gloup":
                self.text+=syntax(self.__tmp1,self.format["author"]).text.replace("\n","\n\t")
                self.codeonly+=syntax(self.__tmp1).codeonly
                for self.__tmp3 in syntax(self.__tmp1).write_file.items():
                    if not self.__tmp3[0] in self.write_file :self.write_file[self.__tmp3[0]]=""
                    self.write_file[self.__tmp3[0]]+=self.__tmp3[1]
            
        self.text+=texts.text("\n"+("="*20),Bg="blue",Txt="white").text



if __name__=="__main__":
    if len(sys.argv)==1:
        print("DPYJ(DecoratedPYthonJson)--Version1.1")
    elif len(sys.argv)==2 or (len(sys.argv)==3 and sys.argv[2]=="open"):
        with open(sys.argv[1],"r") as j:
            j=json.load(j)
            print(syntax(j).text)
    elif len(sys.argv)==3 and sys.argv[2]=="codeonly":
        with open(sys.argv[1],"r") as j:
            j=json.load(j)
            print(syntax(j).codeonly)
            with open(sys.argv[1]+".py","w",encoding="UTF-8")as w:
                w.write(syntax(j).codeonly)
    if "write" in sys.argv:
        with open(sys.argv[1],"r") as j:
            j=json.load(j)
            for txt in syntax(j).write_file.items():
                print(txt[1])
                with open(txt[0]+".py","w",encoding="UTF-8")as w:
                    w.write(txt[1])
    if "run" in sys.argv:
        with open(sys.argv[1],"r") as j:
            j=json.load(j)
            for txt in syntax(j).write_file.items():
                with open(txt[0]+".py","w",encoding="UTF-8")as w:
                    w.write(txt[1])
                    txt=list(txt)
                    if txt[0][:2]=="./":txt[0]=txt[0][1:]
                    path=os.getcwd().replace("\\","/")
                    if path[-1]!="/":path+="/"
                print("running","python"+str(j["pythonversion"])+" "+path+txt[0]+".py")
                subprocess.run("python"+str(j["pythonversion"])+" "+path+txt[0]+".py",shell=True)
