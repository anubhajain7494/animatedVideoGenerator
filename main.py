import os
import subprocess

# Define your parameters
cookie_value = "1p0lRX0AjjByPX18v8Thm2q2gmaqQ72Fh1iv_DY7jDiM6TY5AwG25vQZPbztsS32FB_ykhexAo-ovUAwp1ul0VIOsackAWgND-mOHipcTHiYLwSwdyyl3ZbhrkqrRpq_VZhl3owNz821jzQ61zGV1nWhCaekik9Yl3iwcxGLLJbYhYm7KAVE_5CqxK2n5fePZxMUUt9naVpTBNDHKZDVBneXMVdACorsDrpWayf5S9i8"
output_folder = r"C:\Z004DM5R\Test\Bing-Dalle\Downloaded Images"
prompts = [
    "A young boy riding an elephant in the jungle. The scene is filled with vibrant colors and magical lights.",
    "A futuristic city skyline at night. Neon lights reflecting on wet streets, cyberpunk aesthetics.",
    "A dragon flying over a medieval castle. Fire-breathing and surrounded by dark storm clouds."
]

for prompt in prompts:
    command = [
        "python", "-m", "bingdalle",
        prompt, "-c", cookie_value, "-o", output_folder
    ]

    subprocess.run(command, shell=True)
