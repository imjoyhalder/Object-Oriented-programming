class student:
    def __init__(deal,name,roll,marks):
        deal.name = None
        deal.roll = roll 
        deal.marks = 90
        print("I want to be a Software Engineer")
    
    def test(deal):
        print(f"My name is {deal.name}")
        print(f"My roll  is {deal.roll}")
        print(f"My marks {deal.marks}")

object = student("JOY","643736",20)
object.test()