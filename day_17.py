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


def octal_list_to_int(a_list):
    # most significant bit first:

    queue = list(a_list)

    out = 0

    while queue :
        i = queue.pop(0)

        if i >= 8:
            raise Exception("Invalid octal")
        
        out = out << 3
        out += i
        
    return out

def check_next_bit_recursive(current_out, current_pos):

    cur_prog_match = Computer_3Bit.init_from_data(data).program[-(current_pos+1):]

    for A in range(8):

        test_A = current_out.copy()
        test_A.append(A)

        computer = Computer_3Bit.init_from_data(data)

        computer.A = octal_list_to_int(test_A)

        computer.run()

        assert len(computer.output) == len(cur_prog_match)

        if computer.output == cur_prog_match:

            if current_pos + 1 >= len(computer.program):
                return test_A
            else:
                
                res = check_next_bit_recursive(test_A, current_pos + 1)

                if res:
                    print(res, octal_list_to_int(res), test(data, octal_list_to_int(res)))
                    return res

    return None
    
def part_2(data):

    out = []

    for j in range(8):
        print(j, test(data, j))
    
    out = check_next_bit_recursive(out, 0)

    return octal_list_to_int(out)

def test(data, A):

    computer = Computer_3Bit.init_from_data(data)
    computer.A = A
    computer.run()

    return computer.print_out()

def calculate_min_and_max_A():
    # Largest 16-digit octal number (octal: 7777777777777777)
    max_A = int("7777777777777777", 8)
    
    # Smallest 16-digit octal number starting with 702642030660 (octal)
    min_octal_prefix = "7026420306"  # Given prefix
    min_A = int(min_octal_prefix.ljust(16, '0'), 8)  # Pad with zeros to make 16 digits

    return min_A, max_A

def find_lowest_initial_A_with_range(program, min_A, max_A):
    """
    Find the lowest initial value of A within a specified range [min_A, max_A]
    that causes the program to output a copy of itself.

    Args:
        program (list): The list of 3-bit numbers (the program).
        min_A (int): Minimum value for A to test.
        max_A (int): Maximum value for A to test.

    Returns:
        int: The lowest value of A that works, or None if no valid A is found.
    """
    for A in range(min_A, max_A + 1):  # Iterate through range [min_A, max_A]
       
        # Initialize the computer with the current value of A
        computer = Computer_3Bit(A, 0, 0, program)
        computer.run()
        
         # Print the current value of A being tested (in octal)
        # Print the resulting output
        print(f"Testing A = {oct(A)[2:]} (octal) -> Output: {computer.print_out()}")
        
        # Check if the output matches the program
        if computer.output == program:
            return A  # Return the first valid A found

    return None  # Return None if no valid A is found in the range

def part_2_bf():
    # Calculate min_A and max_A
    min_A, max_A = calculate_min_and_max_A()

    print(f"Min A (decimal): {min_A}")
    print(f"Max A (decimal): {max_A}")

    program = [2, 4, 1, 1, 7, 5, 0, 3, 4, 7, 1, 6, 5, 5, 3, 0]

    # Calculate min_A and max_A
    min_A, max_A = calculate_min_and_max_A()

    # Find the lowest valid A
    lowest_A = find_lowest_initial_A_with_range(program, min_A, max_A)

    if lowest_A is not None:
        print(f"The lowest initial value for register A is: {lowest_A}")
    else:
        print(f"No valid initial value for A was found in the range {min_A} to {max_A}.")


if __name__ == "__main__":

    DAY = "17"
    data = read_text_file(f"{DAY}.txt")
    part_1_start = time.time()
    print(part_1(data))
    print(f"Part 1 finished in {time.time() - part_1_start} s")

    #part_2_bf()

    part_2_start = time.time()
    res_part2 = part_2(data)
    print(res_part2)
    print(f"Part 2 finished in {time.time() - part_2_start} s")

    print(test(data, res_part2))

