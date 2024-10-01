
s="vx"

try:
    print(11/0)
except NameError as e:
    print(f"{e} Sizda xatolik mavjud")
except ZeroDivisionError as e:
    print(f"{e} Sizda xatolik mavjud")

except:
    print("Siz qandaydir xatolik mavjud")
finally:
    print("Siz dasturni oxiriga yetib keldingiz.")

print(12345)
