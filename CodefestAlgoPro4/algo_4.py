import time

stime = time.time()

# Class to convert words and numbers
class Transfer(object):
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    thousand = ['', 'thousand', 'million', 'billion']
    lt20 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    def Display(self, n):
        if n == 0:
            return 'zero'
        ans = ''
        i = 0
        while n > 0:
            if n % 1000 != 0:
                ans = f'{self.find(n % 1000)}{Transfer.thousand[i]} {ans}'
                i += 1
                n //= 1000
            return ans.strip()

    def find(self, x):
        if x == 0:
            return ''
        elif x < 20:
            return Transfer.lt20[x] + ' '
        elif x < 100:
            return Transfer.tens[x // 10] + ' ' + self.find(x % 10)
        else:
            return f'{Transfer.lt20[x // 100]} hundred and {self.find(x % 100)}'


Transfer = Transfer()
mydict = {}

for i in range(999, 0, -1):
    mydict[Transfer.Display(i)] = str(i)

mydict.update(
    {
        'equals': '=',
        'multiple': '*',
        'plus': '+',
        'substract': '-',
        'division': '/',
        '=': '==',
    }
)

# Read input file
with open('input.txt', 'r') as fp:
    filedata = fp.read()

# To reset output file data
with open('outputfile.txt', 'w') as fp:
    pass

for key, val in mydict.items():
    filedata = filedata.replace(key, val)

filedata = filedata.split('\n')[:-1]

n = int(filedata[0])
problem = filedata[1:]

for Que in range(len(problem)):
    prob = problem[Que]
    prob = prob.strip()

    with open('outputfile.txt', 'a') as fp:
        fp.write(f'Que_{Que+1} :: {str(eval(prob)).lower()}\n')

print('Outputfile.txt has been generated............')
