# Bug Report: Incorrect Mathematical Operation

## Bug ID
CALC-001

## Status
Open

## Priority
High

## Severity
Major

## Description
The calculator function is performing division instead of multiplication when given two numbers as input.

## Steps to Reproduce
1. Launch the calculator application
2. Enter first number: 10
3. Enter second number: 5
4. Click on multiply button

## Expected Result
The result should be 50 (10 * 5)

## Actual Result
The result is 2 (10 / 5)

## Environment
- Application Version: 1.0.0
- Operating System: macOS Monterey 12.5
- Browser/Platform: Chrome 96.0.4664.110

## Additional Information
- Bug appears consistently on all test cases
- No error messages are displayed
- Operation symbol shows '*' but performs '/' instead

## Attachments
- Screenshot of incorrect calculation result
- Test case ID: TC_MULT_001

## Reporter
John Doe

## Date Reported
2024-01-20
