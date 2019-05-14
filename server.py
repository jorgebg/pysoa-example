from pysoa.server import Server
from pysoa.server.action import Action


class SquareAction(Action):

    def run(self, request):
        square = request.body['number'] ** 2
        return {
            'square': square,
        }


class ExampleServer(Server):

    service_name = 'example'

    action_class_map = {
        'square': SquareAction,
    }


if __name__ == '__main__':
    ExampleServer.main()
