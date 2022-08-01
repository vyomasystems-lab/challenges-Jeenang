# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
from cocotb.binary import BinaryValue
@cocotb.test()
async def test_snoopy_cache(dut):
    """Test for snoopy cache """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.rst.value = 1
    await FallingEdge(dut.clk)  
    dut.rst.value = 0
    await FallingEdge(dut.clk)


    cocotb.log.info('#### CTB: Develop your test here! ######')
#  output seq_seen;
#  input inp_bit;
#  input reset;
#  input clk;

    dut.cpu_bus_in.value = 1
    await RisingEdge(dut.clk)
    dut._log.info(f'inp={int(dut.cpu_bus_in.value):b} model="Snoopy Cache" OUTPUT ={int(dut.bus_rw_miss_wb_out.value):b} PS ={int(dut.present_state.value):b}')
    dut.cpu_bus_in.value = 16
    await RisingEdge(dut.clk)
    dut._log.info(f'inp={int(dut.cpu_bus_in.value):b} model="Snoopy Cache" OUTPUT ={int(dut.bus_rw_miss_wb_out.value):b} PS ={int(dut.present_state.value):b}')
    dut.cpu_bus_in.value = 2
    await RisingEdge(dut.clk)
    dut._log.info(f'inp={int(dut.cpu_bus_in.value):b} model="Snoopy Cache" OUTPUT ={int(dut.bus_rw_miss_wb_out.value):b} PS ={int(dut.present_state.value):b}')
    assert dut.bus_rw_miss_wb_out.value == 2, "Test failed!!"