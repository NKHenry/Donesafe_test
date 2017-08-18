# Donesafe Code Test

## A few notes about this test
This test is here to give people an opportunity to show off their skills.  It isn't supposed to be super realistic or strenuous to you as a candidate. You should be spending a bit of time on this but if you've suddenly found yourself spending too long (>= 3 hours) on it get in contact at <careers@donesafe.com> and talk to us about it.  There are a few things to point out:
* We don't mind what language or you use or how you structure your fileds, if it's code we should be geek enough to get it.  Though please feel free to explain your choices 🙂
* This is about your thinking, we'd love to see your thinking
* Engineering values like TDD are important to us, so they should be evident in your submission

## Background
Here at Donesafe there are a couple of important numbers that our customers rely on.

One of the most sensitive calculations is for [worker's compensation][1].  In particular, as part of their worker's compensation we use a calculation called [PIAWE][2].  PIAWE is the way we work out how much someone who is unable to work gets paid.

In this case we have four people (found in `people.json`) who need payments.  PIAWE is a confusing and difficult thing for both employees and employers but for the purposes of this code test you'll be pleased to know we're going to simplify things a bit 🙂

There's a sliding scale of payments based on how long you've been injured, and how you get paid (this can be found in `rules.json`).  Our job at Donesafe is to make sure the worker is getting the correct payment.  It's also to make sure the employer is fulfilling their obligations to the employee and regulatory authorities.

## File Structure
### people.json
This is the list of people who need workers compensation payments.
Each person has:
* name - the employee's name
* hourlyRate - how much they are paid per hour
* overtimeRate - how much they are paid per overtime hour
* normalHours - the number of hours per week they usually work
* overtimeHours - the number of hours they get paid overtime for
* injuryDate - when they were injured

### rules.json
This is the set of rules used to calculate payments for people.
Each rule has:
* applicableWeeks - the number of weeks from the date of injury this level of payment is used at
* percentagePayable - what percentage of an employee's qualifiying wage is due back to the employee
* overtimeIncluded - whether overtime hours are part of the qualifying wage


## The tasks
* How much should we pay each of the injured people in `people.json` this week?
* Can you calculate and list their payments for each of their injuries in a report? This report does not need to be anything special, creating a CSV file would work, so would outputting something to STDOUT.

## Questions
OK, we *think* that should be enough to get you rolling.  However, we aren't perfect so if you spotted a mistake or you have a question please contact us <careers@donesafe.com> and we'll work it out with you.

[1]: https://www.fairwork.gov.au/leave/workers-compensation "Fairwork Australia Workers Compensation Page"
[2]: http://www.worksafe.vic.gov.au/injury-and-claims/compensation-and-entitlements/weekly-payments-and-current-work-capacity
