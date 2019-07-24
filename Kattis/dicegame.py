ga1, gb1, ga2, gb2 = map(int, input().split())
ea1, eb1, ea2, eb2 = map(int, input().split())

def mediumValue (a1, b1, a2, b2):
    return (a1 + b1) / 2 + (a2 + b2) /2
    
gunnar = mediumValue(ga1, gb1, ga2, gb2)
emma = mediumValue(ea1, eb1, ea2, eb2)

if gunnar > emma:
    print("Gunnar")
elif gunnar < emma:
    print("Emma")
else:
    print("Tie")