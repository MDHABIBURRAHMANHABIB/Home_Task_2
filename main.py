'''Q1: As a CEO of your company, you can have 20% of the company’s profit as your
salary per month. Last year, from January to April the company purchased 30,000
BDT each month and sold 50,000 BDT products each month. From May to December
purchased 20,000 BDT each month and sold out 45,000 BDT products each month. If
you calculate your total salary for last year, how much it is?'''

print ('Home Task 02 Solved by Habib' )
print ('From January to April (4 months), the salary is = (profit * 20%), A = ((50000-30000) x 4) x 0.20 \n\n')
print ('From May to December (8 months), the salary is = (profit * 20%), B = ((45000-20000) x 8) x 0.20\n\n')
print ('The total salary for last year A + B \n\n')
print ('The total salary is BDT ', ((((50000-30000) * 4) * 0.20) + (((45000-20000) * 8) * 0.20)))

'''Q2: Suppose, Last year in June, Sylhet had a rainfall of 20cm, Chattogram had 40cm,
Dhaka 35 cm. But, Bogura had only 20mm. If, Sylhet, Chattogram and Dhaka
decreased by 5cm of rainfall every next month till October and Bogura increased by
2cm every next month till October, then calculate the total rainfall of each area at the
end of October.'''

print ("Sylhet Rainfall: ", 20+(20-5)+(20-2*5)+(20-3*5)+(20-4*5), "cm")
print ("Chattogram Rainfall: ", 40+(40-5)+(40-2*5)+(40-3*5)+(40-4*5), "cm")
print ("Dhaka Rainfall: ", 35+(35-5)+(35-2*5)+(35-3*5)+(35-4*5), "cm")
print ("Bagura Rainfall: ", 2+(2+2)+(2+2*2)+(2+3*2)+(2+4*2), "cm")

'''Q3: Some bricks of 12cm (Length), 6cm (Width), and 2cm (height) size is used to build a
wall of 100m2 Area. How many full bricks can be used to build the wall? (Hint: brick
area = length x width)'''

print ("Required number of bricks are: ", int (100 // (0.12*0.06)))