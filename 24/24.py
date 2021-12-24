import sys
import collections

program = [line.strip().split() for line in sys.stdin]


class AstNode:
  pass

  def simplify(self):
    return self

  @property
  def constant(self):
    return False


class Constant(AstNode):
  def __repr__(self):
    return str(self.val)

  def __init__(self, val):
    self.val = val

  @property
  def constant(self):
    return True


class Variable(AstNode):
  def __repr__(self):
    return f'<i{self.ord}>'

  def __init__(self, ord):
    self.ord = ord


class BinOp(AstNode):
  def __repr__(self):
    return f'({self.OP} {self.left} {self.right})'

  def __init__(self, left, right):
    self.left = left
    self.right = right


class Mul(BinOp):
  OP = '*'

  def simplify(self):
    if self.left.constant and self.right.constant:
      return Constant(self.left.val * self.right.val)
    if self.left.constant:
      if self.left.val == 0: return Constant(0)
      if self.left.val == 1: return self.right
    if self.right.constant:
      if self.right.val == 0: return Constant(0)
      if self.right.val == 1: return self.left
    return self


class Add(BinOp):
  OP = '+'

  def simplify(self):
    if self.left.constant and self.right.constant:
      return Constant(self.left.val + self.right.val)
    if self.left.constant and self.left.val == 0:
      return self.right
    if self.right.constant and self.right.val == 0:
      return self.left
    return self


class Div(BinOp):
  OP = '/'

  def simplify(self):
    if self.left.constant and self.right.constant:
      return Constant(self.left.val // self.right.val)
    if self.right.constant and self.right.val == 1:
      return self.left
    return self


class Mod(BinOp):
  OP = '%'

  def simplify(self):
    if self.left.constant and self.right.constant:
      return Constant(self.left.val % self.right.val)
    return self


class Eq(BinOp):
  OP = 'eq'

  def simplify(self):
    if self.left.constant and self.right.constant:
      return Constant(1 if self.left.val == self.right.val else 0)
    return self


def evaluate_instruction(instruction, registers, inputs: collections.deque):
  def reg_or_val(x):
    return registers[x] if x in 'xyzw' else int(x)

  i, args = instruction[0], instruction[1:]
  if i == 'inp':
    return {**registers, **{args[0]: inputs.popleft()}}
  else:
    fn = dict(
        add=lambda a, b: a + b,
        mul=lambda a, b: a * b,
        div=lambda a, b: a // b,
        mod=lambda a, b: a % b,
        eql=lambda a, b: 1 if a == b else 0,
    )[i]
    return {
        **registers,
        **{
            args[0]: fn(reg_or_val(args[0]), reg_or_val(args[1]))
        }
    }

def evaluate(program, inputs):
  registers=dict(x=0, y=0, z=0, w=0)
  for instr in program:
    registers = evaluate_instruction(instr, registers, inputs)
  return registers

i = 0
registers = dict(x=Constant(0), y=Constant(0), z=Constant(0), w=Constant(0))

n = 0
for instruction in program:
  op, args = instruction[0], instruction[1:]
  temp = f'r_{i}'
  if op == 'inp':
    registers[temp] = Variable(n)
    n += 1
  else:

    def reg_or_arg(x):
      return registers[x] if x in 'xyzw' else Constant(int(x))

    def expand(x):
      if x in registers:
        return registers[x]
      return x

    a = expand(reg_or_arg(args[0]))
    b = expand(reg_or_arg(args[1]))
    result = dict(add=Add, mul=Mul, div=Div, mod=Mod, eql=Eq)[op](a, b)
    registers[temp] = result.simplify()

  registers[args[0]] = f'r_{i}'
  i += 1

expr = registers[registers['z']]
