#=========================================================================
# RegIncrNbits
#=========================================================================
# Registered incrementer that is parameterized by the bitwidth.

from pymtl   import *

class RegIncrNbits( Model ):

  # Constructor
  def __init__( s, nbits=8 ):

    # Port-based interface
    s.in_ = InPort  (nbits)
    s.out = OutPort (nbits)

    s.reg_out = Wire( Bits(nbits) )

    @s.tick
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_

    # Concurrent block modeling incrementer
    @s.combinational
    def block2():
      s.out.value = s.reg_out + 1 

  # Line Tracing
  def line_trace( s ):
    return "{} ({}) {}".format( s.in_, s.reg_out, s.out )
