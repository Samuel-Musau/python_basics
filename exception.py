jina="python excp"
for j in jina:
    if(j!=1):
        print(j)

x=["python","exception","try"]
try:
    for i in range(3):
        print(f"the element and index from list is {i,x[i]}")
except:
    print("index out of range")