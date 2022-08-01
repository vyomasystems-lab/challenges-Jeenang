## Capture The Bug Hackathon : Jeenang Shah 

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/gitpod_ID_CUB.png)

## Level1 Design1 : MUX Design Verification Environment

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

### Test Scenario
- Test Inputs: inp11=3 sel=13(binary 01101)
- Expected Output: out=3
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

### Design Bug
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

### Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/CUB_result_pass_level1_design1.png)

The updated design is checked in as mux_fix.v

## Level1 Design2 : Sequence Detector Design Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (SEQ_1011 Detector) which takes in single bit input *inp_bit* along with single bit *clk* and *reset*. It gives *seq_seen* output which is also a single bit. 

The sequence is passed one by one as shown belo,
```
dut.inp_bit.value = 0
await RisingEdge(dut.clk)
```
Also, 10us clock is defined with use of cocotb library. 
```
clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
cocotb.start_soon(clock.start())        # Start the clock
```

The assert statement is used for comparing the sequence detector's outut to the expected value when valid sequence is passed.

The following error is seen:
```
assert dut.seq_seen.value == 1, "Sequence Detection test failed!!"
                     AssertionError: Sequence Detection test failed!!
```

### Test Scenario
**Case 1: Normal Sequence 1,0,1,1 is applied**
- Test Inputs: Seqence 1,0,1,1 is applied (After changing the bit waited till posedge of clock)
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen=0

Output mismatches for the above inputs proving that there is a design bug

**Case 2: Finding Bug. Looking for Output 1**
- Test Inputs: Random input of 1 or 0 is applied till seq_seen turn is set.
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen=1

***Observation: seq_seen will be set after one clk cycle of sequence detection(see image below)***

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/CUB_result_fail_level1_design2.png)

### Design Bug
Based on the above test input and analysing the design, we see the following
```
  // if the current state of the FSM has the sequence 1011, then the output is
  // high
  assign seq_seen = current_state == SEQ_1011 ? 1 : 0;
```
Value of *seq_seen* depends of *current_state*, also *current_state* is updated to *next_state* at every posedge of *clk*. So, *seq_seen* will change will be updated in next cycle. 
***Update:*** *seq_seen* can be updated based on *next_state*. 

### Design Fix
Updating the design and re-running the test makes the test pass.

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/CUB_result_pass_level1_design2.png)

The updated design is checked in as seq_detect_1011_fix.v

## Level2 Design : Bit Manupulation Coprocessor Design Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3, mav_putvalue_instr all 32 bits wide. 

The inputs are passed one by one as shown belo,
```

```
Also, 10us clock is defined with use of cocotb library. 
```
clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
cocotb.start_soon(clock.start())        # Start the clock
```

The assert statement is used for comparing the sequence detector's outut to the expected value when valid sequence is passed.

The following error is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0xa does not match MODEL = 0x0For Input: mav_putvalue_src1 = 0x5, mav_putvalue_src2 = 0x2, mav_putvalue_src3 = 0x3, mav_putvalue_instr = 0x101010b3
```

![](https://github.com/vyomasystems-lab/challenges-Jeenang/blob/master/raw_data/CUB_result_fail_level1_design2.png)

