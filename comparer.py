import ast
import pprint

class Analyzer():
  def __init__(self, src: str, target: str) -> None:
    self.src = src
    self.target = target
    self.src_ast = ast.parse(self.src)
    self.target_ast = ast.parse(self.target)
  def ast_diff(self) -> None:
    pprint.pprint(ast.dump(self.src_ast))
    pprint.pprint(ast.dump(self.target_ast))
    print("Now iterate over ast")
    for fieldname, value in ast.iter_fields(self.src_ast):
      print(fieldname)
      print(value)