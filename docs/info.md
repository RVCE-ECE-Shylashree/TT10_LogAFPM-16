> ## 📌 Credits  
>  
> We sincerely acknowledge the **Center of Excellence in Integrated Circuits and Systems (ICAS)** and the **Department of Electronics and Communication Engineering, R.V. College of Engineering, Bengaluru**, for their invaluable support in providing us with the necessary knowledge and training.  
>  
> We extend our special gratitude to **Dr. K S Geetha (Vice Principal)** and **Dr. K N Subramanya (Principal)** for their continuous encouragement and support, enabling us to achieve **TAPEOUT** in **Tiny Tapeout 10**.  
>  
> We are also deeply grateful to **Mahaa Santeep G (RVCE Alumni)** for his mentorship and invaluable guidance throughout the completion of this project.  
  

The code provided is a Verilog module that implements a 16-bit logarithmic approximate floating-point multiplier. This module utilizes logarithmic approximation techniques to perform floating-point multiplication efficiently, reducing computational complexity while maintaining accuracy. It incorporates a state machine that processes the LSB(lower 8 bits) of the inputs in the first cycle and the MSB(upper 8 bits) in the next cycle, subsequently producing the LSB(lower 8 bits) of the output first, followed by the MSB(upper 8 bits) in the next cycle.

Key Components

The Logarithmic Approximate Floating-Point Multiplier (LAFPM) is a hardware-efficient multiplier that processes two 16-bit floating-point numbers using logarithmic approximation techniques. Instead of traditional multiplication, this design reduces complexity by leveraging logarithmic transformations, shifts, and additions. This approach significantly lowers power consumption and area, making it ideal for resource-constrained applications such as machine learning accelerators and embedded systems.
The multiplier operates using a finite state machine (FSM) that progresses through several key states:

**IDLE** – The system remains in this state until a non-zero input is detected. Once an input is received, it transitions to the next stage.

**COLLECT** – The multiplier collects the two 8-bit portions of each operand over multiple cycles to reconstruct the 16-bit floating-point numbers. After both parts are received, it moves to processing.

**PROCESS_1** – The floating-point components, including the sign, exponent, and mantissa, are extracted for further computation.

**PROCESS_2** – The mantissas undergo logarithmic approximation through bit-shifting techniques, reducing the complexity of multiplication.

**PROCESS_3** – The approximated mantissas are added together using a logarithmic-based summation.

**PROCESS_4** – A carry-out bit is determined, which helps adjust the exponent in the next stage.

**PROCESS_5** – The new exponent is computed, and an additional approximation step refines the mantissa for better accuracy.

**PROCESS_6** – The final floating-point result is assembled, combining the computed sign, exponent, and mantissa.

**OUTPUT** – The computed result is transmitted over multiple cycles. Once completed, the system returns to the IDLE state, ready for the next operation.

**Inputs and Clock Frequency**

**u_in and uio_in** are used to receive operands A and B through multiple cycles.

**rst_n** is the active-low reset signal.

**clk** operates at a 50 MHz frequency.

Table: State Transi for FP-16 Multiplication 0x

| **Time (ns)** | **`ui_in` (Input)** | **State**            | **`uio_out` (Expected Output)** | **`uo_out` (Expected Output)** |
|---------------|---------------------|----------------------|---------------------------------|--------------------------------|
| 0             | `11110010`           | NORMAL               | `01010110`                      | `010_010010`                   |
| 10            | `00010010`           | PERFORMANCE          | `11111111`                      | `111_111111`                   |
| 30            | `11110010`           | NORMAL               | `01010110`                      | `010_010010`                   |
| 50            | `11110011`           | THERMAL_MANAGEMENT    | `10101011`                      | `011_011011`                   |
| 70            | `11110010`           | NORMAL               | `01010110`                      | `010_010010`                   |
| 90            | `11101010`           | THERMAL_MANAGEMENT    | `10101011`                      | `011_011011`                   |
| 110           | `11111010`           | BATTERY_SAVING        | `00000000`                      | `000_000000`                   |
| 130           | `11111110`           | BATTERY_SAVING        | `00000000`                      | `000_000000`                   |
| 150           | `11111010`           | BATTERY_SAVING        | `00000000`                      | `000_000000`                   |


Explanation of Table Columns:

Time (ns): The simulation time when the ui_in input is applied. ui_in (Input): The 8-bit input value applied to the design. State: The state of the FSM based on the ui_in input. The states are NORMAL, PERFORMANCE, THERMAL_MANAGEMENT, and BATTERY_SAVING. uio_out (Expected Output): The expected 8-bit output values for the uio_out signals. uio_out[0]: Power save mode indicator. uio_out[2:1], uio_out[4:3], uio_out[6:5]: Voltage controls. uio_out[7]: Part of fcore1[0]. uo_out (Expected Output): The expected 8-bit output values for the uo_out signals. uo_out[0:1]: Part of fcore1[2:1]. uo_out[4:2]: fcore2[2:0]. uo_out[7:5]: fmem[2:0].

Explanation of Key Points: NORMAL State: When the inputs suggest a typical operating environment (e.g., ui_in = 11110010), the design operates with default voltage and frequency levels. PERFORMANCE State: Triggered by a performance request (perf_req = 1), leading to maximum voltage and frequency levels. THERMAL_MANAGEMENT State: Triggered by high temperature (temp_sensor = 10 or 11), moderates the voltage and frequency to prevent overheating. BATTERY_SAVING State: Triggered by low battery level (battery_level = 00 or 01), minimizing power consumption by reducing voltage and frequency to the lowest levels.

Testbench Operation: The testbench applies different ui_in values at specific simulation times. At each time step, it captures the output values (uio_out and uo_out) and compares them with the expected values as per the design's FSM logic. The $monitor statement continuously logs the input and output values, helping to verify the design's behavior at each time point.
