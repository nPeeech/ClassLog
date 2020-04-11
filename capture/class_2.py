import datetime
import sys
import subprocess

wkday = datetime.date.today().weekday()
today = datetime.datetime.today().strftime("%Y_%m_%d")

if wkday == 0:
    f_name = "kokugo"
elif wkday == 1:
    f_name = "rinri"
elif wkday == 2:
    f_name = "bunsyo"
elif wkday == 3:
    f_name = "gw"
elif wkday == 4:
    sys.exit()

cmd = "/usr/local/bin/ffmpeg -f alsa -thread_queue_size 4096 -i plughw:1,0 -f v4l2 -thread_queue_size 4096 -s 1920x720  -itsoffset 0.5 -i /dev/video0 -vf eq=brightness=0.25:saturation=2.5 -t 5400 -c:v h264_omx -b:v 640k -c:a aac -b:a 128k -r 1 /home/pi/mnt/Class_Log/" + today + "/" + f_name + ".mp4"

subprocess.run(cmd.split())