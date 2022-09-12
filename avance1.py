bacteria = 0
agua = 0
planta = 0 
import random 
x = random.randint (1,4)

if x == 1 or x == 4:
    x = "B"
    bacteria = bacteria +1 
else: 
    if x == 2:
     x = "A"
     agua = agua +1 
    else: 
        if x == 3:
            x = "P"
            planta = planta +1
    
y = random.randint (1,4)

if y == 1 or y == 4:
    y = "B"
    bacteria = bacteria +1 
else: 
    if y == 2:
        y = "A"
        agua = agua +1
    else:
        if y == 3:
            y = "P"
            planta = planta +1
z = random.randint (1,4)
if z == 1 or z == 4:
    z = "B"
    bacteria = bacteria +1 
else: 
    if z == 2: 
        z = "A"
        agua = agua +1
    else: 
        if z == 3:
            z = "P"
            planta = planta +1

a = random.randint (1,4)
if a == 1 or a == 4:
    a = "B"
    bacteria = bacteria +1 
else: 
    if a == 2:
        a = "A"
        agua = agua +1
    else:
        if a == 3:
            a = "P"
            planta = planta +1
b = random.randint (1,4)
if b == 1 or b ==4: 
    b = "B"
    bacteria = bacteria +1 
else: 
    if b == 2:
        b = "A"
        agua = agua +1
    else:
        if b == 3:
            b = "P"
            planta = planta +1
c = random.randint (1,4)
if c == 1 or c == 4: 
    c = "B"
    bacteria = bacteria +1 
else: 
    if c == 2:
        c = "A"
        agua = agua +1
    else: 
        if c == 3: 
            c = "P"
            planta = planta +1
d = random.randint (1,4)    
if d == 1 or d == 4: 
    d = "B"  
    bacteria = bacteria +1      
else: 
    if d == 2: 
        d = "A"
        agua = agua +1
    else: 
        if d == 3: 
            d = "P"
            planta = planta +1
e = random.randint (1,4)    
if e == 1 or e == 4: 
    e = "B"       
    bacteria = bacteria +1 
else: 
    if e == 2: 
        e = "A"
        agua = agua +1
    else: 
        if e == 3: 
            e = "P"  
            planta = planta +1
f = random.randint (1,4)    
if f == 1 or f == 4: 
    f = "B"       
    bacteria = bacteria +1 
else: 
    if f == 2: 
        f= "A"
        agua = agua +1
    else: 
        if f == 3: 
            f = "P"  
            planta = planta +1 
g = random.randint (1,4)    
if g == 1 or g == 4: 
    g = "B"
    bacteria = bacteria + 1    
else: 
    if g == 2: 
        g = "A"
        agua = agua +1
    else: 
        if g== 3: 
            g= "P" 
            planta = planta +1   
            
h = random.randint (1,4)    
if h == 1 or h == 4: 
    h = "B"
    bacteria = bacteria +1        
else: 
    if h == 2: 
        h = "A"
        agua = agua +1
    else: 
        if h == 3: 
            h = "P"
            planta = planta +1 
            
i = random.randint (1,4)    
if i == 1 or i == 4: 
    i = "B"    
    bacteria = bacteria +1    
else: 
    if i == 2: 
        i= "A"
        agua = agua +1
    else: 
        if i== 3: 
            i= "P" 
            planta = planta +1 
j = random.randint (1,4)    
if j == 1 or j == 4: 
    j = "B"   
    bacteria = bacteria +1     
else: 
    if j == 2: 
        j= "A"
        agua = agua +1
    else: 
        if j == 3: 
            j = "P" 
            planta = planta +1 
k = random.randint (1,4)    
if k == 1 or k == 4: 
    k = "B"   
    bacteria = bacteria +1     
else: 
    if k == 2: 
        k = "A"
        agua = agua +1
    else: 
        if k == 3: 
            k = "P"    
            planta = planta +1   
l = random.randint (1,4)    
if l == 1 or l == 4: 
    l = "B"
    bacteria = bacteria +1        
else: 
    if l == 2: 
        l = "A"
        agua = agua +1
    else: 
        if l == 3: 
            l = "P"  
            planta = planta +1 
m = random.randint (1,4)    
if m == 1 or m == 4: 
    m = "B"  
    bacteria = bacteria +1      
else: 
    if m == 2: 
        m = "A"
        agua = agua +1
    else: 
        if m == 3: 
            m = "P"  
            planta = planta +1 

print ("----------------------")     
print ("|",x,"|" "|",y,"|" "|",z,"|""|",a,"|")     
print  ("----------------------")  
print ("|",b,"|" "|",c,"|" "|",d,"|""|",e,"|")     
print ("----------------------")         
print ("|",f,"|" "|",g,"|" "|",h,"|""|",i,"|")
print ("----------------------")
print ("|",j,"|" "|",k,"|" "|",l,"|""|",m,"|")

print ("la cantidad de bacterias en el cuadrante es:", bacteria,) 
print ("la cantidad de agua en el cuadrante es:", agua) 
print ("la cantidad de planta en el cuadrante es:", planta)
print ("el porcentaje de bacteria en el cuadrante es %", bacteria*100/16)
print ("el porcentaje de agua en el cuadrante es %", agua*100/16)
print ("el porcentaje de planta en el cuadrante es %", planta*100/16)
if bacteria > agua or bacteria > planta: 
    print ("el elemento que tiene mayor ocurrencia es bacteria")
else:
    if agua > bacteria or agua > planta: 
        print ("el elemento que tiene mayor ocurrencia es el agua" )
    else: 
        if planta > agua or planta > bacteria: 
            print ("el elemento que tiene mayor ocurrencia es planta")

if bacteria == agua:
    print ("en el cuadrante el elemento bacteria ha empatado con el elemento agua")
else: 
    if bacteria == planta: 
        print ("en el cuadrante el elemento bacteria ha empatado con el elemento planta")
    else: 
        if agua == planta: 
            print ("en el cuadrante el elemento agua ha empatado con el elemento planta")
