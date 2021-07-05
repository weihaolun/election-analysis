# Election Audit with Python

## Overview of Election Audit

### Background
We have been helping Tom, an employee from Colorado Board of Election to audit the election results for US congressional precinct in Colorado. The results are tabulated and were given to us as [csv file resource](https://github.com/weihaolun/election-analysis/blob/161dd8acccf89241788970adec1b838c3c1545a3/Resources/election_results.csv).

Previously, we have completed following parts of auditing using Python script:
-	Total number of votes received.
-	A list of voted candidates’ names with number of votes and the percentage of votes they received.
-	A summary of election winner results: winning candidate’s name, winning vote count and winning percentage.
-	Printed and saved above results to a text file (as screenshot below).

     ![part1_result](https://user-images.githubusercontent.com/84211948/124236667-63e64000-dab2-11eb-8716-3ee1d550d3d5.png)

### Purpose
The purpose of this challenge is to complete the election audit using Python by adding the following parts:
-	The voter turnout for each county.
-	The percentage of votes from each county.
-	The county with the highest county.
-	Print and save above results to the text file [election_results.txt](https://github.com/weihaolun/election-analysis/blob/161dd8acccf89241788970adec1b838c3c1545a3/analysis/election_results.txt).

The following sections of this report will address the overall results of the election audit, and a recommendation summary of re-using the script for future elections.

## Election Audit Results
- **How many votes were cast in this congressional election?**

  - There are total **369,711** votes casted through three types of voting methods (mail-in, punch cars and memory cards).

- **Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.**

     |   County   |   Percentage  |     Votes     |
     | ------------- | ------------- | ------------- |
     | Jefferson | 10.5%  | 38,855  |
     | Denver  | 82.8%  | 306,055  |
     | Arapahoe  | 6.7%  | 24,801  |

- **Which county had the largest number of votes?**

  - County **Denver** had the largest number of votes.
  
- **Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.**

     |   Candidate   |   Percentage  |     Votes     |
     | ------------- | ------------- | ------------- |
     | Charles Casper Stockham | 23.0%  | 85,213  |
     | Diana DeGette  | 73.8%  | 272,892  |
     | Raymon Anthony Doane  | 3.1%  | 11,606  |
 
- **Which candidate won the election, what was their vote count, and what was their percentage of the total votes?**
  
  -  The winner of the election was Diana DeGette.
The winning vote count was 272,892, and the percentage of winning votes was 73.8%.

_Note: Please refer to the termimal screenshot below or click [here](https://github.com/weihaolun/election-analysis/blob/161dd8acccf89241788970adec1b838c3c1545a3/analysis/election_results.txt) to see printed results summary._

   ![result](https://user-images.githubusercontent.com/84211948/124241370-69925480-dab7-11eb-95b3-eb6052b9faab.png)

## Election Audit Summary
The core advantage of the election audit Python script is the reusability. The script can be used for other elections with simple modification. In this section, I will present two examples of how the script could be modified for other elections.

1. First, this script can be used for another similar election with minimum modification. When it’s the same congressional election for other counties, or it’s the senatorial election in the same counties, the modifications would be just on the data source.
- In this case, the data structure would be the same since the voting methods remain the same (mail-in, punch cars and memory cards). The columns in dataset would also be Ballot ID, County and Candidate.
- Modification on data source:
   - Before: The data source is _**election_results.csv**_ in Resources folder, and we saved results as a text file into analysis folder.
     ```
     # Assign a variable to load a file from a path.
     file_to_load = os.path.join("Resources", "election_results.csv")
     # Assign a variable to save the file to a path.
     file_to_save = os.path.join("analysis", "election_results.txt")
     ```
   - After: We can put the new data source _**new_election.csv**_ into Resources folder again, and save results as another text file into anlysis folder and give it a new name _**new_results.txt**_
     ```
     # Assign a variable to load a file from a path.
     file_to_load = os.path.join("Resources", "new_election.csv")
     # Assign a variable to save the file to a path.
     file_to_save = os.path.join("analysis", "new_results.txt")
     ```  
- After above modification, a new result will be pulled from the new election data source and saved to a new text file. This sould work with any local election with candidate name and voters' county.

2. Now the votes are filtered by counties, we can re-use the script for elections in cities and even states by modifying variable’s name. Let's change "county" to "state" for example:
   - Before:
    ```
   county_list = []
   county_votes = {}
   winning_county_count = 0
   winning_county_count = 0
   winning_county_percentage = 0
   county_name
   county_count
   county_percentage
   county_results
    ```
   - After:
    ```
   state_list = []
   state_votes = {}
   winning_state_count = 0
   winning_state_count = 0
   winning_state_percentage = 0
   state_name
   state_count
   state_percentage
   state_results
    ```

  - With above modification, printed result will be listed as -state- instead of counties. As mentioned above, this modification would also apply to "city", "district", "area" etc.

3. If the election needs an extra filter, for example, keep counties and add cities, we can add a code section in the script just like what we did for counties. This way, we can get results for both counties and cities.

- Create a city list, city votes dictionary, and create variables to track winning cities if necessary.
  ```
  city_list = []
  city_votes = {}

  winning_city = ""
  winning_city_count = 0
  winnint_county_percentage = 0
  ```
- In the for loop, after extracting candidate name and county name, extract city name as as well. (Let's assume city name is collected into the 4th column in csv file.)
  ```city_name = row [3]

- Also in the for loop, add an if statement to add cities into the city list. Then begin tracking city votes.
  ```
  if city_name not in city_list:
    city_list.append(city_name)
    city_votes[city_name] = 0
  city_votes[city_name] += 1
  ```
- Create a for loop to get city results, this part can be written between county for loop and candidate for loop.
  ```
  for city_name in city_votes:
    city_count = city_votes[city_name]
    city_percentage = float(city_count) / float(total_votes) * 100
    city_results = (f"{city_name}: {city_percentage:.1f}%) ({city_count:,})\n")
    txt_file.write(city_results)
  ```
- Write an if statement to determine the winning city and get its vote counts.
  ```
  if (city_count > winning_city_count) and (city_percentage > winning_city_percentage):
  winning_city_count = city count
  winning_city_percentage = city_percentage
  winning city = city_name
  ```
- Print the city turnout
  ```
  winning_city_summary = (
      f"\n"
        f"-------------------------\n"
        f"Largest City Turnout: {winning_city}\n"
        f"-------------------------\n")
    print(winning_city_summary)
  ```
-After adding above coding blocks, we will get a seperate set results for different cities. We can also add more filter such as "district" or "state" by adding similar code.
