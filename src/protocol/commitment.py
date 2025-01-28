import hashlib
import secrets
from typing import Any, Tuple

class Commitment:
    @staticmethod
    def create(value: Any) -> Tuple[bytes, bytes]:
        """Create a commitment with a random blinding factor"""
        blinding_factor = secrets.token_bytes(32)
        value_bytes = str(value).encode()
        commitment = hashlib.sha256(value_bytes + blinding_factor).digest()
        return commitment, blinding_factor
    
    @staticmethod
    def verify(value: Any, commitment: bytes, blinding_factor: bytes) -> bool:
        """Verify a commitment"""
        value_bytes = str(value).encode()
        computed_commitment = hashlib.sha256(value_bytes + blinding_factor).digest()
        return computed_commitment == commitment

class CommitmentScheme:
    def __init__(self):
        self.commitments = {}
        
    def commit_to_circuit(self, circuit: 'Circuit') -> dict:
        """Create commitments for all wires in the circuit"""
        commitments = {}
        for wire in circuit.input_wires + circuit.output_wires:
            commitment, blinding = Commitment.create(wire.value)
            commitments[id(wire)] = {
                'commitment': commitment,
                'blinding': blinding
            }
        return commitments