## **What time is it?** 

Write a function that returns the time (as a  formatted string,  for 
e.g.`12:04`, `3:20` or `6.30`, where minutes is always in 2 digits) based on 
the position of  hour hand and the minute hand. The position will be denoted 
as two angular values. Each angular value `x` where `0` <= `x` <= `360`,  
would have 
  - `0` degree pointing to  `12`
  - `90` degree pointing to `3` and 
  - `180` degree pointing to `6` 

and so forth. 

### Bonus
Make the calculation to be as quick as possible. And the code should also be 
quite readable as well. 
 
**Clue**: it must be equal to or faster than your own brain, and equally 
elegant in how it goes about it! 

### Extra Bonus 
If the angular value of the hour hand should be greater than 360, the string 
representing the calculated time value would have to be returned along with 
the suffix `pm`. For e.g. `3:21pm` or `11.00pm`, etc. 