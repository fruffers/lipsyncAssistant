#GUI lipsync helper for animators

#gets user to type in word
#sorts word out using the letters in it and matching them to vowels then returns object pictures
#one frame with a looping animation and another slideshow playing the stored images corresponding to the word letters

#imports
import wx
import time
from PIL import ImageTk, Image, IcoImagePlugin
from io import StringIO
import os


#instantiate handler class
pngHandle = wx.PNGHandler
#object/instance of handler class
png1 = pngHandle()


word = ""



class App(wx.App):
    #Framework and 'main' caller of functions
    #imgAddress = "pngs/rest.png"
    def OnInit(self):
        imgAddress = "pngs/rest.png"

        #imgAddress = self.getImageAddress("pngs/rest.png")

        #make image object to store images in
        #imgObj = wx.Image(imgAddress,wx.BITMAP_TYPE_PNG)

        #create frame object from other class
        #pass in the imgObj we made and filled here
        self.frameObj = MakeFrame()
        self.frameObj.Show()
        #self.SetTopWindow(self.frameObj)

        return True



    ####lay a new image on top of the init or make a seperate method?
class Syllable(object):
    #attributes that change


    #init function: things that don't change but must be entered upon initialisation/object creation
    def __init__(self,image,syls):
        self.image = image
        self.syls = syls


