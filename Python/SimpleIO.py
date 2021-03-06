from sys import stderr, stdout, stdin, exit
import sys


class SimpleIO:
    def __init__(self, *args, **argv):
        self.__LOCAL__ = True if ('LOCAL' in sys.argv) else False
        self.local_ifname = "input.txt"
        self.local_ofname = ""
        self.nonlocal_ifname = ""
        self.nonlocal_ofname = ""

        self.ifile = -1
        self.ofile = -1

        if 'LocalDirective' in argv.keys():
            self.__LOCAL__ = True if (argv['LocalDirective'] in sys.argv) else False

        if ('open' in argv.keys()) and (argv['open']):
            ifname = self.local_ifname if self.__LOCAL__ else self.nonlocal_ifname
            ofname = self.local_ofname if self.__LOCAL__ else self.nonlocal_ofname
            self.ifile = stdin if ifname == '' else open(ifname, 'r')
            self.ofile = stdout if ofname == '' else open(ofname, 'w')
            self.reader = self.__new_reader__()

    def reset_local(self, ifname: str, ofname: str):
        self.local_ifname = ifname
        self.local_ofname = ofname
        if self.__LOCAL__:
            self.ifile = stdin if ifname == '' else open(ifname, 'r')
            self.reader = __new_reader__()
            self.ofile = stdout if ofname == '' else open(ofname, 'w')
        return self

    def reset_nonlocal(self, ifname: str, ofname: str):
        self.nonlocal_ifname = ifname
        self.nonlocal_ofname = ofname
        if not self.__LOCAL__:
            self.ifile = stdin if ifname == '' else open(ifname, 'r')
            self.reader = self.__new_reader__()
            self.ofile = stdout if ofname == '' else open(ofname, 'w')
        return self

    def __new_reader__(self, ):
        buf = ''
        while(True):
            inp = self.ifile.read(1024)
            for c in inp:
                if c in ' \t\v\n':
                    if(len(buf) > 0):
                        yield buf
                    buf = ''
                    continue
                buf += c

    def print(self, *args, sep=' ', end='\n'):
        if(len(args) == 1):
            self.ofile.write(args[0] + end)
            return

        self.ofile.write(str(args[0]))
        for x in args:
            self.ofile.write(sep + str(x))
        self.ofile.write(end)

    def next_token(self, ):
        return self.reader.__next__()

    def __exit__(self, ):
        self.ifile.close()
        self.ofile.close()


def main():
    io = SimpleIO(open=True)
    io.print(io.next_token())
    del io

    io = SimpleIO().reset_local('', 'memes.out').reset_nonlocal('', 'hehclassic.out')
    io.print('Eeee, memes')
    del io

if __name__ == '__main__':
    main()
