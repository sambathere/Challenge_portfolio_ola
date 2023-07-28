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


# Task 3: Automatic test + asserts

To zadanie pozwoliło mi m.in.:

✅ poznać framework, na którym będę pracować,

✅ klikać w elementy na stronie,

✅ wypełniać pola tekstem,

✅ wykorzystać assert title, 

✅ uruchomić test.


# Task 4: Refactor, debugger and TC

Dysk Google:

https://drive.google.com/drive/folders/1smaZKkAngtYMGkoDLhayuQq_kyScp_xA?hl=pl

https://docs.google.com/document/d/1o6NgVOIhq02r0boQn1dAh_ujoR0QVQo6tosbjFxZ-0c/edit


1. Przypadek testowy: Logowanie użytkownika z funkcją wait - "visibility_of_element_located"

Opis: Test sprawdza funkcjonalność logowania użytkownika do strony internetowej.

Warunki początkowe:

- Aplikacja jest uruchomiona.
- Strona logowania jest wyświetlona.

Kroki testowe:

- Wprowadź poprawne dane użytkownika (prawidłowy login i hasło).
- Kliknij przycisk "Zaloguj" lub ‘ Sign in’ (w zależności od wersji językowej)

Oczekiwany wynik:

Użytkownik zostaje zalogowany i przekierowany do strony głównej.

Rzeczywisty wynik:

	Pass


Plik “ID_1 TC.mp4”

2. Przypadek testowy: Dodawanie gracza z poziomu shortcuts - ADD PLAYER

Opis: Test sprawdza funkcjonalność button ‘ADD PLAYER’ (shortcut)

Warunki początkowe:

- Aplikacja jest uruchomiona.
- Użytkownik jest zalogowany.
- Widok ‘MAIN PAGE’ ustawiony (domyślny)

Kroki testowe:

- Wprowadź poprawne dane użytkownika (prawidłowy login i hasło).
- Kliknij przycisk "Zaloguj" lub ‘ Sign in’ (w zależności od wersji językowej)
- Kliknij ‘ADD PLAYER’ button (shortcut)
- Wypełnij pole ‘Name’ 
- Wypełnij pole ‘Surname”
- Wypełnij pole ‘Main position’
- Wypełnij pole ‘Age’
- Wypełnij opcjonalnie pola ‘Phone’, ‘Weight’, ‘Height (cm)’, ‘Club’, ‘Level’, ‘Second position’, ‘Achievements’.
- Wybierz opcjonalnie ‘District’.
- Kliknij button “SUBMIT’.

Oczekiwany wynik:

Gracz jest dodany do listy ‘Players’

Rzeczywisty wynik:

	Pass


Plik “ID_2 TC.mp4”

3. Przypadek testowy: Wylogowywanie użytkownika ze strony

Opis: Test sprawdza funkcjonalność wylogowania użytkownika ze strony internetowej.

Warunki początkowe:

- Aplikacja jest uruchomiona.
- Strona logowania jest wyświetlona.

Kroki testowe:

- Wprowadź poprawne dane użytkownika (prawidłowy login i hasło).
- Kliknij przycisk "Zaloguj" lub ‘ Sign in’ (w zależności od wersji językowej)
- Kliknij przycisk ‘Sign out”

Oczekiwany wynik:

Użytkownik zostaje zalogowany i przekierowany do strony głównej, a następnie wylogowany ze strony internetowej.

Rzeczywisty wynik:

	Pass

Plik “ID_3 TC.mp4”

4. Przypadek testowy: Wyczyszczenie formularza (Players)

Opis: Test sprawdza funkcjonalność button ‘CLEAR’

Warunki początkowe:

- Aplikacja jest uruchomiona.
- Użytkownik jest zalogowany.
- Widok ‘MAIN PAGE’ ustawiony (domyślny)

Kroki testowe:

- Wprowadź poprawne dane użytkownika (prawidłowy login i hasło).
- Kliknij przycisk "Zaloguj" lub ‘ Sign in’ (w zależności od wersji językowej)
- Kliknij ‘ADD PLAYER’ button (shortcut)
- Wypełnij pole ‘Name’ 
- Wypełnij pole ‘Surname”
- Wypełnij pole ‘Main position’
- Wypełnij pole ‘Age’
- Kliknij button ‘CLEAR’.

Oczekiwany wynik:

Formularz zostaje wypełniony danymi, a następnie wyczyszczony.

Rzeczywisty wynik:

	Pass

Plik “ID_4 TC.mp4”

5. Przypadek testowy: Przejście do podanego kontaktu ze strony 

Opis: Test sprawdza funkcjonalność button ‘DEV TEAM CONTACT’.

Warunki początkowe:

- Aplikacja jest uruchomiona.
- Użytkownik jest zalogowany.
- Widok ‘MAIN PAGE’ ustawiony (domyślny)

Kroki testowe:

- Wprowadź poprawne dane użytkownika (prawidłowy login i hasło).
- Kliknij przycisk "Zaloguj" lub ‘ Sign in’ (w zależności od wersji językowej)
- Kliknij ‘DEV TEAM CONTACT’ button.

Oczekiwany wynik:

Strona przekierowuje do strony Slack

Rzeczywisty wynik:

	Pass

Plik “ID_5 TC.mp4”


# Task 5: Robot Framework

