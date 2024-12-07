def divide_by_min(arr):
    if not arr:  # Agar massiv bo'sh bo'lsa
        return []

    min_value = min(arr)  # Massivning eng kichik elementini topish

    result = []  # Natijani saqlash uchun yangi massiv
    for num in arr:
        if num < min_value:
            result.append(num / min_value)  # Kichik elementlarni bo'lib chiqish
        else:
            result.append(num)  # Qolgan elementlarni o'zgartirmasdan qo'shish
    return result

# Sinov uchun massiv
arr = [12, 5, 3, 15, 7]
new_arr = divide_by_min(arr)
print(new_arr)