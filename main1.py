import time
import winsound
from tkinter import messagebox

from pycaw.pycaw import AudioUtilities
from pygame import mixer


def virus():
    # Display Virus messageBox
    messagebox.showerror("Error System32", "You have been infected with a virus!")
    time.sleep(1)
    messagebox.showerror("Error System32", "Your files are being deleted!")
    time.sleep(0.5)
    messagebox.showwarning("Warning", "You need To Shut Down Your Computer!")
    time.sleep(0.5)
    messagebox.showwarning("Warning", "Its not a joke!!!!!")

    # Play a sound to alert the user
    time.sleep(0.5)
    for i in range(10):
        winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        if i == 5:
            mixer.init()

            messagebox.showerror("Error System32", "Shut Down Your computer")
            time.sleep(0.5)
            devices = AudioUtilities.GetSpeakers()
            volume = devices.EndpointVolume

            target_volume = float(1)
            target_volume = max(0.0, min(1.0, target_volume))

            volume.SetMasterVolumeLevelScalar(target_volume, None)

            mixer.music.load("Virus in Python/video.mp3")
            mixer.music.set_volume(1.0)
            mixer.music.play()

            messagebox.showinfo("Info", "Your Computer Has Been Hacked")
            messagebox.showwarning("Wrning", "Your Computer Shut Down in 10 sec!!!")

            for x in range(9):
                winsound.Beep(1000, 1000)

if __name__ == "__main__":
    virus()
