import subprocess
import pygetwindow as gw
import time

# Function to open apps
def open_apps():
    # Paths to the applications
    obsidian_path = r"C:\Users\sabar\AppData\Local\Obsidian\Obsidian.exe"
    spotify_path = r"C:\Users\sabar\AppData\Roaming\Spotify\Spotify.exe"
    vscode_path = r"C:\Users\sabar\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    # Open the applications
    subprocess.Popen([obsidian_path])
    subprocess.Popen([spotify_path])
    subprocess.Popen([vscode_path])
    subprocess.Popen([brave_path])

    # Allow some time for windows to open before arranging them
    time.sleep(5)  # Adjust delay as needed based on your system speed and how quickly apps launch

# Function to arrange windows
def arrange_windows():
    # Monitor resolutions
    portrait_res = (1080, 1920)  # 27" portrait monitor
    landscape_res = (3440, 1440)  # 34" landscape monitor

    # Get window objects
    obsidian_win = next((w for w in gw.getWindowsWithTitle('Obsidian')), None)
    spotify_win = next((w for w in gw.getWindowsWithTitle('Spotify')), None)
    vscode_win = next((w for w in gw.getWindowsWithTitle('Visual Studio Code')), None)
    brave_win = next((w for w in gw.getWindowsWithTitle('Brave')), None)

    # Position and resize windows
    if obsidian_win:
        obsidian_win.moveTo(0, 0)  
        obsidian_win.resizeTo(portrait_res[0], portrait_res[1] // 2) 

    if spotify_win:
        spotify_win.moveTo(0, portrait_res[1] // 2)
        spotify_win.resizeTo(portrait_res[0], portrait_res[1] // 2) 

    if vscode_win:
        vscode_win.moveTo(portrait_res[0], 0)
        vscode_win.resizeTo(landscape_res[0] // 2, landscape_res[1]) 

    if brave_win:
        brave_win.moveTo(portrait_res[0] + landscape_res[0] // 2, 0) 
        brave_win.resizeTo(landscape_res[0] // 2, landscape_res[1])

def main():
    open_apps()
    arrange_windows()

if __name__ == "__main__":
    main()