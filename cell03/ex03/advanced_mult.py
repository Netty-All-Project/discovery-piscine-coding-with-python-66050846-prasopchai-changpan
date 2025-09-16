start = 0
while start <= 10:
    print(f"Table de {start}: ", end="") #end="" พิมพ์แล้วไม่ขึ้นบรรทัดใหม่
    de = 0
    while de <= 10:
        result = start * de
        if de == 10:
            print(f"{result}")
        else:
            print(f"{result} ", end="")
        de += 1
    start += 1