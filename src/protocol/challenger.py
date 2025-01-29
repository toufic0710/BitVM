from typing import List, Dict
from ..circuits.basic_gates import Gate
from .commitment import Commitment
from ..circuits.circuit import Circuit

class Challenge:
    def __init__(self, gate_index: int, expected_output: bool):
        self.gate_index = gate_index
        self.expected_output = expected_output
        self.input_values = []  # Store input values for verification

class Challenger:
    def __init__(self):
        self.challenges: List[Challenge] = []
        
    def verify_circuit(self, circuit: Circuit, commitments: Dict) -> bool:
        """Verify circuit execution through challenges"""
        for gate_index, gate in enumerate(circuit.gates):
            challenge = self.create_challenge(gate_index)
            self.challenges.append(challenge)
            
            # Get response from circuit
            response = {
                'gate_index': gate_index,
                'inputs': [wire.value for wire in gate.input_wires],
                'output': gate.output_wire.value
            }
            
            if not self.verify_response(response, challenge):
                return False
        return True
    
    def create_challenge(self, gate_index: int) -> Challenge:
        """Create a challenge for a specific gate"""
        challenge = Challenge(gate_index, None)  # output will be verified later
        challenge.input_values = []  # can be populated with expected inputs
        return challenge
    
    def verify_response(self, response: dict, challenge: Challenge) -> bool:
        """
        Verify the response to a challenge
        """
        if response['gate_index'] != challenge.gate_index:
            return False
            
        for input_value in response['inputs']:
            if not isinstance(input_value, bool):
                return False
                
        if not isinstance(response['output'], bool):
            return False
            
        if challenge.expected_output is not None:
            if response['output'] != challenge.expected_output:
                return False
                
        if challenge.input_values:
            if response['inputs'] != challenge.input_values:
                return False
        
        return True