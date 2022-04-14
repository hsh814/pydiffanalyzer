import scalpel.cfg as cfg
from scalpel.call_graph.pycg import CallGraphGenerator, formats
from typing import Dict, List, Set
import sys
import json
sys.path.append(".")
sys.path.append("..")
import comparer

def main() -> None:
  with open("v1/sqrt.py", "r") as v1:
    src = v1.read()
  with open("v2/remove_html_markup.py", "r") as v2:
    target = v2.read()
  srccfg = cfg.CFGBuilder().build_from_src("v1_sqrt.py", src)
  print(type(srccfg.functioncfgs))
  for (block_id, fun_name), fun_cfg in srccfg.functioncfgs.items():
    fun_cfg: cfg.CFG
    graph = fun_cfg.build_visual('png')
    graph.render("v1_sqrt")
    print(f"{block_id} {fun_name}")
    for sub in fun_cfg:
      sub: cfg.Block
      print(f"#{sub.id} {sub.statements[0].lineno}-{sub.statements[-1].lineno}")
      print(f"{sub.exits}")
      print(f"{sub.statements}")
  
  targetcfg = cfg.CFGBuilder().build_from_src("v2_sqrt.py", src)
  print(type(targetcfg.functioncfgs))
  for (block_id, fun_name), fun_cfg in targetcfg.functioncfgs.items():
    fun_cfg: cfg.CFG
    graph = fun_cfg.build_visual('png')
    graph.render("v2_sqrt")
    print(f"{block_id} {fun_name}")
    for sub in fun_cfg:
      sub: cfg.Block
      print(f"#{sub.id} {sub.statements[0].lineno}-{sub.statements[-1].lineno}")
      print(f"{sub.exits}")
      print(f"{sub.statements}")
  #an = comparer.Analyzer(src, target)
  #an.ast_diff()
  """
  cg_generator = CallGraphGenerator(["msv-search/msv-search.py"], "msv-search", 100, "call-graph")
  cg_generator.analyze()
  formatter = formats.Simple(cg_generator)
  with open("example_results.json", "w+") as f:
    f.write(json.dumps(formatter.generate()))
  """
main()