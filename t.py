import random

class Mix():
    """Generates m (default: 50) questions with operands between 1 and n (default: 100), using addition, subtraction,
    multiplication, and division operators."""

    def __init__(self, num_questions=50, max_operand_value=100):
        self.num_questions = num_questions
        self.max_operand_value = max_operand_value

    def __str__(self):
        return f'{self.num_questions} questions with operands between 1 and {self.max_operand_value}, using addition, subtraction, multiplication, and division operators.'

    def __repr__(self):
        return self.__str__()

    def generate_question(self, operator):
        """Generates a question with operands between 1 and max_operand_value, using the specified operator."""
        while True:
            num1 = random.randint(1, self.max_operand_value)
            num2 = random.randint(1, self.max_operand_value)
            if operator == '÷' and num1 % num2 != 0:
                continue
            elif operator == '-' and num1 - num2 < 0:
                continue
            else:
                break
        return f'{num1} {operator} {num2} = '

    def generate_questions(self, operators):
        """Generates num_questions questions using the specified operators."""
        questions = []
        for i in range(self.num_questions):
            s = ''
            for operator in operators:
                s += self.generate_question(operator)
            questions.append(s)
        return questions

    def generate_file(self, filename, operators):
        """Generates questions and saves them to a file."""
        questions = self.generate_questions(operators)
        with open(filename, 'w') as f:
            for i, question in enumerate(questions):
                print(f'{question:<20}', end='\t', file=f)
                if (i+1) % 3 == 0:
                    print('\n', file=f)

    def add(self):
        """Generates questions using addition operator."""
        self.generate_file('calcu.txt', ['+'])

    def sub(self):
        """Generates questions using subtraction operator."""
        self.generate_file('calcu.txt', ['-'])

    def mul(self):
        """Generates questions using multiplication operator."""
        self.generate_file('calcu.txt', ['×'])

    def div(self):
        """Generates questions using division operator."""
        self.generate_file('calcu.txt', ['÷'])

    def add_sub(self):
        """Generates questions using addition and subtraction operators."""
        self.generate_file('calcu.txt', ['+', '-'])


    def mul_div(self):
        global sign
        sign = ['×', '÷']
        self.__all()

    def mix(self):
        global sign
        sign = ['+', '-', '×', '÷']
        self.__all()
