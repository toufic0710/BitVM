# BitVM Demo Implementation

A simplified implementation of BitVM concepts demonstrating circuit evaluation and verification, in Python.

## Overview

This project demonstrates core BitVM concepts including:
- Boolean circuit construction and evaluation
- Commitment schemes
- Challenge-response verification

## Features

### Currently Implemented
- **Basic Logic Circuit Implementation**: 
  - AND and NOT gates
  - Wire and Gate abstractions
  - Circuit evaluation
- **Simple Commitment Scheme**:
  - Basic SHA-256 based commitments
  - Challenge-response verification
- **Testing Framework**:
  - Unit tests for circuit evaluation
  - NAND gate truth table verification

## Quick Start

1. Setup virtuel environment

```
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```
pip install -e .
```

3. Run the simple circuit example:

```python3 examples/simple_circuit.py```

4. Run Tests

```pytest tests/```

## Core Components

### Circuit Components
- `Wire`: Represents boolean connections between gates
- `Gate`: Base class for logic gates
- `Circuit`: Manages circuit structure and evaluation

### Verification Protocol
- `Commitment`: Basic commitment scheme implementation
- `Challenger`: Verification challenge generation
- `Responder`: Challenge response handling

## Educational Purpose

This implementation is for educational purposes to demonstrate:
1. How boolean circuits can represent computation
2. Basic concepts of commitment schemes
3. Simple challenge-response protocols

## Limitations

This is a teaching example and is NOT a complete BitVM implementation. It lacks:
- Bitcoin integration
- Complete VM operations
- Transaction handling
- Proper fraud proofs
- State channels
- Many other BitVM features

## License

Copyright © 2024 Toufic Batrice. All rights reserved.