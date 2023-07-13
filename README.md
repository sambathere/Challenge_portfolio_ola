# Task 1: Software configuration

Subtask 1: Why did I choose to participate in the challenge portfolio?

Hello! My name is Ola and I decided to be the part of this project because I love to learn new skills. It drives my motivation and confidence. When I gain knowledge I see all the new ways and doors opening for me, almost literally 😄
I learn Python for few months now and wanted to explore various possibilities it gives, including testing. I also hope for opportunity in carrer change in the future. 

Subtask 4: QUIZ
5/14

# Task 2: Selectors

Subtask 2: Find selectors on sign in page 

1. remind password_button_xpath
   
* //*[@id="__next"]/form/div/div[1]/a
* //*[text()="Remind password"]
* //child::div/a
   
2. sign in_button_xpath
   
* //*[@id="__next"]/form/div/div[2]/button/span[1]
* //button[contains(., 'Sign in')]
* //button[@type='submit' and span[contains(text(), 'Sign in')]]

3. language_button_xpath

* //*[@id="__next"]/form/div/div[2]/div/div
* //div[@class='MuiSelect-root MuiSelect-select MuiSelect-selectMenu MuiInputBase-input MuiInput-input' and @aria-haspopup='listbox']
* //*[text()="English"] / //*[text()="Polski"]


Task 3: Automatic test + asserts

To zadanie pozwoliło mi m.in.:

✅ poznać dogłębnie framework, na którym będę pracować,

✅ klikać w elementy na stronie,

✅ wypełniać pola tekstem,

✅ wykorzystać assert title, 

✅ uruchomić test.
