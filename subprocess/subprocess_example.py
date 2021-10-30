import subprocess

ps = subprocess.run(args="wmic cpu", stdout=subprocess.PIPE)
print(ps.stdout.decode("utf-8"))


