letter = ''' Dear <|Name|>,
        You are selected! <|Date|> '''

print(letter.replace("<|Name|>", "Akshay").replace("<|Date|>", "10 January"))