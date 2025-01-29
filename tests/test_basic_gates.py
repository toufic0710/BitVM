import pytest
from src.circuits.circuit import Circuit
from src.circuits.basic_gates import Wire, ANDGate, NOTGate
from src.protocol.challenger import Challenger, Challenge

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

def test_challenger_verification():
    """Test the challenger verification system"""
    circuit = create_test_circuit()
    challenger = Challenger()
    
    # Test with valid response
    challenge = challenger.create_challenge(0)  # Challenge AND gate
    valid_response = {
        'gate_index': 0,
        'inputs': [True, False],
        'output': False
    }
    assert challenger.verify_response(valid_response, challenge)
    
    # Test with invalid gate index
    invalid_response = {
        'gate_index': 1,  # Wrong gate index
        'inputs': [True, False],
        'output': False
    }
    assert not challenger.verify_response(invalid_response, challenge)
    
    # Test with invalid input types
    invalid_types_response = {
        'gate_index': 0,
        'inputs': [1, 0],  # Should be boolean
        'output': False
    }
    assert not challenger.verify_response(invalid_types_response, challenge)

def test_circuit_verification():
    """Test complete circuit verification"""
    circuit = create_test_circuit()
    challenger = Challenger()
    
    # Set inputs and evaluate
    circuit.set_inputs([True, False])
    circuit.evaluate()
    
    # Verify entire circuit
    assert challenger.verify_circuit(circuit, {})  # Empty commitments for now

def test_challenge_creation():
    """Test challenge creation"""
    challenger = Challenger()
    challenge = challenger.create_challenge(0)
    
    assert challenge.gate_index == 0
    assert challenge.expected_output is None
    assert isinstance(challenge.input_values, list)