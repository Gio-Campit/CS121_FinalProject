<div align ="center">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/ANGAT.png"
" alt="Angat Buhay Lahat Logo" width ="650" height="500">
<h1>Angat Buhay Lahat: Donation Through Philippine Geography Exploration!</h1>

<p><b>IT 2104</b></p>
<a><p>CAMPIT, VIRGILIO L.</p></a>

 <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>



<details>
  <summary><strong>Table of Contents</strong></summary>

  1. [Project Overview](#project-overview)
  2. [Application of Python Concepts](#application-of-python-concepts)
  3. [Sustainable Development Goals (SDG) in the Project](sustainable-development-goals-(sdg)-in-the-project)
  4. [Instructions on how to run the Program](instructions-on-how-to-run-the-program)
</details>

---


### PROJECT OVERVIEW
  **Angat Buhay Lahat: DONATION THROUGH PHILIPPINE GEOGRAPHY EXPLORATION** is a philippine geography quiz game that enables the user to identify each capital of different provinces from the seventeen regions in the Philippines. The mere purpose of this system is to let the user learn the different capitals of the provinces from different regions while they can also help the ANGAT BUHAY FOUNDATION by just playing the game. In this game, users can accumulate points by getting the correct answer of the different questions and the points that they got can be converted into a coin in which these coins can be donated in the ANGAT BUHAY FOUNDATION to help them on their initiatives for the people. 

<hr class="w-48 h-1 mx-auto my-4 bg-pink-500 border-0 rounded md:my-10 dark:bg-pink-600">

### APPLICATION OF PYTHON CONCEPTS
  The following are the different python concepts applied in the program:

-**DICTIONARIES**
  - the program used a region dictionary that organizes data, storing regions as keys and provinces-capitals as nested dictionaries. It allows a quick lookup of regions and their respective provinces and capitals.
 
 **CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/dictionaries.png"
</div>

-**LOOPS**
  - this python concept enables iteration of all provinces in a chosen region through for loop, on the other hand, while loop allows the user to have 3 attempts to answer each question.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/loops.png"
</div>

-**CONDITIONAL STATEMENTS** 
  - if and else are used to manage the logic in order to check the correctness of answers as well as updating points or providing feedback. It implements the core logic of the quiz game.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/conditional statements.png"
</div>

-**STRING MANIPULATION** 
  - the .lower() method is used to ensure that the user input is compared in a case-insensitive manner. It improves its user-friendly feature by accepting any answers regardless of its capitalization.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/string manipulation.png"
</div>

  
  -**INPUT VALIDATION** 
    - the input validation checks if the chosen region exixts in the dictionary of program. This python concepts prevents the selection of invalid region guiding the user to input the valid region.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/inputvalidation1.png"
</div>
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/inputvalidation2.png"
</div>


-**MODULARITY OF PROGRAM** 
  - this python concepts is used in breaking down the program into smaller, independent functions for specific tasks. It also enhances the readability and maintainability of the program.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/modularity.png"
</div>

-**MATHEMATICAL OPERATIONS** 
  - it calculates points dynamically based on the number of attempts, it also implements the point system that is awarded to the user.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/mathoperations.png"
</div>


-**FUNCTION** 
  - the function convertToCoins is a function with return type in which it uses return statement in sending back the calculated coin value. It returns an integer if its insufficient (points is less than 10) while it returns a float when the points is valid for coin conversion. It provides the result to the caller allowing it to be reused and enables further processing of its output.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/functions.png"
</div>

-**DYNAMIC FEEDBACK** 
  - allowing the user to have a real-time feedback based on their choices and points in the game. It also allows the user to know about their progress.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/df1.png"
</div>
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/df2.png"
</div>


-**ERROR HANDLING** 
  - the error handling concept of python was used to validate the Gcash number by using a regular expression to ensure that it contains exactly 11 digits. It allows the user to prevent from inputting invalid data that may affect their transaction in transferring the coins accumulated to their Gcash.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/error handling.png"
</div>

-**REGULAR EXPRESSION** 
  - this python conncept is used in validating the Gcash number using a regex pattern that allows the user to only enter exactly 11 digits number. It ensures to input data accurately so that it will not affect the sensetive transactions like transferring coins into Gcash.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/regex.png"
</div>

  -**RANDOMIZATION** 
    - random.choice function is used to select a random province from the chosen region. This enables the program to prompt the user a random province when they are playing the game.

**CODE BLOCK**
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/CODEBLOCKS/randomization.png"
</div>


<hr class="w-48 h-1 mx-auto my-4 bg-pink-500 border-0 rounded md:my-10 dark:bg-pink-600">

  
  ### SUSTAINABLE DEVELOPMENT GOALS (SDG) INTEGRATION ON THE PROJECT
  
  While this project focuses on providing knowledge for the user about the different capitals of provinces in the Philippines, it also serves as a donation drive for a specific charity which is the Non-government Organization ANGAT BUHAY FOUNDATION. This project targets different Sustainable Development Goals as same as the ANGAT BUHAY FOUNDATION. The following are the different SDG integrated in the project:

  1. ZERO HUNGER - Through Angat Buhay Foundation, the donation that came from from this project will be donated to the foundation to help them in achieving this Goal by securing that there will be no people will suffer from Hunger.
  2. QUALITY EDUCATION - Aside from the fact that the project itself already gives the user a knowledge about the Philippines which also supports on having a quality education for everyone, through the organization, these initiatives can be widen even more by giving them additional support to achieve this goal. Angat Buhay Foundation is providing classroom, dormitories, and different learning materials that helpls the students to have an access to quality education that gives them a lifelong learning oppurtunities.
  3. GOOD HEALTH AND WELL BEING - Angat Buhay Foundation also aims to ensure that everyone have an access on different nutrition and healthcare programs.
  4. DECENT WORK AND ECONOMIC GROWTH - The organization also gives a free training for everyone who wishes to have a decent work by providing them a Voc-Tech Training as well as employment.
  5. GENDER EQUALITY - The organization helps in empowering the marginalized sectors including the women through creating a partnership with different private sectors and civil society partners. By ending domestic abuse against women and giving them financial independence is also a part of this goal.
  6. CLIMATE ACTION - Part of the endeavors of the organization is by giving the victims of different calamities and disaster-stricken areas an immediate assistance, supports rehabilitation initiatives as well as giving them an intervention about risk reduction and resiliency.

  In conclusion, making this project as a way of helping the ANGAT BUHAY FOUNDATION can help the organization to achieve its  initiatives for the people.

<hr class="w-48 h-1 mx-auto my-4 bg-pink-500 border-0 rounded md:my-10 dark:bg-pink-600">

  ### INSTRUCTIONS ON HOW TO RUN THE PROGRAM
