# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""

    inp0 = 2
    sel = 0

    # input driving
    dut.inp0.value = inp0
    dut.sel.value = sel

    await Timer(2, units='ns')

    assert dut.out.value == inp0, f"Mux result is incorrect: {dut.X.value} != {inp0}"


@cocotb.test()
async def adder_randomised_test(dut):
    """Test for adding 2 random numbers multiple times"""

    for i in range(32):

        inp0 = random.randint(0, 3)
        inp1 = random.randint(0, 3)
        inp2 = random.randint(0, 3)
        inp3 = random.randint(0, 3)
        inp4 = random.randint(0, 3)
        inp5 = random.randint(0, 3)
        inp6 = random.randint(0, 3)
        inp7 = random.randint(0, 3)
        inp8 = random.randint(0, 3)
        inp9 = random.randint(0, 3)
        inp10 = random.randint(0, 3)
        inp11 = random.randint(0, 3)
        inp12 = random.randint(0, 3)
        inp13 = random.randint(0, 3)
        inp14 = random.randint(0, 3)
        inp15 = random.randint(0, 3)
        inp16 = random.randint(0, 3)
        inp17 = random.randint(0, 3)
        inp18 = random.randint(0, 3)
        inp19 = random.randint(0, 3)
        inp20 = random.randint(0, 3)
        inp20 = random.randint(0, 3)
        inp21 = random.randint(0, 3)
        inp22 = random.randint(0, 3)
        inp23 = random.randint(0, 3)
        inp24 = random.randint(0, 3)
        inp25 = random.randint(0, 3)
        inp26 = random.randint(0, 3)
        inp27 = random.randint(0, 3)
        inp28 = random.randint(0, 3)
        inp29 = random.randint(0, 3)
        inp30 = random.randint(0, 3)
        sel =random.randint(0, 31)

        # input driving
        dut.inp0.value = inp0
        dut.inp1.value = inp1
        dut.inp2.value = inp2
        dut.inp3.value = inp3
        dut.inp4.value = inp4
        dut.inp5.value = inp5
        dut.inp6.value = inp6
        dut.inp7.value = inp7
        dut.inp8.value = inp8
        dut.inp9.value = inp9
        dut.inp10.value = inp10
        dut.inp11.value = inp11
        dut.inp12.value = inp12
        dut.inp13.value = inp13
        dut.inp14.value = inp14
        dut.inp15.value = inp15
        dut.inp16.value = inp16
        dut.inp17.value = inp17
        dut.inp18.value = inp18
        dut.inp19.value = inp19
        dut.inp20.value = inp20
        dut.inp21.value = inp21
        dut.inp22.value = inp22
        dut.inp23.value = inp23
        dut.inp24.value = inp24
        dut.inp25.value = inp25
        dut.inp26.value = inp26
        dut.inp27.value = inp27
        dut.inp28.value = inp28
        dut.inp29.value = inp29
        dut.inp30.valie = inp30
        dut.sel.value = sel

        int_list = [inp0, inp1, inp2, inp3, inp4, inp5, inp6,
            inp7, inp8, inp9, inp10, inp11, inp12, inp13, 
            inp14, inp15, inp16, inp17, inp18, inp19, inp20,
            inp21, inp22, inp23, inp24, inp25, inp26,
            inp27, inp28, inp29, inp30]

        await Timer(2, units='ns')
        
        dut._log.info(f'inp={int_list[sel]:05} sel={sel:05} model="MUX " DUT={int(dut.out.value):05}')
        assert dut.out.value == int_list[sel], "Randomised test failed with: {INPUT_LIST} : {SEL} :: {OUT}".format(
            INPUT_LIST=dut.inp30.value, SEL=dut.sel.value, OUT=dut.out.value)