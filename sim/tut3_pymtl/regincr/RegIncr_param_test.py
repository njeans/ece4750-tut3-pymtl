#=========================================================================
# RegIncr_param_test
#=========================================================================

import collections
import pytest
import itertools

from random import sample

from pymtl  import *
from pclib.test import run_test_vector_sim, mk_test_case_table
from RegIncrNBit import RegIncrNbits


#-------------------------------------------------------------------------
# mk_test_vector_table
#-------------------------------------------------------------------------

def mk_test_vector_table( nbits, inputs ):
  test_vec_table = [ ('in_ out*')]
  inputs.extend( [0] )
  results = collections.deque( ['?'] )

  for i in inputs:
    test_vec_table.append( [ i, results.popleft() ] )
    results.append(Bits( nbits, i + 1, trunc=True))

  return test_vec_table

@pytest.mark.parametrize( "n", [ 8, 16, 32, 63] )
def test_random( n, dump_vcd):
  run_test_vector_sim( RegIncrNbits( nbits=n), 
    mk_test_vector_table(n, sample( xrange((2**n)-1) ,20) ) , dump_vcd)

