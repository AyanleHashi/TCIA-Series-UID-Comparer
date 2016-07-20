import Tkinter as tk
import os

class TK(tk.Frame):
    
    output = []
    
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.label = tk.Label(root, text='Carefully type the file location here').pack()
        self.button = tk.Button(self, text='Print Value',
                                command=self.button_print).pack()
        self.entry = tk.Entry(root)
        self.entry.pack()

    def button_print(self):
        get = self.entry.get()
        for (path, dirs, files) in os.walk(get, topdown=True):
            if not dirs:
                self.output.append(os.path.basename(path))
        print self.output

def main():
    root = tk.Tk()
    TK(root).pack()
    root.mainloop()

if __name__ == '__main__':
    main()