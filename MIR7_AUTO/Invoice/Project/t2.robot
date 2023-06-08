*** Settings ***
Library           AutoItLibrary
Library           RPA.Desktop

*** Variables ***
${rate}           6091.70

*** Test Cases ***
T1
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\goto_right.py
    sleep    1s
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\goto_right.py
    sleep    1s
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\goto_right.py
    sleep    1s
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\goto_right.py
    sleep    1s
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\goto_down.py
    sleep    1s
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\ctrla.py
    sleep    1s
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\ctrlc.py
    sleep    1s

T2
    Run    python F:\\11.11_Sharing\\11.11_sharing\\MIR7_AUTO\\fiinal\\script\\condition.py
    sleep    2s
    ${crate}    Set Variable    ${rate_to_be_checked}
    WHILE    ${rate} == ${crate}
    Log    Executed as long as the condition is True.
    BuiltIn.Log To Console    YEAH!
    BREAK
    END
