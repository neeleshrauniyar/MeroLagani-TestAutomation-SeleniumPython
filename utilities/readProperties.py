import configparser, os

config= configparser.RawConfigParser()
config.read(os.path.dirname(os.getcwd())+"//configurations//config.ini")
# config.read("/Users/neeleshrauniyar/PycharmProjects/MeroLagani/configurations/config.ini")

class ReadProperties:
    config = configparser.RawConfigParser()
    config.read(os.path.dirname(os.getcwd()) + "//configurations//config.ini")
    @staticmethod
    def readBaseURL():
        url= config.get('commonInfo', 'baseURL')
        return url

print(ReadProperties.readBaseURL())
