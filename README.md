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
  3. [Sustainable Development Goals (SDG) Integration on the Project](#sustainable-development-goals-sdg-integration-on-the-project)
  4. [Instructions on how to run the Program](#instructions-on-how-to-run-the-program)
  5. [Gratitude Statement](#Gratitude-Statement)
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

The following are the instructions that guides you on how the Angat Buhay Lahat: Donation through Philippine Geography Exploration project works.

-**START OF THE PROGRAM**
  -  Run the program in a python environment.
  -  The program will prompt the user a welcome message.
  -  At the beginning of the game, it will ask the user what region of the Philippines they want to play. Note that the selection of region is case sensetive, if the user did not uinput the exact word on the choices, the program will then let the user to choose again.

<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/welcome message.png" alt="welcome message" width="370" height="200""
</div>
    
-**GAME PROPER**
  -  After succesfully entering the region that you want to play, the program will then prompt random provinces from the chosen region until all of the provinces are answered.
  -  The user will only have three (3) attempts to answer. Each attempt has a corresponding point. 1st attempt is equal to 5 points, 2nd attempt is equal to 3 points while the third attempt is equal to only 1 point. If the user is not able to answer what is the capital of that specific province, the program will proceed to the next province.

<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/phase1.png" alt="phase1" width="370" height="200""
</div>
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/game proper.png" alt="game proper" width="370" height="350""
</div>

-**CONTINUATION OF PLAY**
  -  After the user have finished answering one region, the program will then ask the user whether they want to continue playing or not.
  -  If yes, then the program will then let the user to choose again in the region to play.
  -  If no, the program will prompt the user how many points they got upon playing the game.
<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/continue playing.png" alt="continue playing" width="370""
</div>

-**CONVERSION OF POINTS INTO COINS**
  -  The accumulated points can be used by the user too convert into coins. The program will ask the user whether they want to convert their points into coins or not.
  -  5 points is equivalent to 1 peso, however, the total accumulated points should be more than 10 in order for it to be converted innto coins.
  -  If the user picked yes, the points will be converted into coins, and if no, a thank you message will be prompted.

<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/stop play.png" alt="stop play" width="370""
</div>

-**SENDING COINS TO GCASH ACCOUNT**
  -  After the user has coverted the points into coins, the user will then let the user to enter the Gcash number that will be used to receive the coins.
  -  If an invalid Gcash number has been entered, the program will ask the user again to re-enter the correct number.
  -  After a succesful transaction, a thank you message will be prompted.

<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/GCASH.png" alt="GCASH" width="370""
</div>

-**DONATION SECTION**
  -  After sending the coins into GCASH, the program will ask the user whether they want to donate it to ANGAT BUHAY FOUNDATION.
  -  If no, then a "Thank you for playing the game, your coins are yours to keep" message will be prompted.
  -  If yes, the program will give the user the link of ANGAT BUHAY FOUNDATION where they can click it and donate the coins that they got from the game.

<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/donation (2).png" alt="donation (2)" width="370" height="15""
</div>

<div align="right side">
  <img src="https://github.com/Gio-Campit/CS121_FinalProject/blob/main/images/Instructions/AngatBuhayDonation.png" alt="AngatBuhayDonation" width="400" height="350""
</div>

 <hr class="w-48 h-1 mx-auto my-4 bg-gray-100 border-0 rounded md:my-10 dark:bg-gray-700">
</div>

### GRATITUDE  STATEMENT
Making this project on my own has been very challenging especially I do not excel that much when it comes to coding, but fortunately I survived it. First and foremost, I would like to thank our dear Creator on giving me strenght and wisdom so that I can finish this project. To my family and of course to our magandang professor Ma'am Fatima Marie Agdon(ma'am maganda ka po talaga hindi dahil sa nanghihingi ako ng uno kundidahil maganda ka po talaga haha), thank you for giving us the knowledge about this course and for eagerly teaching us regardless of the situatios that our class have encountered. Lastly to myself of course, there are days that you want to give up but you didn't, just don't be too dramatic next time okay?? We still have a capstone on our third and fourth year(do' nalang tayo umiyak self).


