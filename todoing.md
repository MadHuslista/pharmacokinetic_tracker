
# TODOING

# PRIORITY BECAUSE NEEDED

# Notification
- When peak is reached -> Remember the user to cultivate it: 
  - Eat fruit sugar to fed the brain
  - Do sports to increase the blood flow
  - Wrap yourself in hoodie to avoid expending energy into temp regulation work
  - BE AWARE OF ATTENTION FRAGILITY AND BE CAREFUL TO DO NOT DIVERT FROM CURRENT TASKS

# Library
- Create the independent libraries (branch feature/libraries): 
  - #	{ include = "pk_engine" },
  - #	{ include = "pk_db" },
  - # { include = "pk_visuals"}

- Add them to the poetry file 

# Then reevaluate with what to continue. 
  - Basic DB enabling? 

# Solved
+ Add a second axis, so I have both, the time and the delay 
  + -> solved with mplcursor annotation
+ Add CLI info returned. 
  - Last dosage time 
  - Last dosage delay
  - Current time
  - Current delay
  - Current cp
  - time of next at effective threshold. 
  - Example: 
  ```
  | Last dosage time:       | Current time:            |
  | - 2021-03-01 12:00:00   | - 2021-03-01 12:00:00    |
  | Last dosage delay:      | Current delay:           |
  | - 0                     | - 0                      |
  | Time of next dosage:    | Current cp:              |
  | - 2021-03-01 12:00:00   | - 0.5                    |
  ``` 
