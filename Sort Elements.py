
elements = []
num_of_element = int(input("Please enter number of elements : "))

for i in range(num_of_element):
    ele = [input("Please enter the element : ")]
    elements.append(ele)

print(elements)
asce = sorted(elements)
print(asce)
desce = sorted(elements, reverse=True)
print(desce)
