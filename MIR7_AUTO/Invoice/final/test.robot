*** Settings ***
Library    OperatingSystem
*** Variables ***
${rate}           6091.70

*** Test Cases ***
T3
	sleep    4s
	${output}=    Run    python    F:\\Invoice\\final\\condition.py    WITH OPTION    Capture Output
    ${crt}=    Evaluate    ${output.strip()}    # Remove leading/trailing whitespace
    Log    ${crt}