class MakeFrame(wx.Frame):
    #window all is on
    # objects
    # (image, syls) parameters



    imageList = []

    def __init__(self, parent=None, id=-1, pos=wx.DefaultPosition, title="Lipsync Assistant"):

        #handle capital letters

        # create objects
        ah = Syllable("pngs/ah.png", ["ah", "a","n" ])
        e = Syllable("pngs/ee.png", ["e", "ee", "ce", "sea"])
        eh = Syllable("pngs/eh.png", ["eh", "h", "se"])
        iy = Syllable("pngs/iy.png", ["i", "y"])
        kr = Syllable("pngs/kr.png", ["kr", "k", "r", "s","x"])
        l = Syllable("pngs/l.png", ["l"])
        m = Syllable("pngs/m.png", ["m", "b", "p"])
        o = Syllable("pngs/o.png", ["o", "oh", "ou", "you"])
        rest = Syllable("pngs/rest.png", [" ", ".", ",", ";", "_"])
        th = Syllable("pngs/th.png", ["f", "v","t"])
        uh = Syllable("pngs/uh.png", ["c", "d", "g", "j", "z", "u"])
        w = Syllable("pngs/w.png", ["w", "q"])

        posSyls = [ah, e, eh, iy, kr, l, m, o, rest, th, uh, w]


        ##convert image passed in to a bitmap
        #getImg = image.ConvertToBitmap()
        #get size of image
        ##imgSize = getImg.GetWidth(), getImg.GetHeight()

        #call and fill out the init method of a wx.Frame to create the frame
        #self will refer to the class superclass (parent) init method
        #otherwise you would have to make the frame outside of init and pass it in
        wx.Frame.__init__(self,parent,id,title,pos,size=(1000,1000))

        self.SetBackgroundColour("white")



        #make text box
        enterBoxPanel = wx.Panel(self, size=(200, 800))
        enterBox = wx.TextCtrl(enterBoxPanel, style=wx.TE_MULTILINE, size=(200, 800))

        #refs = []
        # bind event handler (function) when enter is pressed
        ######refs is not being returned
        prevList = []
        enterBox.Bind(wx.EVT_TEXT_ENTER, handler=lambda event: self.makeImages(enterBox, posSyls, prevList))




    def makeImages(self,enterBox, posSyls, prevList):

        words, posSyls = self.giveWord(enterBox,posSyls)
        imageList = self.sortWords(words, posSyls)
        prevList = self.fillImages(imageList, prevList)

        #rebind the function so it uses the prevList in this new scope and images can be deleted
        enterBox.Bind(wx.EVT_TEXT_ENTER, handler=lambda event: self.makeImages(enterBox, posSyls, prevList))



    def giveWord(self,event,posSyls):

        # get words
        textBox = event
        # get text from textbox
        text = str(textBox.GetValue())

        # list holder of words
        words = []
        # temp holder of each word
        word = ""

        global enterTry
        global oldText

        print("entertry", enterTry)

        # need to clear text each time the user resubmits the text box
        text2 = ""
        print("TRUE TEXT", text)
        # if enterTry == False:
        # print("old text",oldText)
        # text = text.replace(oldText,"heyo")
        # print("that text",text)

        # enterTry = True

        # parsing the text
        # add a space on the end so it iterates the whole thing and doesn't break at the empty end
        #text += " "
        print("text", text)

        for letter in text.strip("\n"):
            words.append(letter)
            # print("letter",letter)
            #if letter != " ":
                #word += letter
            #elif letter == " " or letter == "":
                #if word == "" or word == " ":
                    # prevents spaces or nulls being in the
                    # array even if the user puts loads of spaces
                    #pass
                #else:
                    # new word every time a space occurs
                    #words.append(word)
                    #word = ""

            #else:
                #pass

        enterTry = False
        oldText = text

        print("words", words)
        # must remove \n from input
        # newline counts as a new word

        # clear the textbox after enter is pressed
        #textBox.Clear()

        # clear box? or not? have a clear button instead
        # handle words/convert/match them to vowels

        ############need to accept spaces so that the rest is visible############

        return words, posSyls




    def sortWords(self,words,posSyls):


        imageList = []

        for letter in words:
                for syllable in posSyls:
                    if letter in syllable.syls:
                        imageAddress = syllable.image
                        # animate using imageList
                        imageList.append(imageAddress)


        return imageList




    def fillImages(self,imageList, prevList):
        #global imgObjList

        print("prevList is ", prevList)

        if not prevList:
            pass
        else:
            #delete previous images
            for pic in prevList:
                pic.Destroy()
                self.Layout()

        imgObjList = []



        print("imgObjList is ",imgObjList)

        # timer = 0
        # secTimer = 0
        #
        # while timer < 10:
        #     for image in imageList:
        #         aniPic = wx.Image(image, wx.BITMAP_TYPE_PNG)
        #         aniPic = aniPic.ConvertToBitmap()
        #
        #         ref = wx.StaticBitmap(parent=self, bitmap=aniPic)
        #
        #         ref.SetPosition(wx.Point(50, 100))
        #
        #         while secTimer < 10:
        #             secTimer += 1
        #
        #         timer += 1





        counter = 0
        bitmapList = []

        #######big face
        # defPic = wx.Image("pngs/rest.png", wx.BITMAP_TYPE_PNG)
        # defPic = defPic.ConvertToBitmap()
        # bitmap = wx.StaticBitmap(parent=self, bitmap=defPic)
        # bitmap.SetPosition(wx.Point(300, 5))

        #animate
        # for obj in imgObjList:
        #      # place bitmap/show
        #      bitmap.bitmap = obj
        #      bitmap = wx.StaticBitmap(parent=self, bitmap=obj)
        #      bitmap.SetPosition(wx.Point(300, 5))

        # fill list
        for image in imageList:
            # assign address
            imageAddress = image
            # make image object to store images in
            imgObj = wx.Image(imageAddress, wx.BITMAP_TYPE_PNG)
            imgObj = imgObj.Scale(120, 120, wx.IMAGE_QUALITY_HIGH)
            # convert to bitmap
            getImg = imgObj.ConvertToBitmap()
            # store image object in array
            imgObjList.append(getImg)



        refs = []
        vert = 0
        horiz = 200
        counter = 0
        #layout images
        #these are the series of images that show each syllable
        for obj in imgObjList:
            ref = wx.StaticBitmap(parent=self, bitmap=obj)
            refs.append(ref)
            if counter == 6:
                vert += 130
                horiz = 200
                counter = 0
            ref.SetPosition(wx.Point(horiz,vert))
            horiz += 110
            counter += 1

        print("current refs are: ",refs)

        return refs













global enterTry
enterTry = True
global oldText
oldText = ""




#####only letters are counted not joined letters



#instantiate app class
#instantiate App (toolkit/framework) class object



#main event loop
app = App()
app.MainLoop()

