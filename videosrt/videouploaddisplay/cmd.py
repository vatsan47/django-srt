import subprocess

def srt(video):
    print(subprocess.check_call(['wsl', 'ccextractor', video]))