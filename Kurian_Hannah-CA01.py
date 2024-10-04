# Kurian_Hannah, CA-01.py, October 2023
# input 3 values for L,B and H

L = float(input("enter barge length (in meters): "))
B = float(input("enter the barge breadth (in meters): "))
H = float(input("enter the barge height (in meters): "))

# barge does not have a lid
# iron has a weight of 1.06kg

SA_of_barge= (2*L*H + 2*B*H + L*B)
Mass_of_barge= (1.06 * SA_of_barge)
Draft_height= Mass_of_barge/ (L*B)

#four output variables below

print("Length: ", L, "Breadth: ", B, "Height: ",H)
print(f"the surface area of the barge in m^2 is: {SA_of_barge:.2f}")
print(f"the mass of the draft in KG is: {Mass_of_barge:.2f}")
print(f"the draft of the barge in metres is: {Draft_height:.2f}")


# Kurian_Hannah-CA01.py
# input 5 values

#Test       L,B,H              Expected SA of barge, Mass of barge, Draft height        Actual SA of barge, Mass of barge, Draft height             Comment 

#1         76,22,5               2652.00, 2811.12, 1.68                                      2652.00, 2811.12, 1.68                                   ok 
#2         80,30,9               4380.00, 4642.90, 1.93                                      4380.00, 4642.90, 1.93                                   ok
#3         120,75,20             16800.00, 17808.00, 1.98                                    16800.00, 17808.00, 1.98                                 ok
#4         60,15,4               1500.00, 1590.00, 1.77                                      1500.00, 1590.00, 1.77                                   ok
#5         150,45,11             11040.00, 11702.40, 1.73                                    11040.00, 11702.40, 1.73                                 ok




