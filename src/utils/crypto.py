import hashlib
from typing import Tuple
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

def generate_keypair() -> Tuple[bytes, bytes]:
    """Generate ECDSA keypair"""
    private_key = ec.generate_private_key(ec.SECP256K1())
    public_key = private_key.public_key()
    return private_key.private_bytes(), public_key.public_bytes()

def hash256(data: bytes) -> bytes:
    """Double SHA256"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()