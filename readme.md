1 - Title of the program: 
    
   **Flat Mates Bill**


2 - Objective:

 > Calculate the bill per each flatmate according to their length of stay in the house and generate pdf report.


3 - Method:
   - Calculate price per stay
   - Identify flatmates
   - Calculate length of stay per each flatmate
   - Generate PDF Report pertaining total bill pre flatmate


4 - Tasks: 
   - Bill - Calculate: 
                        Input -> Bill, Period(days)
   - Bill per Flatmate - Calculate: 
                        Input -> Name, Bill, length of stay, 
   - Generate PDF - Print: 
                        Input -> Names, Bill per Flatmate, Bill
    

5 - Description: Input? -> Output?
    
  > An App that gets as input the amount of a bill for a particular period and the days that each of the flatmates stayed in the house for that period and returns how much each flatmate has to pay. It also generates a PDF report stating the names of the flatmates, the period, and how much each of them had to pay.
    
    
6 - Define Objects:--> Task --> 
    Identify Nouns in description
   - amount -> Calculate -> Output
   - bill -> per flatmate -> Output
   - period -> Input
   - days -> number -> Input
   - flatmates -> Identify names -> Input
   - house -> house price -> Input
   - PDF Report -> generate -> Output

7 - Process: 
 >Flatmates --> Stay in House -> Calculate days-Bill per Flatmate -> Generate PDF Bill



8 - Objects: 

    > Attributes
    ----------------
    > Methods



    Class Bill:
    --------------------
    > Attributes
    --------------------
        - amount
        - period
    --------------------
    > Methods
    --------------------
    none
        
        
        
        
    Class BillPerFlatmate:
    ---------------------
    > Attributes
    ---------------------
        - FlatMate_name
        - Period of stay
    ---------------------
    > Methods
    ---------------------
        - pays()
    ---------------------
    
    
   
        
    Class PdfReport:
    ---------------------
    > Attributes
    ---------------------
        - filename
    ---------------------
    > Methods
    ---------------------
        - generate_pdf(
                flatmate1,
                flatmate2,
                bill)
        
    