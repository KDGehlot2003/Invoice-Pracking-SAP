*** Settings ***
Library           Process
Library           String

*** Test Cases ***
Check Condition
    ${output}    Run Process    python    F:\\Invoice\\final\\condition.py
    ${lowercase_output}    Convert To Lowercase    ${output.stdout}
    ${boolean_result}    Evaluate    '${lowercase_output}' == 'true'
    Log To Console    ${boolean_result}
    WHILE    ${boolean_result} == True
    BuiltIn.Log To Console    ${boolean_result} YEAH!
    BREAK
    END
