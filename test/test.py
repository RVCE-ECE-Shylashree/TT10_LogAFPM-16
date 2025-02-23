# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
from cocotb.triggers import Timer 

@cocotb.test()
async def test_project(dut):
    
    dut._log.info("Start")
    dut.clk.value = 0  # Manually set clk to 0 before starting the clock
    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await Timer(10, units="ns")
    
    # Set the clock period to 10 ns (100 MHz)
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    
    await Timer(10, units="ns")
    dut.rst_n.value = 1
    
    dut._log.info("Test project behavior")
    
    # Set the input values you want to test
    dut.ui_in.value = 0xBC
    dut.uio_in.value = 0x90

    # Wait for two clock cycles
    await Timer(40, units="ns")
    dut.ui_in.value = 0x43
    dut.uio_in.value = 0x41

    await Timer(160, units="ns")
    assert dut.uo_out.value == 0x75

    await Timer(20, units="ns")
    assert dut.uo_out.value == 0x49
    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
