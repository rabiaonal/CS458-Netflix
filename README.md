# CS458-Netflix

HOW TO RUN THE WEBPAGE
1) In order to see the webpage, one must have node.js on his/her computer as well as ejs and express modules that can be installed by simply running "npm install ejs" and "npm install express" on the command prompt or downloading the related modules.
2) After changing the directory to "src" that contains all the source code; by running "node app.js" from the terminal or the command prompt, one can easily see the webpage on the browser at the address "http://localhost:3000".
  
  -> node app.js

HOW TO RUN THE TESTS
1) To be able to run the selenium tests, one must have python 3 and selenium package installed by "pip install selenium" on his/her computer.
2) Also, selenium needs webdriver executables and corresponding browser executables installed on computer. Before running test script, one should get required driver from "https://www.selenium.dev/downloads/" and put it on directory "src" to run with script "Test.py".
3) The tests are in the file Test.py under directory "src", running "python Test.py [driver]" will run several tests and give the results.

  -> python Test.py Chrome
  -> python Test.py Firefox
  -> python Test.py Opera
