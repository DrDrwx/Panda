# Author  : @DivorcedRSAKey
# Purpose : This library was designed to keep me from rewriting all my code constantly
#           for different projects.
# Version : Mud (0.3.1)

def logger(logMsg, logType="info", logFile="panda.log", verbose=True, write=False):
    from time import strftime as s, gmtime as g
    strf = "[%Y-%M-%d %H:%M%:%S]"
    logTypes = {
            "error": "[!]",
            "info": "[-]",
            "plus": "[+]"
            }
    log = "%s %s %s" % (s(strf, g()), logTypes[logType], logMsg)
    if verbose:
        print log
    if write:
        lf = open(logFile, "a")
        lf.write(log+"\n")
        lf.close()

class Logger():
    def __init__(self, logFile="panda.log", verbose=False, write=False):
        self.strf = "[%Y-%M-%d %H:%M:%S]"
        self.types = {
            "error": "[!]",
            "info": "[-]",
            "plus": "[+]"
            }
        self.verbose = verbose
        self.write = write
        self.logFile = logFile

    def log(self, logMsg, logType='info', write=True):
        from time import strftime as s, gmtime as g
        log = "%s %s %s" % (s(self.strf, g()), self.types[logType], logMsg)
        if self.verbose:
            print log
        if self.write:
            if write:
                lf = open(self.logFile, "a")
                lf.write(log+"\n")
                lf.close()
