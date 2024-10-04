# Barge-Surface-Area-Mass-and-Draft-Calculation-Program
This Python program, my first project in my first year of computer science, calculates a barge's surface area, mass, and draft height based on user input for its dimensions. It factors in the barge's open top, calculates the mass using iron's density, and determines how much of the barge is submerged.

# Code Breakdown:

### Input Values for Dimensions:
The user is prompted to input three values:
- `L`: Length of the barge (in meters)
- `B`: Breadth of the barge (in meters)
- `H`: Height of the barge (in meters)

```python
L = float(input("enter barge length (in meters): "))
B = float(input("enter the barge breadth (in meters): "))
H = float(input("enter the barge height (in meters): "))

Surface Area Calculation:
The formula for the surface area (SA_of_barge) accounts for the fact that the barge does not have a lid. The surface area of a rectangular object (with no top) is the sum of the areas of the two sides, two ends, and the bottom.
Formula used:
SA_of_barge = (2*L*H + 2*B*H + L*B)

Mass Calculation:
The mass of the barge is based on the surface area and the density of iron. The code assumes that the weight of the iron used is 1.06 kg per square meter.
Formula used:
Mass_of_barge = (1.06 * SA_of_barge)

Draft Height Calculation:
The draft height is the amount of the barge that would be submerged in water, and it is calculated by dividing the mass of the barge by the area of the base of the barge (L \cdot B).
Formula used:
Draft_height = Mass_of_barge / (L * B)

Output:
The program prints out:

print("Length: ", L, "Breadth: ", B, "Height: ", H)
print(f"the surface area of the barge in m^2 is: {SA_of_barge:.2f}")
print(f"the mass of the draft in KG is: {Mass_of_barge:.2f}")
print(f"the draft of the barge in metres is: {Draft_height:.2f}")

Test Cases:
At the bottom of the code, there are sample test cases with specific values for L, B, and H, along with the corresponding expected output for surface area, mass, and draft height. Each test compares expected and actual outputs.

Example Test:
For the input values:

Length = 76 m, Breadth = 22 m, Height = 5 m
Expected output:
Surface area = 2652.00 m²
Mass = 2811.12 kg
Draft height = 1.68 m
Actual output matches the expected output, marked as "ok."

Purpose:
This code is useful for calculating the key characteristics of a rectangular barge made of iron, particularly the mass and how deep it will sit in water when placed into a body of water.





