import subprocess
import os

print("Adjusting videos...")

for filename in os.listdir("./raw"):
    if filename.endswith(".mp4"):
        if filename not in os.listdir("./clean"):
            subprocess.call(
                "ffmpeg -i ./raw/"
                + filename
                + " -vf scale=480:270 -c:v libvpx-vp9 -crf 30 -b:v 1024k ./clean/"
                + filename,
                shell=True
            )

            os.remove("./raw/" + filename)

        else:
            os.remove("./raw/" + filename)
