import settings
import math
# transparent from
# import tkinter as tk # Python 3
# root = tk.Tk()
# # The image must be stored to Tk or it will be garbage collected.
# label = tk.Label(root, bg='white')
# root.overrideredirect(True)
# root.geometry("+250+250")
# root.lift()
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", "black")
# root.attributes('-alpha', 0.3)
# label.pack()
# label.mainloop()


# //////////////////////////////////
from tkinter import *
import time
#
# def sel():
#    selection = "Value = " + str(var.get())
#    label.config(text = selection)
#
# root = Tk()
# var = DoubleVar()
# scale = Scale( root, variable = var ,orient=HORIZONTAL)
# scale.pack(anchor=CENTER)
#
# button = Button(root, text="Get Scale Value", command=sel)
# button.pack()
#
# label = Label(root)
# label.pack()
#
# root.mainloop()
import threading

class SettingForm (threading.Thread):
   """ shows using the same StringVar in the second list box
       and in the entry box
   """

   def __init__(self,sett):
      threading.Thread.__init__(self)
      self.settings=sett
      self.top = Tk()
      self.top.title("Test of Entry")
      self.top.geometry("250x700+0+0")
      # self.top.wm_attributes("-transparentcolor", "white")
      # self.top.attributes('-alpha', 0.5)



      self.bs_var=IntVar(self.settings.MOG2shadow)
      bs_check = Checkbutton(self.top, text="Background", variable=self.bs_var,
                       onvalue=1, offvalue=0,
                             width=20,command=self.bs_fliper)
      self.bs_var.set(self.settings.bsMethod)
      bs_check.pack()

      self.bs_box=LabelFrame(self.top,labelwidget=bs_check)
      self.bs_box.pack()

      self.bs_learningrate=DoubleVar(value=self.settings.MOG2learningRate)
      bs_learnrate=Scale(self.bs_box,variable=self.bs_learningrate,
                         orient=HORIZONTAL,command=self.bs_changeLearningrate,
                         resolution=0.001,from_=0,to=1,label="Bs Learning Rate")
      bs_learnrate.pack()

      self.bs_history = IntVar(value=self.settings.MOG2history)
      bs_history = Scale(self.bs_box, variable=self.bs_history,
                           orient=HORIZONTAL, command=self.bs_changeHist,
                           resolution=10, from_=0, to=200, label="history")
      bs_history.pack()

      self.bs_shadow=IntVar(value=self.settings.MOG2shadow)
      shadow_check = Checkbutton(self.bs_box, text="Shadow", variable=self.bs_shadow,
                             onvalue=1, offvalue=0,
                             width=20, command=self.bs_shadowfliper)
      shadow_check.pack()

      self.bs_threshold = IntVar(value=self.settings.thresholdLimit)
      bs_threshold = Scale(self.bs_box, variable=self.bs_threshold,
                         orient=HORIZONTAL, command=self.bs_changeThresh,
                         resolution=5, from_=0, to=100, label="threshold")
      bs_threshold.pack()

      self.bs_fliper()

      self.minarea = IntVar(value=math.sqrt(self.settings.minArea))
      minarea = Scale(self.top, variable=self.minarea,
                           orient=HORIZONTAL, command=self.changeMinArea,
                           resolution=10, from_=10, to=300, label="MinArea")
      minarea.pack()

      self.dilation = IntVar(value=self.settings.dilationPixels)
      dilation = Scale(self.top, variable=self.dilation,
                      orient=HORIZONTAL, command=self.changeDilation,
                      resolution=1, from_=1, to=60, label="Dilation Pixel")
      dilation.pack()

      self.threshold = IntVar(value=self.settings.thresholdLimit)
      threshold = Scale(self.top, variable=self.threshold,
                        orient=HORIZONTAL, command=self.changeThreshold,
                        resolution=1, from_=10, to=200, label="Threshold")
      threshold.pack()

      self.MinMovement = IntVar(value=self.settings.movementMinimum)
      MinMovement = Scale(self.top, variable=self.MinMovement,
                        orient=HORIZONTAL, command=self.changeMinMovement,
                        resolution=1, from_=10, to=200, label="MinMovement")
      MinMovement.pack()

      self.MaxMovement = IntVar(value=self.settings.movementMaximum)
      MaxMovement = Scale(self.top, variable=self.MaxMovement,
                        orient=HORIZONTAL, command=self.changeMaxMovement,
                        resolution=1, from_=10, to=200, label="MaxMovement")
      MaxMovement.pack()

      self.NoOfFrames = IntVar(value=self.settings.movementTime)
      NoOfFrames = Scale(self.top, variable=self.NoOfFrames,
                        orient=HORIZONTAL, command=self.changeNoOfFrames,
                        resolution=1, from_=10, to=200, label="No of Frames after which alaram is genetated")
      NoOfFrames.pack()




      self.blur=IntVar(self.settings.useGaussian)
      blur = Checkbutton(self.top, text="Blur", variable=self.blur,
                       onvalue=1, offvalue=0,
                             width=20,command=self.changeBlur)
      self.blur.set(0)
      blur.pack()

      self.blur_box=LabelFrame(self.top,labelwidget=blur)
      self.blur_box.pack()

      self.blur_pixel=IntVar(value=self.settings.gaussianPixels)
      blur_pixel=Scale(self.blur_box,variable=self.blur_pixel,
                         orient=HORIZONTAL,command=self.changeblur_pixel,
                         resolution=1,from_=3,to=51,label="Blur Pixel")
      blur_pixel.pack()
      self.changeBlur()


      # label_1 =  Label(self.top, textvariable=label_lit)
      # label_1.pack()
      # label_lit.set("Test of Label")

      # label_2 =  Label(self.top, textvariable=self.str_1)
      # label_2.pack()
      #
      # label_3 =  Label(self.top, textvariable=self.int_lit)
      # label_3.pack()
      # self.int_lit.set(self.int_ctr)
      #
      # entry_1 =  Entry(self.top, textvariable=self.str_1)
      # entry_1.pack()
      # self.str_1.set("Entry Initial Value")

      ##---  Delete the contents of an entry widget
      ## entry.delete(0,END)

      # print_button =  Button(self.top, text='PRINT CONTENTS',
      #                               command=self.getit, bg='blue', fg='white')
      # print_button.pack(fill= X, expand=0)
      #
      # exit_button =  Button(self.top, text='EXIT',
      #                              command=self.top.quit, bg='red', fg='white')
      # exit_button.pack(fill= X, expand=1)
      #
      # entry_1.focus_set()
      #


   def run(self):
      self.top.mainloop()
   ##-----------------------------------------------------------------
   def changeNoOfFrames(self,e):
      self.settings.movementTime=self.NoOfFrames.get()
   def changeThreshold(self,e):
      self.settings.thresholdLimit=self.threshold.get()
   def changeMaxMovement(self,e):
      self.settings.movementMaximum=self.MaxMovement.get()
   def changeMinMovement(self,e):
      self.settings.movementMinimum=self.MinMovement.get()
   def changeDilation(self,e):
      self.settings.dilationPixels=self.dilation.get()
   def changeMinArea(self,e):
      self.settings.minArea=self.minarea.get()*self.minarea.get()
   def changeBlur(self):
      self.settings.useGaussian=self.blur.get()
      if self.blur.get() == 0:
         for w in self.blur_box.winfo_children():
            w.configure(state='disabled')
      elif self.blur.get() == 1:
         for w in self.blur_box.winfo_children():
            w.configure(state=NORMAL)
   def changeblur_pixel(self,e):
       if not self.blur_pixel.get() % 2:
           self.blur_pixel.set(self.blur_pixel.get()+1)
       self.settings.gaussianPixels=self.blur_pixel.get()
   def bs_fliper(self):
      # self.bs_box.state(['!alternate'])
      self.settings.bsMethod=self.bs_var.get()
      if self.bs_var.get()==0:
         for w in self.bs_box.winfo_children():
            w.configure(state='disabled')
      elif self.bs_var.get()==1:
         for w in self.bs_box.winfo_children():
            w.configure(state=NORMAL)
   def bs_changeLearningrate(self,e):
      self.settings.MOG2learningRate=self.bs_learningrate
   def bs_changeHist(self,e):
      self.settings.MOG2history=self.bs_learningrate
   def bs_shadowfliper(self):
      self.settings.MOG2shadow = self.bs_shadow
   def bs_changeThresh(self,e):
      self.settings.MOG2thresh = self.bs_threshold

##===============================================================
# if "__main__" == __name__:
#    ET = EntryTest()
#    ET.top.mainloop()
   # print("under __main__ =", ET.str_1.get())
   # print("uzair")
   # ET.join()