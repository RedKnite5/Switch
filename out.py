from Switch.switch_builtins import *
namespace = Namespace()
exec('''
def _f2005304714240():
 _f2005304714240_ns = deepcopy(namespace)
 _f2005304714240_ns.update({})
 exec('''
def _f2005304706000(_f2005304706000_arg0):
 _f2005304706000_ns = deepcopy(_f2005304714240_ns)
 _f2005304706000_ns.update({'.': _f2005304706000_arg0})
 print_no_nl(_f2005304706000_ns['.'])
''', ns_d := {key: (val.__dict__ if isinstance(val, ModuleType) else val) for key, val in globals().items()}) or ns_d['_f2005304706000'](SwitchFrac(4))
''', ns_d := {key: (val.__dict__ if isinstance(val, ModuleType) else val) for key, val in globals().items()}) or ns_d['_f2005304714240']()
