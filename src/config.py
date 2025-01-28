NETWORK_CONFIG = {
    "network": "testnet",
    "rpc_user": "your_rpc_user",
    "rpc_password": "your_rpc_password",
    "rpc_host": "localhost",
    "rpc_port": 18332
}

CIRCUIT_CONFIG = {
    "max_gates": 1000,
    "timeout_blocks": 144,  # 1 day
    "min_confirmations": 6
}

COMMITMENT_CONFIG = {
    "hash_function": "sha256",
    "blinding_size": 32
}