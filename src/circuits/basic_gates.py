
class Wire:
    def __init__(self):
        self.value = None
        self.connections = []

class Gate:
    def __init__(self):
        self.input_wires = []
        self.output_wire = None

    def connect_input(self, wire: Wire):
        self.input_wires.append(wire)
        wire.connections.append(self)

    def connect_output(self, wire: Wire):
        self.output_wire = wire
        wire.connections.append(self)

class ANDGate(Gate):
    def evaluate(self):
        if len(self.input_wires) != 2:
            raise ValueError("AND gate requires exactly 2 inputs")
        result = self.input_wires[0].value and self.input_wires[1].value
        self.output_wire.value = result
        return result

class NOTGate(Gate):
    def evaluate(self):
        if len(self.input_wires) != 1:
            raise ValueError("NOT gate requires exactly 1 input")
        result = not self.input_wires[0].value
        self.output_wire.value = result
        return result