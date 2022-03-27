class Stack():
	def __init__(self):
		self.stack = []

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()

	def peek(self):
		data = self.stack.pop()
		self.push(data)
		return data

	def isEmpty(self):
		if size() == 0:
			return True
		else:
			return False

	def size(self):
		return len(self.stack)

# Этот метод был нужен при отладке задания 1  
	def fill_by_char(self, data):
		if isinstance(data,str) == False:
			return -1
		count = 0  
		for c in data:
			self.push(c)
			count = count + 1
		return count  
      
BRACKETS = '[([])((([[[]]])))]{()}'#'}{}'#'{{[(])]}}'#'[[{())}]'#

def check_brackets(brackets):
	s = Stack()
	for i in BRACKETS:
		if i == '(' or i == '[' or i == '{':
			s.push(i)
		else:
			if s.size() > 0:
				check = s.peek()
				if (i == ')' and check == '(') or (i == ']' and check == '[') or (i == '}' and check == '{'):
					s.pop()
				else:
					return s.stack, False, f'нарушена последовательность {check}{i}'
			else:
				return s.stack, False, 'в начале блока идёт закрывающая скобка'
	return s.stack, True, 'сбалансирована.'

l,res,descr = check_brackets(BRACKETS)
if res == True:
	print(f'Последовательность {BRACKETS} {descr}')
else:
	print(f'Последовательность {BRACKETS} НЕ сбалансирована.'+ f'\nПричина: {descr}')