from colorama import init

from utils import cli_argument, Pipeline

if __name__ == "main":
    print('Fuck yes')
    init()
    args = cli_argument()
    phone_number = args.phone_number
    pipeline = Pipeline(args)
    pipeline.run(phone_number)
