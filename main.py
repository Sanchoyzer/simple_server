#!/home/alex/work/simple_server/venv/bin/python
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from json import dumps
from hashlib import sha512
from dotenv import dotenv_values
from threading import Thread


SERVER_ADDRESS = dotenv_values().get('ADDRESS')
SERVER_PORT = dotenv_values().get('PORT')
LOG_PATH = dotenv_values().get('LOG_PATH')


class HttpProcessor(BaseHTTPRequestHandler):
    def get_input_val(self):
        param_dict = parse_qs(urlparse(self.path).query)
        input_val = param_dict.get('input_str')
        return input_val[0] if input_val is not None else None

    @staticmethod
    def get_output_val(input_val):
        return sha512(input_val.encode('utf-8')).hexdigest() if input_val is not None else ''

    @staticmethod
    def inner_log(msg):
        with open(LOG_PATH, 'a') as f:
            f.write(msg + '\n')

    @staticmethod
    def log(msg):
        # задергаем диск уже на middleload
        # и пусть клиент ждет без асинхронщины
        # ведь это учебный пример :)
        t = Thread(target=HttpProcessor.inner_log, args=(msg,))
        t.start()

    def do_GET(self):
        input_val = self.get_input_val()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        output_val = self.get_output_val(input_val)
        self.wfile.write(dumps({'output_str': output_val}).encode('utf-8'))
        self.log('in: "{}", out: "{}"'.format(input_val, output_val))


def run():
    try:
        with HTTPServer((SERVER_ADDRESS, int(SERVER_PORT)), HttpProcessor) as httpd:
            print('start server')
            httpd.serve_forever()
    except KeyboardInterrupt:
        print('stop server')


if __name__ == '__main__':
    run()
