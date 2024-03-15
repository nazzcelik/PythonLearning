#############################
# Uygulama - Mülakat Sorusu
#############################
# Amaç: Aşağıdaki şekilde string değiştiren bir fonksiyon yazmak istiyoruz.

# Before: hi my name is naz and i am learning python.
# After: Hi My NaMe iS NaZ aNd i aM LeArNiNg pYtHoN.


def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("hi my name is naz and i am learning python.")
