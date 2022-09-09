import subprocess as sp
import random
import os

class ExcuteCode:
    def __init__(self, langauge, user_code):
        self.langauge = langauge
        self.user_code = user_code
        self.filename = self.generate_filename()
        self.temp_dir = 'temp/'
        self.output = ''
    
    def generate_filename(self):
        filename = ''
        for _ in range(12):
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            filename += (chr(random_integer))
        return filename

    def set_output(self, result):
        if result.stdout.decode() != '':
            self.output = result.stdout.decode()
        else:
            self.output = result.stderr.decode()

    def run(self):
        if self.langauge == 'py':
            self.run_python()
        elif self.langauge == 'c':
            self.run_c()
        elif self.langauge == 'cpp':
            self.run_cpp()
        elif self.langauge == 'js':
            self.run_js()
        elif self.langauge == 'java':
            self.run_java()
        else:
            pass
        return self.output
    
    def run_python(self):
        file = self.temp_dir + self.filename + '.py'
        with open(file, 'w') as f:
            f.writelines(self.user_code)
        result = sp.run(['python3', file], capture_output= True)
        self.set_output(result)

    def run_c(self):
        file = self.temp_dir + self.filename + '.c'
        output_file = self.temp_dir + self.filename
        with open(file, 'w') as f:
            f.writelines(self.user_code)
        result = sp.run(['gcc', file, '-o', output_file], capture_output= True)
        if result.stderr.decode() != '':
            self.set_output(result)
            return
        result = sp.run([output_file], capture_output= True)
        self.set_output(result)

    def run_cpp(self):
        file = self.temp_dir + self.filename + '.cpp'
        output_file = self.temp_dir + self.filename
        with open(file, 'w') as f:
            f.writelines(self.user_code)
        result = sp.run(['g++', file, '-o', output_file], capture_output= True)
        if result.stderr.decode() != '':
            self.set_output(result)
            return
        result = sp.run([output_file], capture_output= True)
        self.set_output(result)

    def run_js(self):
        file = self.temp_dir + self.filename + '.js'
        with open(file, 'w') as f:
            f.writelines(self.user_code)
        result = sp.run(['node', file], capture_output= True)
        self.set_output(result)

    def run_java(self):
        pass

