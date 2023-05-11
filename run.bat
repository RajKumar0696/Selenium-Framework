REM pytest -v -s -m "regression" --html=./Reports/reports.html testCases/ --browser chrome
pytest -v -s -m "sanity" --html=./Reports/reports.html testCases/ --browser chrome
REM pytest -v -s -m "regression and sanity" --html=./Reports/reports.html testCases/ --browser chrome
REM pytest -v -s -m "regression or sanity" --html=./Reports/reports.html testCases/ --browser chrome


rem- meaning is comment out the commands.now non REM line only execute


REM pytest -v -s -m "regression" --html=./Reports/reports.html testCases/ --browser firefox
pytest -v -s -m "sanity" --html=./Reports/reports.html testCases/ --browser firefox
REM pytest -v -s -m "regression and sanity" --html=./Reports/reports.html testCases/ --browser firefox
REM pytest -v -s -m "regression or sanity" --html=./Reports/reports.html testCases/ --browser firefox
