import time

def read_text_file (file_path):

    with open(file_path, "r") as f:
        data = f.readlines()
        data = [line.replace("\n","") for line in data]

    return data


# opcode (3 bit / 1 int 0 to 7), operand (3 bit / 1 int 0 to 7)


class Computer_3Bit(object):

    def __init__(self, initA, initB, initC, program):
        self.A = initA
        self.B = initB
        self.C = initC

        self.instruction_pointer = 0
        self.output = []

        self.program = program

    def print_A(self):
        A_bin_actual = bin(self.A)

        A_list = []

        A_bin = str(A_bin_actual)
        A_bin = A_bin[2:]
        A_bin = A_bin[::-1]

        for i in range(1+(len(A_bin)-2)//3):
            A_list.append(int(A_bin[3*i:3*i+3][::-1], 2))

        A_list.reverse()

        print(bin(self.A), A_list)

    def run(self):
        
        while self.instruction_pointer < len(self.program):
            #self.print_A()
            self.next_instruction()

    def next_instruction(self):

        opcode = self.program[self.instruction_pointer]
        operand = self.program[self.instruction_pointer + 1]

        if opcode == 0:
            self.adv(operand)

        elif opcode == 1:
            self.bxl(operand)

        elif opcode == 2:
            self.bst(operand)

        elif opcode == 3:
            self.jnz(operand)

        elif opcode == 4:
            self.bxc(operand)

        elif opcode == 5:
            self.out(operand)    

        elif opcode == 6:
            self.bdv(operand)   

        elif opcode == 7:
            self.cdv(operand)

        else:
            raise Exception("Invalid operand")      

        self.instruction_pointer += 2

    def combo_operand(self, operand):

        if operand < 0 or operand > 7:
            raise Exception("Invalid Operand")
        
        elif operand <= 3:
            return operand
        
        elif operand == 4:
            return self.A
        
        elif operand == 5:
            return self.B
        
        elif operand == 6:
            return self.C
        
        elif operand == 7:
            raise Exception("Invalid Operand")
        
        else:
            raise Exception("Invalid Operand")
        
        
    def adv(self, operand):
        # Opcode 0, division

        self.A = self.A // (2**self.combo_operand(operand))

    def bxl(self, operand):
        # Opcode 1, bitwise xor
        self.B = self.B ^ operand

    def bst(self, operand):
        # Opcode 2, combo operand modulo 8
        self.B = self.combo_operand(operand) % 8

    def jnz(self, operand):
        # Opcode 3, jump if A not zero

        if self.A != 0:
            self.instruction_pointer = (operand - 2) #Subtract 2 so value is correct after 2 is added

    def bxc(self, operand):
        # Opcode 4, bitwise XOR of register B and register C

        self.B = self.B ^ self.C

    def out(self, operand):
        # Opcode 5, calculates the value of its combo operand modulo 8, then outputs that value

        self.output.append(self.combo_operand(operand)%8)
        #self.print_A()

    def bdv(self, operand):
        # Opcode 6, same as adv, but result in B
        self.B = self.A // (2**self.combo_operand(operand))
    
    def cdv(self, operand):
        # Opcode 7, same as adv, but result in C
        self.C = self.A // (2**self.combo_operand(operand))

    def print_out(self):

        return ",".join([str(i) for i in self.output])

    @classmethod
    def init_from_data(cls, data):

        A = int(data[0][12:])
        B = int(data[1][12:])
        C = int(data[2][12:])

        program = [int(i) for i in data[4][9:].split(",")]

        return cls(A, B, C, program)

def part_1(data):

    #Register A: 729

    computer = Computer_3Bit.init_from_data(data)

    computer.run()

    return computer.print_out()


def part_2(data):

    out = []

    for j in range(8):
        print(j, test(data, j))

    for i in Computer_3Bit.init_from_data(data).program:

        match = False

        # if i == 0:
        #     out.append(0)
        #     match = True
        #     break
    
        for A in range(8):

            computer = Computer_3Bit.init_from_data(data)

            computer.A = A#<<3

            computer.run()

            if computer.output[0] == i:
                out.append(A)
                match = True
                break
        
        if not match:
            raise Exception(f"No match for {i}")
        else:
            print(A, "->", i)

    print(out)

    res = 0
    while out:
        res += out.pop()
        res = res << 3

    return res

def test(data, A):

    #Register A: 729

    computer = Computer_3Bit.init_from_data(data)
    computer.A = A
    computer.run()

    return computer.print_out()


if __name__ == "__main__":

    DAY = "17"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    part_2_start = time.time()
    res_part2 = part_2(data)
    print(res_part2)
    print(f"Part 2 finished in {time.time() - part_2_start} s")

    print(test(data, res_part2))

