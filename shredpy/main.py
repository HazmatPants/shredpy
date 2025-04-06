import os
import sys
import argparse
import random

args = None
shredded = 0
patterns = {
    "00": b"\x00",
    "FF": b"\xFF",
    "AA": b"\xAA",
    "55": b"\x55",
    "92": b"\x92",
    "random": "random",  # os.urandom
    "deadbeef": b"\xDE\xAD\xBE\xEF",
    "feedface": b"\xFE\xED\xFA\xCE"
}

def shred(file):
    """
    Overwrites a file with random bytes, then (optionally) deletes it.
    """
    global shredded, patterns, args
    if args.dryrun:
        print(f"[Dry run] Would shred: {file}")
        shredded += 1
        return
    
    size = os.path.getsize(file)
    if args.verbose:
        print(f"Shredding {file} ({size} bytes) with {args.passes} passes...")
    with open(file, "wb") as f:
        for i in range(args.passes):
            if args.pattern is None:
                pattern = random.choice(list(patterns.values()))
            else:
                if args.pattern in patterns:
                    pattern = patterns[args.pattern]
                else:
                    print(f"{args.pattern} is not a valid pattern")
                    args.pattern = None
                    pattern = random.choice(list(patterns.values()))
                    print("Valid patterns:")
                    for i in range(len(patterns)):
                        print(list(patterns.keys())[i])
                    exit()
            if pattern == "random":
                f.write(os.urandom(size))
                if args.verbose and i % max(1, args.passes // 10) == 0:
                    print(f"Pass {i + 1}/{args.passes} with pattern urandom")
            else:
                f.write(pattern * size)
                if args.verbose and i % max(1, args.passes // 10) == 0:
                    print(f"Pass {i + 1}/{args.passes} with pattern {pattern}")

    if not args.nodelete:
        os.remove(file)
        if args.verbose:
            print(f"Deleted {file}")
    else:
        if args.verbose:
            print(f"Skipped deleting {file} (nodelete)")
    shredded += 1

def main():
    global args
    parser = argparse.ArgumentParser()
    # define parameters
    # int
    parser.add_argument("-p", "--passes", type=int, help="Number of times to pass the file through the shredder", default=10000)
    # list
    parser.add_argument("-f", "--files", type=str, help="File(s) to shred", nargs="+", required=True)
    # bool
    parser.add_argument("-nd", "--nodelete", action="store_true", help="Do not delete the file(s), only overwrite")
    parser.add_argument("-nc", "--noconfirm", action="store_true", help="Do not ask for confirmation")
    parser.add_argument("-d", "--dryrun", action="store_true", help="Only show what would be shredded")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    parser.add_argument("-P", "--pattern", type=str, help="Use a specific pattern")

    args = parser.parse_args()
    
    for file in args.files:
        try:
            if args.noconfirm:
                if args.verbose:
                    print(f"Skipped confirmation for {file} (noconfirm)")
                if not os.path.isfile(file):
                    print(f"Skipping: {file} is not a valid file.")
                    continue
                shred(file)
            else:
                confirm = input(f"Shred {file}? (y/n): ")
                if confirm.lower() == 'y':
                    if not os.path.isfile(file):
                        print(f"Skipping: {file} is not a valid file.")
                        continue
                    shred(file)
                else:
                    print(f"{file} not shredded")
        except Exception as e:
            print(f"Error: {e}")

    if args.dryrun:
        print(f"{shredded} file(s) would be shredded")
    else:
        print(f"Shredded {shredded} file(s)")

if __name__ == "__main__":
    main()
