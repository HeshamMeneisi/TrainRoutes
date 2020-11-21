import argparse
import sys

from routing import Router


def main(args) -> int:
    try:
        print("TrainRoutes CLI Started")

        print(f'Loading routes from {args.routes_file}')
        router = Router(args.routes_file)
        print('Routes loaded')
        # Support non-interactive origin/dest args
        origin = args.origin
        dest = args.dest
        start_cli_loop(router, origin, dest)
    except Exception as ex:
        print(sys.stderr, ex)
        return 1


def start_cli_loop(router: Router, origin: str = None, dest: str = None):
    interactive = not origin and not dest

    while interactive:

        # block until origin is valid
        while not router.has_station(origin):
            if origin:
                print(f'Station "{origin}" not found')
            origin = input('Enter Origin Station: ')

        # block until dest is valid
        while not router.has_station(dest):
            if dest:
                print(f'Station "{dest}" not found')
            dest = input('Enter Destination Station: ')

        print('Routing...')
        try:
            route = router.find_route(origin, dest)
            if route is None:
                print(f'Result: No routes from {origin} to {dest}')
            else:
                print(f'Result: {route.stop_count} stop(s), {route.total_time} minute(s)')
                print(f'Details: {", ".join([str(seg) for seg in route.path])}')
        except Exception as ex:
            print(sys.stderr, ex)

        origin = dest = None

    return 0


def create_arg_parser():
    p = argparse.ArgumentParser()
    p.add_argument('--routes-file', required=False, default='routes.csv',
                   help='points to the csv file containing routes')
    p.add_argument('--origin', required=False, help='(Optional) origin station name')
    p.add_argument('--dest', required=False, help='(Optional) destination station name')
    return p


if __name__ == '__main__':
    parser = create_arg_parser()
    argv = parser.parse_args()
    exit(main(argv))
