from twisted.internet import reactor, protocol
from twisted.internet.protocol import ServerFactory as ServFactory
from twisted.internet.endpoints import TCP4ServerEndpoint


class Server(protocol.Protocol):
    def connectionMade(self):
        print("New Connection")
        self.transport.write("Hello from Server".encode("utf-8"))

    def dataReceived(self, data):
        print(data)
        self.transport.write(data)


class ServerFactory(ServFactory):
    def buildProtocol(self, addr):
        return Server()


if __name__ == "__main__":
    endpoint = TCP4ServerEndpoint(reactor, 2000)
    endpoint.listen(ServerFactory())
    reactor.run()
