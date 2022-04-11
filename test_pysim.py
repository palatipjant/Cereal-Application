
import PySimpleGUI as sg

bg = "img/"

time = 5000

sg.Window("Cereal",[[sg.Image(bg)]],transparent_color=sg.theme_background_color(),no_titlebar=True,keep_on_top=True).read(timeout=time,close=True)



