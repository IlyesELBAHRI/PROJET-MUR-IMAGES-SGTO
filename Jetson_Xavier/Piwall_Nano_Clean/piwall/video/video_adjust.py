import subprocess
import os

print("Adjusting videos...")

for filename in os.listdir("./raw"):
    if filename.endswith(".mp4"):
        if filename not in os.listdir("./clean"):
            subprocess.call("ffmpeg -i ./raw/" + filename +
                            " -b:v 1024k -filter:v fps=25 " + "./clean/" + filename, shell=True)

            os.remove("./raw/" + filename)

        else:
            os.remove("./raw/" + filename)
