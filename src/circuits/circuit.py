from typing import List
from .basic_gates import Wire, Gate

class Circuit:
    def __init__(self):
        self.gates: List[Gate] = []
        self.input_wires: List[Wire] = []
        self.output_wires: List[Wire] = []

    def add_gate(self, gate: Gate):
        self.gates.append(gate)

    def set_inputs(self, values: List[bool]):
        if len(values) != len(self.input_wires):
            raise ValueError("Number of values doesn't match number of input wires")
        for wire, value in zip(self.input_wires, values):
            wire.value = value

    def evaluate(self) -> List[bool]:
        for gate in self.gates:
            gate.evaluate()
        return [wire.value for wire in self.output_wires]

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