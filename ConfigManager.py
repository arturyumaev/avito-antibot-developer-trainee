class ConfigManager():
    def __init__(self):
        self.configName = "./conf.ini"
        self.unlimAccessNetworksName = "./unlimAccessNetworks.ini"

    def readConfig(self):
        try:
            self.config = open(self.configName, "r")
            self.configuration = self.config.readlines()
            
            self.NREQ           = int(self.configuration[0][5:-1])
            self.TIME_RANGE_SEC = int(self.configuration[1][15:-1])
            self.TIME_LOCK_SEC  = int(self.configuration[2][14:-1])

        except IOError:
            print("An error occured while reading configuration file", self.configName)
            self.NREQ = 100
            self.TIME_RANGE_SEC = 60
            self.TIME_LOCK_SEC = 120
            print("Configuration was set to default settings")
        else:
            self.config.close()
        finally:
            return self.NREQ, self.TIME_RANGE_SEC, self.TIME_LOCK_SEC


    def getUnlimAccessNetworks(self):
        try:
            f = open(self.unlimAccessNetworksName, "r")
            netsRaw = f.readlines()

            if len(netsRaw) != 0:
                self.networks = [net[:-1] if net[-1:] == '\n' else net for net in netsRaw]
            else:
                self.networks = []

        except IOError:
            print("An error occured while reading network file", self.unlimAccessNetworksName)
            self.networks = []
            print("Network file configuration was set to default settings")
        else:
            f.close()
        finally:
            return self.networks
