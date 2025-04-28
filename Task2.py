#single weight ko double karna hai
# aur double weight ko single karna hai
# agar weight 0.5 se kam hai to usko 0.5 karna hai
# agar weight 0.5 se zyada hai to usko 0.5 se kam karna hai


weight =float(input("Enter the weight in kg:"))

Double_weight =2*weight
single_weight =weight/2
if weight<0.5:
    weight=0.5
    
    print("Weight is less than 0.5, so it is set to 0.5")
elif weight>0.5:
    weight=weight-0.5
    
    print("Weight is greater than 0.5, so it is reduced by 0.5")
print("Double weight is :",Double_weight)
print("Single weight is :",single_weight)
