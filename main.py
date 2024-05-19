import os

from colorama import init

from utils import cli_argument, Pipeline

if __name__ == "__main__":
    init()

    if os.path.exists("located_numbers"):
        os.mkdir("located_numbers")

    args = cli_argument()
    phone_number = args.phone_number
    pipeline = Pipeline(args)
    pipeline.run(phone_number)
