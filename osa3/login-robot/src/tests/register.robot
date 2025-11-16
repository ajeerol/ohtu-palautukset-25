*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kimi  kimi1234
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kaisa  kaisa123
    Output Should Contain  User with username kaisa already exists

Register With Too Short Username And Valid Password
   Input Credentials  kt  hyvaksytty1
    Output Should Contain  Invalid username: username too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  ääkköset  aakkoset1
    Output Should Contain  Invalid username: use chars between [a-z]

Register With Valid Username And Too Short Password
    Input Credentials  aakkoset  ss
    Output Should Contain  Invalid password: password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kelpotunnari  vaanKirjaimet
    Output Should Contain  Invalid password: only alpha chars used


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kaisa  kaisa123
