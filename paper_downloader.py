from scihub import SciHub
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

class App:
    def __init__(self, root):
        frame = tk.Frame(root)
        label = tk.Label(frame, text="Enter paper identifier (DOI, PMID, URL): ")
        label.pack()
        self.inp = tk.StringVar(root)
        entry = tk.Entry(frame, textvariable=self.inp, justify=tk.CENTER)
        entry.pack(fill=tk.X)
        button = tk.Button(frame, text="Download", command=self.download)
        button.pack()
        self.status = tk.Label(frame, text="")
        self.status.pack()
        frame.pack(expand=True, fill=tk.X)
        self.sh = SciHub()

    def say(self, text):
        self.status.config(text=text)

    def download(self):
        inp = self.inp.get()
        self.say("Attempting to download paper...")
        out = self.sh.fetch(inp)
        if 'err' in out:
            self.say("There was an error downloading that paper.")
            return
        self.say("Paper successfully downloaded.")
        fname = asksaveasfilename(title="Save your paper.", defaultextension=".pdf")
        if fname is None:
            self.say("No file selected; paper not saved.")
            return
        try:
            f = open(fname, "xb")
            f.write(out["pdf"])
            f.close()
        except IOError:
            self.say("There was an error saving the paper.")
            return
        self.say(f"Paper successfully saved as {fname}.")

def main():
    root = tk.Tk()
    root.title("Paper Downloader")
    root.geometry("600x480")
    app = App(root)
    root.mainloop()
        
if __name__ == "__main__":
    main()
