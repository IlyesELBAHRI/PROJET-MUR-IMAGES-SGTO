import subprocess
import os

print("Adjusting images...")

for filename in os.listdir("./raw"):
    if filename.endswith(".png"):
        if filename not in os.listdir("./clean"):
            subprocess.call("ffmpeg -loop 1 -i ./raw/" + filename +
                            " -c:v libx264 -t 5 -pix_fmt yuv420p -vf scale=1920:1080 " + "./clean/" + filename[:-4] + ".mp4", shell=True)

            os.remove("./raw/" + filename)

        else:
            os.remove("./raw/" + filename)
