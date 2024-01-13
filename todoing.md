
# TODOING

# PRIORITY BECAUSE NEEDED


# Notification
- When peak is reached -> Remember the user to cultivate it: 
  - Eat fruit sugar to fed the brain
  - Do sports to increase the blood flow
  - Wrap yourself in hoodie to avoid expending energy into temp regulation work
  - BE AWARE OF ATTENTION FRAGILITY AND BE CAREFUL TO DO NOT DIVERT FROM CURRENT TASKS

- Convertir a Python 3 la simulación => E: Herramienta para controlar mi salud 
    REQUISITOS: 
    - Idea: Un log permanente en csv. 
        - Convert to hours!!
        - CLI: "New dosis"  => Add the new dosis and etc. 
        - Simulation "New dosis" + current time
            - Add an slider for the new dosis! 
        - API: (h: hour / q: quantity) 
            aft --now()
            aft --clean_time()
            aft --steady_state() => superimpose steady state from now
            aft -a --add_new_dose --h 20.00 --q 1 
            aft -s --sim_new_dose --h 19.00 --q 1
            aft -d --display_doses 
        - Add mean dosage => Search about it     
        - Add a message option also. So, if a have a message I could write it in a separate log (not in a csv, but open a txt file. I feel it like open nano o vscode, and write normally; but the hour, day and etc its auto) 
            - And also add a litle tick with a message notification in the graph 

    + Updated to hour axis
    + Add API, and autocompute the intervals of time. 
    - Agregar periodos de sueño!
    - How to check this shit from App? 



# Library
- Create the independent libraries (branch feature/libraries): 
  - #	{ include = "pk_engine" },
  - #	{ include = "pk_db" },
  - # { include = "pk_visuals"}

- Add them to the poetry file 

# Then reevaluate with what to continue. 
  - Basic DB enabling? 

# Solved
+ Upate the `run_pk -p` behavior, when is fed without args 
    -> should give current time. 
    -> Options would be: 
        - `run_pk -p` -> Inmediatly return the delay
        - Ask if edit any input (i think this would be better)
    - Make it so it would be easy to change option


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

# Refs
  - Ocupar la idea del gist PERO aplicar la otra librería 
  - Revisar otras referencias también
  - Refs specific with LDX
      - https://gist.github.com/icook/899fcc7187d2d0ae5f57
      - https://github.com/crowsonkb/pharmacokinetics => demo funcional: https://kath.io/pk/
  
  - Refs of PK/PD: 
      Google: python pharmacokinetics
      - https://allendowney.github.io/ModSimPy/chap17.html
      - https://demo.popypkpd.com/
      - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6363067/

# OPTIONALS: 
- Make a Pull Request
    - https://medium.com/@topspinj/how-to-git-rebase-into-a-forked-repo-c9f05e821c8a

