import argparse


def build_greeting(name):
    return f"Hello, {name}!"


def main():
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("name", nargs="?", default="Git learner")
    args = parser.parse_args()
    print(build_greeting(args.name))


if __name__ == "__main__":
    main()
