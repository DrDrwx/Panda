# Author  : @DivorcedRSAKey
# Purpose : This library was designed to keep me from rewriting all my code constantly
#           for different projects.
# Version : Puddle (0.6.6)

import sys
calling_file = sys.argv[0].split(".py")[0]
if calling_file == "":
    calling_file="panda"

class Logger():
    def __init__(self, logFile="%s.log" % calling_file, verbose=True, write=True, debug=True):
        self.strf = "[%Y-%m-%d %H:%M:%S]"
        self.types = {
            "error": "[!]",
            "info": "[-]",
            "plus": "[+]",
            "debug": "[D]",
            "warn": "[W]"
            }
        self.verbose = verbose
        self.write = write
        self.logFile = logFile
        self.debugger=debug

    def log(self, logMsg, logType='info', verbose=True, write=True):
        from time import strftime as s, gmtime as g
        log = "%s %s %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(self.logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def success(self, logMsg, logType='plus', verbose=True, write=True):
        from time import strftime as s, gmtime as g
        log = "%s %s Success: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(self.logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def error(self, logMsg, logType='error', verbose=True, write=True):
        from time import strftime as s, gmtime as g
        log = "%s %s Error: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(self.logFile, "a")
            lf.write(log+"\n")
            lf.close()

    def debug(self, logMsg, logType='debug', verbose=True, write=True):
        if self.debugger:
            from time import strftime as s, gmtime as g
            log = "%s %s Debug: %s" % (s(self.strf, g()), self.types[logType], logMsg)
            if self.verbose and verbose:
                print log
            if self.write and write:
                lf = open(self.logFile, "a")
                lf.write(log+"\n")
                lf.close()

    def warning(self, logMsg, logType='warn', verbose=True, write=True):
        from time import strftime as s, gmtime as g
        log = "%s %s Warning: %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose and verbose:
            print log
        if self.write and write:
            lf = open(self.logFile, "a")
            lf.write(log+"\n")
            lf.close()

