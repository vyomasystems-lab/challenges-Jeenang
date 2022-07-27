# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await RisingEdge(dut.clk)  
    dut.reset.value = 0
    await RisingEdge(dut.clk)


    cocotb.log.info('#### CTB: Develop your test here! ######')
#  output seq_seen;
#  input inp_bit;
#  input reset;
#  input clk;
    input_seq = []
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    input_seq.append(dut.inp_bit.value)
    dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    input_seq.append(dut.inp_bit.value)
    dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')
    dut.inp_bit.value = 0
    await RisingEdge(dut.clk)
    input_seq.append(dut.inp_bit.value)
    dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    input_seq.append(dut.inp_bit.value)
    dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')
    dut.inp_bit.value = 1
    await RisingEdge(dut.clk)
    input_seq.append(dut.inp_bit.value)
    dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')
    assert dut.seq_seen.value == 1, "Sequence Detection test failed!!"

@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await RisingEdge(dut.clk)  
    dut.reset.value = 0
    await RisingEdge(dut.clk)
#  output seq_seen;
#  input inp_bit;
#  input reset;
#  input clk;
    input_seq = []
    while(dut.seq_seen.value!=1):
        dut.inp_bit.value = random.randint(0, 1)
        await RisingEdge(dut.clk)
        input_seq.append(dut.inp_bit.value)
        dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')

   # dut._log.info(f'inp={int(dut.inp_bit.value):01} model="SEQ_1011 " SEQ_SEEN={int(dut.seq_seen.value):01}')
    cocotb.log.info('INPUT SEQUENCE::')
    print(input_seq)
