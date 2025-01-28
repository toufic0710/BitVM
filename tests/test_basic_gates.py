import pytest
from src.circuits.circuit import Circuit
from src.circuits.basic_gates import Wire, ANDGate, NOTGate

def create_test_circuit() -> Circuit:
    circuit = Circuit()
    
    # Create input wires
    a = Wire()
    b = Wire()
    circuit.input_wires = [a, b]
    
    # Create gates
    and_gate = ANDGate()
    not_gate = NOTGate()
    
    # Connect wires
    and_gate.connect_input(a)
    and_gate.connect_input(b)
    
    intermediate_wire = Wire()
    and_gate.connect_output(intermediate_wire)
    not_gate.connect_input(intermediate_wire)
    
    output_wire = Wire()
    not_gate.connect_output(output_wire)
    circuit.output_wires = [output_wire]
    
    # Add gates to circuit
    circuit.add_gate(and_gate)
    circuit.add_gate(not_gate)
    
    return circuit

def test_nand_truth_table():
    """Test all possible inputs for the NAND circuit"""
    circuit = create_test_circuit()
    
    # NAND truth table
    test_cases = [
        ([False, False], True),
        ([False, True], True),
        ([True, False], True),
        ([True, True], False)
    ]
    
    for inputs, expected_output in test_cases:
        circuit.set_inputs(inputs)
        outputs = circuit.evaluate()
        assert outputs[0] == expected_output, f"Failed for inputs {inputs}"