make_short = lambda size='L', text='"I love Python"' : print(f"The size of the shirt is {size} and the text is {text}")

make_short()
make_short('M')    
make_short(size='S', text='"javascript forever"')

short = {'size': 'XS', 'text': '"I love C#"'}
make_short(**short)