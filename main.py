import argparse


def main(routes_file_path):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--routes-file", required=False, default='routes.csv',
                        help='points to the csv file containing routes')
    args = parser.parse_args()
    main(args.routes_file)
