import socket
import threading

class FakeServer:
    def __init__(self, answers: dict[str,str], default_answer: str=None):
        self._sock = socket.socket()
        self._sock.bind(("localhost", 0))
        self._sock.listen()
        self.port = self._sock.getsockname()[1]
        self.requests_received = []
        self._answers = answers
        self._default_answer = default_answer
        self._accept_thread = threading.Thread(target=self._accept)
        self._accept_thread.start()

    def _accept(self):
        connection = self._sock.accept()[0]
        try:
            while True:
                request_char = connection.recv(1)
                if request_char == '\n' or (not request_char and request):
                    connection.sendall(str.encode(self._answers.get(request, self._default_answer)))
                    self.requests_received.append(request)
                    request = ""
                elif not request_char:
                    break
                else:
                    request += request_char
        finally:
            connection.close()

    def __del__(self):
        self._accept_thread.join()