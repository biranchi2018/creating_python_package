
from biranchi.calculator import add, sub, mul, div

 
def test_package():
	a, b = 2, 5
	print(f'a : {a}, b : {b}')
	
	add_result = add(a, b)
	print(f'add : {add_result}')
	
	sub_result = sub(a, b)
	print(f'sub : {sub_result}')

	mul_result = mul(a, b)
	print(f'mul : {mul_result}')

	div_result = div(a, b)
	print(f'div : {div_result}')
	

if __name__ == '__main__':
	test_package()