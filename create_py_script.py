#!/usr/bin/env python3
import argparse
import sys
import textwrap

def main():
  parser=argparse.ArgumentParser()
  parser.add_argument("script_name")
  args=parser.parse_args()
  print("Creating "+args.script_name+".py")

  script_head="""#!/usr/bin/env python3"""

  script_imports=("""\n"""
    """import argparse\n"""
    """import sys\n""")
   
  script_main=("""\n"""
    """def main():\n"""
    """  pass\n"""
    """\n"""
    """if __name__ == '__main__':\n"""
    """  main()\n""")

  with open(args.script_name+".py",'w') as script_file:
    script_file.write(script_head+script_imports+script_main)

if __name__ == '__main__':
  main()
