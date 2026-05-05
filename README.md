# Clinic Accelerator Take Home Assignment

## How to run (Python 3.13.9)
  1. clone repo and cd into the folder using a termainl
  2. run in terminal: pip install -r requirements.txt
  3. run in terminal: python3 convert.py

## JSON format example
I chose this format because it seemed to me that each header has 4 properties that we would want to track. Also if we would want to add more information to the headers like maybe a target value, we can just add it in.
```json
  {
  "February 16, 2026": [
    {
      "Total Revenue \n- All Services": {
        "value": 40454.28,
        "focus": "Financial",
        "source": "EMR",
        "role": "J"
      },
    }],
  } 
```

## What I decided to do about the messy bits (merged cells, spacer columns, formulas, etc.) and what trade-offs I made
  1. Pandas does not make any distinction betweel normal cells and merged cells, so I decided to just display them all. I figured this might be OK since you can acess these cells directly in the actual xlsx file.
  2. Wasn't sure what to do with formulas, so I just used the values
  3. I used pandas beacuse it seems to be more effiecient in data analysis and dealing with larger data. openpyxl would be better at keeping the formatting. I decided to not keep the value formatting like $ or % signs.

## Changes I would make with infinite amount of time
  1. Change how the headers and values are being seperated. Right now it is a hardcoded and any changes to the number of headers would probably break it. I would try to make the logic more dynamic.
  2. I noticed some cells are color coded, so I would like to add some distinction to them as well in the JSON
  3. The cells for phone performance can probably all be categorized into one
  4. Add formatting to the values like % and $ 
