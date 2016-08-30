#=========================================================================
# RegIncr
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl import *

class RegIncr( Model ):

  def line_trace( s ):
    return "in:{} ({}) out:{}".format( s.in_, s.reg_out, s.out )

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

    # Sequential logic

    s.reg_out = Wire( Bits(8) )

    
   

    @s.tick
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert a
    # combinational concurrent block here to model the incrementer logic,
    # and later you will insert a line tracing function to compactly
    # output the input, register, and output values.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    #Concurrent block modeling incrementer

    @s.combinational
    def block2():
      s.out.value = s.reg_out +1
      #s.out.value = s.reg_out +2


    
   



