def bmi_calc(weight,height):

    height=height/100

    if weight<=0 or height<=0 :
        print("Enter valid positive values greater than 0")
    else: 
        BMI=weight/(height**2)
        bmi=round(BMI,2)
        print(bmi)

        if BMI<18.5:
            print("You are underweight")
        elif BMI<25:
            print("You are Normal")
        elif BMI<30:
            print("You are overweight")
        else:
            print("You are obese")

weight=int(input("Enter your weight in kg : "))
height=int(input("Enter your height in cm : "))
bmi_calc(weight,height)