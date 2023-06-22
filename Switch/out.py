from Switch.switch_builtins import *
main_ns = Namespace()
main_ns.walrus('$', exec('''
def _f0(_f0_arg0):
 _f0_ns = deepcopy(main_ns)
 _f0_ns.update({'@': _f0_arg0})
 while less_than(_f0_ns['@'],SwitchFrac(2)):
  return SwitchFrac(1)


 return add(_f0_ns['$'](sub(_f0_ns['@'],SwitchFrac(1))),_f0_ns['$'](sub(_f0_ns['@'],SwitchFrac(2))))
''', ns_d := {key: (val.__dict__ if isinstance(val, ModuleType) else val) for key, val in {**globals(), **locals()}.items()}) or ns_d['_f0'])
print_no_nl(main_ns['$'](SwitchFrac(8)))
