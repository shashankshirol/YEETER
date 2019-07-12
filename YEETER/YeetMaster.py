import urllib.request
import requests
from random import randrange

def FancyYeeter(length = 2, times = 1, upper_case = False):
    url = 'http://artii.herokuapp.com/make?'

    #FONTS
    fonts = ['sbookb', 'hollywood', 'clr7x8', 'cosmic', 'coinstak', 'ogre', 'cli8x8', 'xhelvi', 'charact1', 'charact2', 'charact3',
    'charact4', 'charact5', '3-d', '5lineoblique', 'bubble__', 'new_asci', 'roman', 'script__', 'alligator', 'alligator2', 'avatar', 'banner3-D',
    'barbwire', 'marquee', 'nipples', 'pebbles', 'rectangles', 'rozzo', 'rev', 'sblood', 'slant', 'small', 'short', 'stacey', 'stop', 'thin',
    'usaflag', 'weird', 'whimsy']
    
    #MAKING YEET(s)
    if length<2:
        length = 2
    if times<1:
        times = 1
    e = 'e'*length
    yeet_p = 'y'+e+'t'
    yeet_p = yeet_p*times
    if(times>1):
        yeet_p = yeet_p.replace('t', 't-')
        yeet_p = yeet_p[:-1]
    if(upper_case):
        yeet_p = yeet_p.upper()
    
    #SELECTING A RANDOM YEET FONT
    font_id = randrange(len(fonts))

    #FINALIZING the URL
    url = url+'text='+yeet_p+'&font='+fonts[font_id]

    #GETTING YEET(s)
    YEET_text = urllib.request.urlopen(url).read()
    YEET_output = YEET_text.decode('utf-8')

    print(YEET_output)


def NormalYeeter(length = 2, times = 1, upper_case = False):
    #MAKING YEETS
    if length<2:
        length = 2
    if times<1:
        times = 1
    e = 'e'*length
    yeet_p = 'y'+e+'t'
    yeet_p = yeet_p*times
    if(times>1):
        yeet_p = yeet_p.replace('t', 't-')
        yeet_p = yeet_p[:-1]
    if(upper_case):
        yeet_p = yeet_p.upper()
        
    print(yeet_p)