import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.core.window import Window
import kivy.properties as kp
# from kivy.properties import NumericProperty
import random as rd
import numpy as np
import colorsys
#TODO: GENERATE ARRAY w/ random hsv values
#TODO: Animate boxes according to specific sorting algorithms
class CornerRectangleWidget(Label):
    pass

class MainBody(GridLayout):
    rows = 2
    arrSize = 50

    def displayArr(self, arr):
        self.ids.BoxL.clear_widgets()
        for i in range(len(arr)):
            l = CornerRectangleWidget()
            l.id = f'l{i}'
            self.ids.BoxL.add_widget(l)
            l.size_hint_y = None
            l.height = int(arr[i])

    def sortArr(self):
        return np.sort(self.getarr())

    def swap_stack(self, s1, s2):
        anim1 = Animation(pos=s2.pos, duration=.1)
        anim2 = Animation(pos=s1.pos, duration=.1)
        anim1.start(s1)
        anim2.start(s2)

    def sort_bubble(self, arr):
        for _ in range(len(arr), 0, -1):
            for j in range(len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.swap_stack(self.ids[f'l{j}'], self.ids[f'l{j+1}'])
        return arr

    def sort_merge(self, arr):
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.sort_merge(L)
            self.sort_merge(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1

            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1

            while j < len(R):
                arr[k] = R[j]
                j+=1
                k+=1
        return arr

    def changecolor(self):
        l = self.ids['l0']
        print(l.height)

    def gen_rd_arr(self):
        self.rdarr = list(np.random.randint(1,500,self.arrSize))

    def getarr(self):
        return self.rdarr[:]

class AnimationApp(App):

    def build(self):

        return MainBody()



    def moveBtn(self, instance):
        anim = Animation(size=(rd.randint(80, 200), rd.randint(80, 200)), duration=.1)
        anim &= Animation(pos=(rd.randint(0, self.width-instance.width), rd.randint(0, self.height-instance.height)), duration=.1)
        anim.start(instance)




if __name__ == '__main__':
    AnimationApp().run()