#!/usr/bin/env python3
import argparse
import sys

def main():
  parser=argparse.ArgumentParser()
  parser.add_argument("script_name")
  args=parser.parse_args()
  print(args.script_name+".py")

if __name__ == '__main__':
  main()
