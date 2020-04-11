import datetime
import sys
import subprocess

wkday = datetime.date.today().weekday()
today = datetime.datetime.today().strftime("%Y_%m_%d")

if wkday == 0:
    f_name = "sugaku"
elif wkday == 1:
    sys.exit()
elif wkday == 2:
    f_name = "sugaku"
elif wkday == 3:
    f_name = "kagaku"
elif wkday == 4:
    f_name = "sugaku"

cmd = "/usr/local/bin/ffmpeg -f alsa -thread_queue_size 4096 -i plughw:1,0 -f v4l2 -thread_queue_size 4096 -s 1920x720  -itsoffset 0.5 -i /dev/video0 -vf eq=brightness=0.25:saturation=2.5 -t 5400 -c:v h264_omx -b:v 640k -c:a aac -b:a 128k -r 1 /home/pi/mnt/Class_Log/" + today + "/" + f_name + ".mp4"

subprocess.run(cmd.split())