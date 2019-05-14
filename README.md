# mobile_applications_testing

1. Test environment:<br>
<ul>
<li> Windows 7, 32-bit, IntelCore5, 3.5 GB RAM</li>
<li> Java v1.8.0_171</li>
<li> Android Studio v3.1.2</li>
<li> Nodejs v8.11.2</li>
<li> npm v5.6.0</li>
<li> Appium v1.8</li>
<li> Appium-doctor v1.4.3</li>
<li>PyCharm 2018.1.3</li>
<li> Python v2.7</li>
<li>Appium Python Client v0.42</li>
<li>Selenium v3.3.1</li>
<li> Gigaset GS170 with Android v7.0</li>
  </ul>
2. Test cases:<br>
TC1_WIFI settings handling with API Demos<br>
The name of the application testing : API Demos<br>
The number and name of the test case: TC1_WIFI settings handling with API Demos<br>
Steps:<br>
1. Click "Preference" in the application API Demos.<br>
2. Click "Preference dependencies" in the application API Demos.<br>
3. Print the amount of checkboxs. <br>
4. If the WIFI checkbox  is not checked check it.<br>
5. Click the WIFI settings and write: "1234".<br>
6. Click OK button.<br>
7. Force return to the home screen.<br>
Expected results:<br>
The amount of the checkboxs: 1 and checkbox WIFI in Preference dependencies is checked.<br>
The file name: tc1.py<br>
<br>
TC2_Form filling in contact manager app<br>
The name of the application testing:  Contact Manager<br>
The number and name of the test case: TC2_Form filling in contact manager app<br>
Steps: <br>
1. Click "Add contact" in the application Contact Manager.<br>
2. Fill fields: Contact name, Contact phone, Contact email.<br>
3. Check the correctness of the entered data.<br>
4. Click Save button.<br>
Expected results:<br>
In the application Contact Manager a contact is created.<br>
File name: tc2.py<br>
<br>
TC3_Notification_testing<br>
The name of the application testing: -<br>
The number and name of the test case: TC3_Notification_testing<br>
Steps:<br>
1. Open notifications.<br>
2. Search the notifications.<br>
3. Find the notification with the title: "USB debugging connected" and the content :"Tap to disable USB debugging".<br>
4. If it finds this text, display the content and title of the notification.<br>
5. Do assertions.<br>
6. Push back button.<br>
Expected results:<br>
The notification exists.<br>
File name: tc3.py<br>
