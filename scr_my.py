# Gnome sort
k = 1
v = 2
def gnome_sort(unsort_str):
    unsort = [each for each in unsort_str]
    i = 1
    while i < len(unsort):
        if unsort[i - 1] <= unsort[i]:
            i += 1
        else:
            tmp = unsort[i]
            unsort[i] = unsort[i - 1]
            unsort[i - 1] = tmp
            i -= 1
            if i == 0:
                i=1
    return unsort


stri = ['8', '8', '8', '8', '8', '7', '7', '7', '7', '6', '5', '4']
print gnome_sort("76588888765765")
print gnome_sort(['8', '8', '8', '8', '8', '7', '7', '7', '7', '6', '5', '4'])
if __name__ == "__main__":
    print gnome_sort(stri)
