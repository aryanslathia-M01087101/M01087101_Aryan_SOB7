greeting = input("Hello, possible pirate! What's the password?")  # fixed missing quote and bracket

# check if pirate password is correct
if greeting in ["Arrr!"]:  #  replaced ) by ]
	print("Go away, pirate.")
else:  # fixed elif error
	print("Greetings, hater of pirates!")  # fixed indentation