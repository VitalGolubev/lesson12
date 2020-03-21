import time


class NotesApp:
    def __init__(self, filename=None):
        self.filename = filename if filename else 'notes.json'

    def run(self):
        while True:
            print('I\'m running')
            time.sleep(1)

    def shutdown(self):
        print('Shutdown')


if __name__ == '__main__':
    app = NotesApp()
    try:
        app.run()
    except KeyboardInterrupt:
        app.shutdown()
