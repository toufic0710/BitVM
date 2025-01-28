import sys
import os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.circuits.basic_gates import Wire, ANDGate, NOTGate
from src.circuits.circuit import Circuit
from src.protocol.challenger import Challenger
from src.protocol.responder import Responder
from src.protocol.commitment import CommitmentScheme

def create_simple_circuit() -> Circuit:
    """
    Creates a simple circuit that implements: NOT(AND(a, b))
    This is equivalent to NAND gate, which is universal for computation
    """
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

def main():
    # Create and setup circuit
    circuit = create_simple_circuit()
    
    # Test with inputs [True, False]
    circuit.set_inputs([True, False])
    
    # Evaluate circuit
    outputs = circuit.evaluate()
    print(f"Circuit inputs: [True, False]")
    print(f"Circuit output: {outputs[0]}")
    
    # Create commitments
    commitment_scheme = CommitmentScheme()
    commitments = commitment_scheme.commit_to_circuit(circuit)
    
    # Setup verification
    challenger = Challenger()
    responder = Responder()
    responder.set_circuit(circuit)
    
    # Run verification
    is_valid = challenger.verify_circuit(circuit, commitments)
    print(f"Circuit verification: {is_valid}")

if __name__ == "__main__":
    main()