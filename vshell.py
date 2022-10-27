import os


class Vshell:
    ''' Constructor '''
    def __init__(self, img):
        self.cf = "/"
        self.image = img

    ''' "ls" command '''
    def _ls(self):
        if self.cf == "/":
            for name in self.image.namelist():
                if "/" not in name:
                    print(name)
                elif "." not in name and "/" not in name[:-1]:
                    print(name[:-1])
        else:
            for name in self.image.namelist():
                if self.cf[1:] in name and self.cf[1:] != name:
                    if "/" not in name[len(self.cf) - 1:]:
                        print(name[len(self.cf) - 1:])
                    elif "." not in name[len(self.cf) - 1:] and "/" not in name[len(self.cf) - 1:-1]:
                        print(name[len(self.cf) - 1:-1])

    ''' "cd" command '''
    def _cd(self, folder):
        if "/" == folder[0] and len(folder) == 1 or folder == "~":
            self.cf = "/"
        elif folder[0] == "-" and len(folder) == 1 or folder[0] == "." and folder[1] == "." and len(folder) == 2:
            if self.cf == "/":
                if folder[0] == "-":
                    self._pwd()
            else:
                i = len(self.cf) - 1
                while self.cf[i - 1] != "/":
                    i -= 1
                self.cf = self.cf[:i]
                if folder[0] == "-":
                    self._pwd()
        elif "/" == folder[0]:
            for name in self.image.namelist():
                if folder[1:] in name:
                    self.cf = folder + "/"
                    break
            else:
                print("can't cd to " + folder + ": No such file or directory")
        else:
            for name in self.image.namelist():
                if (self.cf + folder)[1:] == name[:-1]:
                    self.cf = self.cf + folder + "/"
                    break
            else:
                print("can't cd to " + folder + ": No such file or directory")

    ''' "pwd" command '''
    def _pwd(self):
        if "/" == self.cf:
            print("/")
        else:
            print(self.cf[:-1])

    ''' "cat" command '''
    def _cat(self, f):
        for file in self.image.infolist():
            if self.cf[1:] + f in file.filename or f[0] == "/" and f[1:] in file.filename or self.cf == "/" and f == file.filename:
                byte_text = self.image.read(file)
                print(byte_text.decode('utf-8'))
                break
        else:
            print("can't open " + f + ": No such file or directory")

    ''' "exit" command '''
    def _exit(self):
        exit()

    ''' "clear" command '''
    def _clear(self):
        os.system('cls')

    '''  Infinite loop '''
    def exec(self):
        while True:
            if self.cf == "/":
                print(os.getlogin() + ":~" + "$", end=" ")
            else:
                print(os.getlogin() + ":~" + self.cf[:-1] + "$", end=" ")
            command = input()
            if " " in command:
                command, folder = command.split(" ", 1)
            if command == "ls":
                self._ls()
            elif command == "pwd":
                self._pwd()
            elif command == "exit":
                self._exit()
            elif command == "clear":
                self._clear()
            elif command == "cat":
                self._cat(folder)
            elif command == "cd":
                self._cd(folder)
            else:
                print(command + ": not found")
