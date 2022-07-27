# Level1 Design1 : MUX Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/gitpod_ID_CUB.png)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux-32x1 module here) which takes in *31* 2-bit inputs *inp0, inp1, inp2, ..., inp29, inp30* along with 4-bit input of *sel* and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.inp0.value = 0
dut.inp1.value = 2
dut.inp2.value = 1
""""""""
""""""""
dut.inp29.value = 3
dut.inp30.value = 2
dut.sel.value = 28
```

The assert statement is used for comparing the mux's outut to the expected value.

The following error is seen:
```
assert dut.out.value == int_list[sel], "Randomised test failed with: {INPUT_LIST} : {SEL} :: {OUT}".format(
                     AssertionError: Randomised test failed with: 3 : 01101 :: 00
```

## Test Scenario
- Test Inputs: inp11=3 sel=13(binary 01101)
- Expected Output: out=3
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
      5'b01000: out = inp8;  
      5'b01001: out = inp9;  
      5'b01010: out = inp10;
      5'b01011: out = inp11;
      5'b01101: out = inp12;      ===> BUG
      5'b01101: out = inp13;
      5'b01110: out = inp14;
      5'b01111: out = inp15;
```
For the adder design, the logic should be ``5'b01100: out = inp12`` instead of ``5'b01101: out = inp12`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/CUB_result_pass_level1_design1.png)

The updated design is checked in as mux_fix.v
