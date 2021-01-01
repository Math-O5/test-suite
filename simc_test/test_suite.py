import argparse

from simc_test.unittests.main import unit_test

parser = argparse.ArgumentParser(description="sim-C Test Suite")
parser.add_argument("--unit", "-u", action='store_true')
parser.add_argument("--code", "-c", action='store_true')

def hello():
    print("Hello World")

args = vars(parser.parse_args())
args_with_func = {"unit": unit_test, "code": hello}

if not any(list(args.values())):
    for arg, test_func in args_with_func.items():
        test_func()
else:
    for arg, should_run in args.items():
        if should_run:
            args_with_func[arg]()