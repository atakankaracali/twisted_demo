from twisted.internet import reactor, protocol
from twisted.internet.protocol import ClientFactory as ClFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


class Client(protocol.Protocol):
    def dataReceived(self, data):
        data = data.decode("utf-8")
        print(data)
        self.transport.write(input(":::").encode("utf-8"))


class ClientFactory(ClFactory):
    def buildProtocol(self, addr):
        return Client()


if __name__ == "__main__":
    endpoint = TCP4ClientEndpoint(reactor, "localhost", 2000)
    endpoint.connect(ClientFactory())
    reactor.run()
