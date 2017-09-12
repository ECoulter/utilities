#!/usr/bin/env python3
import argparse
import sys
import textwrap

def main():
  parser=argparse.ArgumentParser()
  parser.add_argument("script_name",help="Name of the script to be created")
  parser.add_argument("-f","--with_file",help="Add skeleton of file open/write",action="store_true")
  parser.add_argument("-a","--with_args",help="Add skeleton of argparse useage",action="store_true")
  args=parser.parse_args()
  print("Creating "+args.script_name+".py")

  script_head="""#!/usr/bin/env python3"""

  script_imports=("""\n"""
    """import argparse\n"""
    """import sys\n""")
   
  script_main=("""\n"""
    """def main():\n"""
    """  pass\n"""
    """\n""")

  script_file_skel=(
    """  try:\n"""
    """    with open(file_name,'x') as script_file: #"w" for write, "a" for append, "x" checks for file exist, "r" for read\n"""
    """      filename.write(script_head+script_imports+script_main)\n"""
    """  except Exception as err:\n"""
    """    print("IOError:",err) \n"""
    """\n""")

  script_args_skel=(
    """  parser=argparse.ArgumentParser()\n"""
    """  parser.add_argument("string_arg",help="Positional string argument")\n"""
    """  parser.add_argument("-f","--flag",help="Basic flag arg",action="store_true")\n"""
    """  args=parser.parse_args()\n"""
    """  if args.flag:\n"""
    """    print("Flag turned on")\n"""
    """  print("This is an argument:",args.string_arg)\n"""
    """\n""")
 
  script_close=(
    """if __name__ == '__main__':\n"""
    """  main()\n""")

  if args.with_file:
    script_main += script_file_skel
  if args.with_args:
    script_main += script_args_skel

  try:
    with open(args.script_name+".py",'x') as script_file:
      script_file.write(script_head+script_imports+script_main+script_close)
  except Exception as err:
    print("IOError:",err) 
    

if __name__ == '__main__':
  main()
