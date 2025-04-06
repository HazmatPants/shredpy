import os
import sys
import argparse

parser = argparse.ArgumentParser()
# parameters
# int
parser.add_argument("--passes", type=int, help="Number of times to pass the file through the shredder", default=10000)
# list
parser.add_argument("--files", type=str, help="File(s) to shred", nargs="+", required=True)
# bool
parser.add_argument("--nodelete", action="store_true", help="Do not delete the file(s), only overwrite")
parser.add_argument("--noconfirm", action="store_true", help="Do not ask for confirmation")
parser.add_argument("--dryrun", action="store_true", help="Only show what would be shredded")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

args = parser.parse_args()
shredded = 0

def shred(file):
    """
    Overwrites a file with random bytes, then (optionally) deletes it.
    """
    global shredded
    if args.dryrun:
        print(f"[Dry run] Would shred: {file}")
        shredded += 1
        return
    
    size = os.path.getsize(file)
    if args.verbose:
        print(f"Shredding {file} ({size} bytes) with {args.passes} passes...")
    patterns = [b'\x00', b'\xFF', None]  # None = use os.urandom
    with open(file, "wb") as f:
        for i in range(args.passes):
            pattern = patterns[i % len(patterns)]
            if pattern is None:
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
        except PermissionError as e:
            print(f"Permission denied for {file} ({e})")
        except Exception as e:
            print(f"Error: {e}")

    if args.dryrun:
        print(f"{shredded} file(s) would be shredded")
    else:
        print(f"Shredded {shredded} file(s)")
