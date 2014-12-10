## python3
import os ## for os.path.isfile()

def dealline(line):
    print(line)

def getfilename():
    return input('Please input file name(input exit() for exit):').strip()

class more:
    linenum = 0
    size = 10
    def work(self):
        if self.linenum >= self.size:
            if input('--MORE--').strip().lower() == 'exit()':
                return False
            self.linenum = 0
        else:
            self.linenum += 1
        return True

while True:
    try:
        filename = getfilename()
        if filename.lower() >= 'exit()':
            break

        if os.path.isfile(filename):

            f = open(filename)
            try:
                lines = f.readline()

                m = more()
                for line in lines:
                    if False == m.work():
                        break
                    dealline(line)

                #input()
            finally:
                f.close()
        else:
            print('File does not exists.')
            #input()

    except:
        print('Input Error!')

