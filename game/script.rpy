## The script of the game goes in this file.

## Declare characters used by this game. The color argument colorizes the name
## of the character.

#character

#eksepresi arthur
image arthur_normal = "characters/arthur/Arthur-normal.png"
image arthur_normal cropped = LiveCrop((0, 0, 350, 650), "arthur_normal")

image arthur_senyum = "characters/arthur/Arthur-senyum.png"
image arthur_senyum cropped = LiveCrop((0, 0, 350, 650), "arthur_senyum")

image arthur_kaget = "characters/arthur/Arthur-kaget.png"
image arthur_kaget cropped = LiveCrop((0, 0, 350, 650), "arthur_kaget")

image arthur_terkejut = "characters/arthur/Arthur-terkejut.png"
image arthur_terkejut cropped = LiveCrop((0, 0, 350, 650), "arthur_terkejut")

image arthur_segan = "characters/arthur/Arthur-segan.png"
image arthur_segan cropped = LiveCrop((0, 0, 350, 650), "arthur_segan")

image arthur_segan2 = "characters/arthur/Arthur-segan2.png"
image arthur_segan2 cropped = LiveCrop((0, 0, 350, 650), "arthur_segan2")

image arthur_sedih = "characters/arthur/Arthur-sedih.png"
image arthur_sedih cropped = LiveCrop((0, 0, 350, 650), "arthur_sedih")


#ekspresi ivan

#school uniform
image ivan_normal = "characters/ivan/Ivan-normal.png"
image ivan_normal cropped = LiveCrop((0, 0, 350, 650), "ivan_normal")

image ivan_senyum = "characters/ivan/Ivan-senyum.png"
image ivan_senyum cropped = LiveCrop((0, 0, 350, 650), "ivan_senyum")

image ivan_tablo = "characters/ivan/Ivan-tablo.png"
image ivan_tablo cropped = LiveCrop((0, 0, 350, 650), "ivan_tablo")

image ivan_kesel = "characters/ivan/Ivan-kesel.png"
image ivan_kesel cropped = LiveCrop((0, 0, 350, 650), "ivan_kesel")

image ivan_marah = "characters/ivan/Ivan-marah.png"
image ivan_marah cropped = LiveCrop((0, 0, 350, 650), "ivan_marah")

image ivan_kaget = "characters/ivan/Ivan-kaget.png"
image ivan_kaget cropped = LiveCrop((0, 0, 350, 650), "ivan_kaget")

image ivan_sebel = "characters/ivan/Ivan-sebel.png"
image ivan_sebel cropped = LiveCrop((0, 0, 350, 650), "ivan_sebel")

image ivan_ngeledek = "characters/ivan/Ivan-ngeledek_resize.png"
image ivan_ngeledek cropped = LiveCrop((0, 0, 350, 650), "ivan_ngeledek")

image ivan_bersiul = "characters/ivan/Ivan-siul.png"
image ivan_bersiul cropped = LiveCrop((0, 0 ,350, 650), "ivan_bersiul")



#kasual
#image ivan


#ekspresi karin
image karin = "characters/karin/karin_resize.png"
image karin cropped = LiveCrop((0, 0, 350, 650), "karin")


image karin_kesel = "characters/karin/karin-kesel_resize.png"
image karin_kesel cropped = LiveCrop((0, 0, 350, 650),"karin_kesel")




#backgrounds
image bg jalanan = "backgrounds/jalanan.jpg"

image bg koridor = "backgrounds/koridor.jpg"

image bg tangga = "backgrounds/tangga.jpg"

image bg kelas = "backgrounds/kelas.jpg"

image bg kamar ivan = "backgrounds/kamar-iivan.jpg"

image bg pemakaman = "backgrounds/pemakaman.jpg"

image bg tangga = "backgrounds/tangga.jpg"

image bg rumah_sakit = "backgrounds/rumah-sakit.jpg"

image bg apartemen = "backgrounds/apartemen.jpg"


#event
image lisa_cg = "events/cg.jpg"

image vas_bunga = "events/vas2.jpg"

image dinding_ivan = "backgrounds/dinding_ivan.jpg"
#image vas_bunga cropped = LiveCrop((0, 0, 200, 400), "vas_bunga")




#initialize music

#sound effect
define audio.opendoor_morning = "sfx/door.wav"
define audio.walking_morning = "sfx/steps.wav"
define audio.birds = "sfx/birds.wav"
define audio.walking_fast = "sfx/faststeps.wav"
define audio.hit_body = "sfx/hit1.wav"
define audio.outside_door = "sfx/outsidedooropen.wav"
define audio.classbell = "sfx/classbell.wav"
define audio.shokku = "sfx/shokku.wav"
define audio.slap = "sfx/slap.wav"


#backgroudn music
define audio.apartemen = "music/apatemen.mp3"
define audio.belakang_sekolah = "music/belakang.mp3"
define audio.kelas = "music/kelas.mp3"
define audio.koridor_sekolah = "music/koridor.mp3"
define audio.mainmenu_sound = "music/mainmenu.mp3"
define audio.prolog = "music/prolog.mp3"





#logic position

#posisi untuk kiri
transform my_left:
    xalign .3 yalign 1.0


#posisi untuk kanan
transform my_right:
    xalign .6 yalign 1.0




#posisi sembuyi
transform sembunyi_1:
    xalign .6 yalign 1.0

transform sembunyi_2:
    xalign .9 yalign 1.0



#posisi vas bunga jatuh
transform vas_center:
    xalign .5 yalign 0.6





#posisi berkumpul -> bagian kiri
transform posisi_kiri:
    xalign .2 yalign 1.0


#posisi berkumpul -> bagian kanan
transform posisi_kanan:
    xalign .8 yalign 1.0



#for dialog jauh
#image karin_far cropped = LiveCrop((0, 0, 540, None), "karin")


image arthur_normal small = im.Scale("Arthur-normal.png", 270, 550)

image karin small = im.Scale("karin.png", 223.936, 512)








# declare the character

#main karakter

define l = Character('Lisa', color="#EB3E8F")
define a = Character('Arthur', color="#CD4021")

define i = Character('Ivan', color="#1CA6D5")
define k = Character('Karin', color="#ECCF2B")

#karakter pembantu
define c = Character('Cewek A', color="#EC2E42")
define g = Character('Pak Andi', color="#55DF4A")
define s = Character('Suster')


define child = Character('Gadis Mungil')
define man = Character('Another Man')


#conditional
define anonim = Character('???')



#shake effetct
init python:

    import math

    class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)

        return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

    Shake = renpy.curry(_Shake)



## The game starts here.

label start:

    #scene bg jalanan with fade

    

    ## This shows a character sprite. A placeholder is used, but you can replace
    ## it by adding a file named "eileen happy.png" to the images directory.

    ## These display lines of dialogue.

    jump start_prolog