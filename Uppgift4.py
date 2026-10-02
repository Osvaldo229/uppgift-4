while True:



     print("detta är en loop")

     stop=input("skriv q för att stoppa det: ")

     if stop.lower()== "q" :

         print("Programmet har avslutats.")  

         break




for i in range(10):
    print(i + 1)

x = 0

while True:
    x += 1
    print(x)
    
    if x == 15:
        break

for i in range(10):
    print(5)


y = int(input("skriv ett tal: "))
 
for i in range(1, y): 
    print(i + 1)

for i in  range( 1, 13):
    print ( "2 *", i, "=", 2 * i)