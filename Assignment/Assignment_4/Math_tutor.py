import random


class MathTutor:
    
    def mathquestions():
        operators = ["+","-","*","/"]
        operator = random.choice(operators)
        firstnumber = random.randint(1, 100)
        secondnumber = random.randint(1, 100)

        question = f"{firstnumber} {operator} {secondnumber} = ??"
        
        if operator == "+":
             answer = firstnumber + secondnumber
        elif operator == "-":
            answer = firstnumber - secondnumber
        elif operator == "*":
            answer = firstnumber * secondnumber
        else:
            answer = firstnumber / secondnumber
        
        print(question)
        return answer
     
     
class MathScore(MathTutor): 
    @staticmethod
    def mathscorecalculator():
        count = 0
        point = 0
        confirmation = "y"
        while confirmation.lower() == "y":
            count += 1
            answer = MathTutor.mathquestions()
            user_answer = float(input("enter a number:"))
            if user_answer == answer:
                point += 1
            confirmation = input("Do you want to continue (y/n):") 
        total_score = f"{point}/{count}" 
        print(total_score)
        
mathscore = MathScore
mathscore.mathscorecalculator() 
                
        

            
              

