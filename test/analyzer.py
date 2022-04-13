import sys
sys.path.append(".")
sys.path.append("..")
import comparer

def main() -> None:
  with open("v1/remove_html_markup.py", "r") as v1:
    src = v1.read()
  with open("v2/remove_html_markup.py", "r") as v2:
    target = v2.read()
  an = comparer.Analyzer(src, target)
  an.ast_diff()

main()