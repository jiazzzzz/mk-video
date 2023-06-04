from moviepy import editor
from moviepy.editor import *


class genVideo:
    def __init__(self, txt_file, title, content_duration, audio_file, font="./font/cj.ttf", title_duration=5, size=(1920,1080), output_file="./output/output.mp4") -> None:
        self.font = font
        self.title_duration = title_duration
        self.txt_file = txt_file
        self.size = size
        self.title = title
        self.content_duration = content_duration
        self.audio_file = audio_file
        self.output_file = output_file

    def gen_video(self):
        clip = self.__bg_clip__(self.size)
        inf = self.__get_txt__(self.txt_file)

        t_clip = self.__title_clip__(self.title)
        t_clip.set_start(clip.end)

        txtclip = TextClip(inf, font=self.font, fontsize=30, color='black', bg_color='white', transparent=True)\
            .set_duration(self.content_duration ).resize((clip.size[0], clip.size[1]*10)).set_fps(24)
        
        w = None
        h = clip.size[1]
        x_speed = x_start = 0
        y_start = -100
        y_speed = 55
        txtclip = txtclip.fx(vfx.scroll, w, h, x_speed, y_speed, x_start, y_start).set_start(t_clip.end)
        audio_clip = editor.AudioFileClip(self.audio_file)
       
        newclip = CompositeVideoClip([txtclip,clip,t_clip], bg_color=(255, 255, 255), ismask=False)
        newclip = newclip.set_audio(audio_clip)
        newclip.write_videofile(self.output_file, threads=8)


    def __bg_clip__(self, size, color=(255,255,255)):
        return ColorClip(size, color, duration=0)

    def __title_clip__(self, title, duration=5, size=(1920,1080)):
        return TextClip(title, font=self.font, fontsize=60, color='black', method="caption", align="center", size=(1920, 1080), bg_color='white', transparent=True)\
            .set_duration(duration).resize(size).set_fps(24)

    def __get_txt__(self, txt_file):
        with open(txt_file, 'r', encoding='utf-8') as f:
            return f.read()        

if __name__=='__main__':
    txt_file = "./txt/1.txt"
    title = "孩子学习不好根本原因是什么"
    content_duration = 220
    audio_file = "./audio/LindseyStirling-TheArena.mp3"
    font = "./font/ThePeakFont.ttf"

    t = genVideo(txt_file, title, content_duration, audio_file, font=font)
    t.gen_video()