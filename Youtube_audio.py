from pytube import YouTube

video_link = ['https://www.youtube.com/watch?v=0HQqXllXpfQ',
            'https://www.youtube.com/watch?v=mA7tcDryYDU&t=567s',
            'https://www.youtube.com/watch?v=qHp2ooJxJRs',
            'https://www.youtube.com/watch?v=4s34XjQFBjg&t=2566s',
            'https://www.youtube.com/watch?v=nf-TSiYNd48',
            'https://www.youtube.com/watch?v=hF7O9c_Kdoc']

for v in video_link:
    yt = YouTube(v)
    # audio = yt.streams.get_by_itag('140')
    audio = yt.streams.filter(only_audio=True).first()
    audio.download()

yt = YouTube(video_link[0])
audio = yt.streams.filter(only_audio=True).all()