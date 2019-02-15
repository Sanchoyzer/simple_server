#!/usr/bin/env python3

from hashlib import sha512
from aiohttp import web
from aiofiles import open as aioopen


LOG_FILE = '/srv/src/log'
routes = web.RouteTableDef()


@routes.get('/input_str={input_str}')
async def hash_handler(request):
    input_val = request.match_info['input_str']
    output_val = sha512(input_val.encode('utf-8')).hexdigest() if input_val is not None else ''
    async with aioopen(LOG_FILE, 'a') as f:
        await f.write('in: "{}", out: "{}" \n'.format(input_val, output_val))
    return web.json_response({'output_str': output_val})


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app)


if __name__ == '__main__':
    main()
