# broj = 4
# broj_2 = 5

# def brojac(broj):
#     broj += 1
#     broj = broj + broj_2
#     return broj
    
# print(brojac(2))    
# print(broj)
# print(broj_2)

broj = 6
def brojac():
    global broj
    broj += 1
    return broj

print(brojac())
print(broj)

