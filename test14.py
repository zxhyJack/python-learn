# while
count = 1
while count <= 5:
    print(count)
    count += 1

prompt = '\nTell me something, and I will repeat it back to you:\nEnter "exit" to end the program.'
message = input(prompt)
while message != 'exit':
  message = input(prompt)
  if message != 'exit':
    print(message)