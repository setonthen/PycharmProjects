* Settings *
Documentation    validate application homepage and login
Library  SeleniumLibrary
Resource  MyKeyWords.robot  # this is calling our variable files into this project
Resource  Variables.robot
Suite Teardown  close all browsers     #this code is used to close all the opened browser windows

##
#RobotFramework Run commands
#robot .\automationpractice_homepage_login.robot
#robot -d Reports -i .\automationpractice_homepage_login.robot
#robot -d Reports -i Joshua1 --variable USER_EMAIL:setonthen_autotesting@gmail.com  --variable USER_PASSWORD:testing .\automationpractice_homepage_login.robot
##



* Test Cases *
Verify that logo and add to cart are displayed on homepage
    [Tags]  Joshua
    Check homepage logo and add to cart
    #[Teardown]  close browser               #this part of the code is to close the browser after successfully running the test

Valid Login
    #[Tags]  Joshua1
    Login user   ${USER_EMAIL}   ${USER_PASSWORD}
    #[Teardown]  close browser


Invalid Login1: wrong user address with right password
    [Tags]  Joshua2
    Login with incorrect username      setonthen_auto@gmail.com     testing
    #[Teardown]  close browser

Invalid Login2: wrong password but right email
#    [Tags]  Joshua3
    Login with incorrect password       setonthen_autotesting@gmail.com     test
    #[Teardown]  close browser


Valid error messages for incorrect login    # the section of code below is data driven test
    #[Tags]  Joshua4
    [Template]  verify error messages for different invalid login scenarios
    #username                         Paasword    Error messages
    setonthen_autotesting@gmail.com   test        Invalid password.
    setonthen@gmail.com               testing     Authentication failed.
    ${EMPTY}                          Testing     An email address required.
    #[Teardown]   close browser

Verify that users can retrieve forgotten password
    [Tags]  Joshua5
    [Setup]  Get to login page            #Setup is a word in selenium for precondition
    Retrieve User Password    ${FORGOT_PASSWORD_LINK}   ${FORGOT_PASSWORD_EMAIL}   setonthen_autotesting@gmail.com   ${RETRIEVE_PASSWORD_BUTTON}


* Keywords *
verify error messages for different invalid login scenarios
    [Arguments]  ${username}  ${paasword}  ${errormessage}
    Open Browser   ${URL}  ${BROWSER}
    click element   ${HOMEPAGE_SIGNIN_BUTTON}
    input text  ${LOGIN_USERNAME_FIELD}  ${username}
    input text  ${LOGIN_PASSWORD_FIELD}    ${paasword}
    click element   ${LOGIN_BUTTON}
    page should contain  ${errormessage}
    #[Teardown]  close browser