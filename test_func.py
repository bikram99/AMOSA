from math import *


def DTLZ1(input_arr, n_obj):
    n_var = len(input_arr)
    k = n_var - n_obj + 1
    out = [0.0]*n_obj
    g = 0.0
    for i in range(n_var-k, n_var):
        g = g + ((input_arr[i] - 0.5)**2) - cos(20*pi*(input_arr[i] - 0.5))
    g = 100*(k+g)
    for i in range(1, n_obj+1):
        s = 0.5 * (1 + g)
        j = n_obj - i
        while j >= 1:
            j = j - 1
            s = s * input_arr[j]
        if i > 1:
            s = s * (1 - input_arr[n_obj - i])
        out[i-1] = s
    return out


def DTLZ2(input_arr, n_obj):
    n_var = len(input_arr)
    k = n_var - n_obj + 1
    out = [0.0]*n_obj
    g = 0.0
    for i in range(n_var-k, n_var):
        g = g + ((input_arr[i] - 0.5)**2)
    for i in range(1, n_obj+1):
        s = (1.0 + g)
        j = n_obj - i
        while j >= 1:
            j = j - 1
            s = s * cos(pi*input_arr[j]*0.5)
        if i > 1:
            s = s * sin(input_arr[n_obj - i]*pi/2)
        out[i-1] = s
    return out


def DTLZ3(input_arr, n_obj):
    n_var = len(input_arr)
    k = n_var - n_obj + 1
    g = 0.0
    for i in range(n_obj-1, n_var):
        g += (((input_arr[i]-0.5)**2) - cos(20.0*pi*(input_arr[i]-0.5)))
    g = (k+g)*100
    out = [0.0]*n_obj
    for m in range(0, n_obj):
        product = (1+g)
        i = 0
        while((i+m) <= n_obj-2):
            product *= cos(input_arr[i]*pi/2)
            i += 1
        if m > 0:
            product *= sin(input_arr[i]*pi/2)
        out[m] = product
    return out


def DTLZ4(input_arr, n_obj, a=100):
    n_var = len(input_arr)
    k = n_var - n_obj + 1
    g = 0.0
    for i in range(n_obj-1, n_var):
        g += ((input_arr[i]-0.5)**2)
    out = [0.0]*n_obj
    for m in range(0, n_obj):
        product = (1+g)
        i = 0
        while((i+m) <= n_obj-2):
            product *= cos((input_arr[i]**a)*pi/2)
            i += 1
        if m > 0:
            product *= sin((input_arr[i]**a)*pi/2)
        out[m] = product
    return out


def SCH1(input):
    func1 = input**2
    func2 = (input-2.0)**2
    out = [func1, func2]
    return out


def SCH2(intput):
    func1 = float()
    if(input <= 1):
        func1 = - input
    elif (input > 1 and input <= 3):
        func1 = input - 2
    elif (input > 3 and input <= 4):
        func1 = 4 - input
    else:
        func1 = input - 4
    func2 = (input - 5)**2
    out = [func1, func2]
    return out



# functions left:
# DTLZ110
# DTLZ115
# DTLZ15
# DTLZ24
# DTLZ5
# DTLZ7
# Dev1
# Dev2
# Dev3
# Dev4
# ZDT1
# ZDT2
# ZDT3
# ZDT6
