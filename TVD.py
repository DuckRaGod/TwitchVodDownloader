import os
from twitchdl import twitch

print("Hello, To twitch vod downloader")



f = open("vod.txt", "r")
lines = []

while(True):
    line = f.readline()
    line = line.replace('\n','')
    if not line:
        break
    lines.append(line)
f.close

if(len(lines) < 5):
    print('Err')
    quit()

video = twitch.get_video(lines[0])
save_path = lines[1]
start_time = lines[2]
end_time = lines[3]
save_name = lines[4]

print(video.get("title"))
print(save_path)
print(start_time)
print(end_time)
print(save_name)

os.system("twitch-dl download " + lines[0] + " -s " + start_time + " -e " + end_time +" -o "+ save_path + save_name)